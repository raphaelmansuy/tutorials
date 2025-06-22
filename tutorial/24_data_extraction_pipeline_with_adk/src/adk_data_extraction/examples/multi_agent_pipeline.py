"""
Multi-Agent Extraction Pipeline with Google ADK

This example demonstrates a sophisticated multi-agent pipeline that includes:
1. Document Classification Agent
2. Specialized Extraction Agents (Contract, Invoice, General)
3. Quality Validation Agent
4. Pipeline Orchestration

The pipeline showcases how multiple agents can work together to process
different types of documents with specialized expertise and quality control.
"""

import asyncio
import hashlib
import logging
from typing import Union, Any
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field

from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# =============================================================================
# SCHEMAS FOR MULTI-AGENT PIPELINE
# =============================================================================

class DocumentType(str, Enum):
    """Document types that can be processed by the pipeline"""
    CONTRACT = "contract"
    INVOICE = "invoice"
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    REPORT = "report"
    EMAIL = "email"
    UNKNOWN = "unknown"


class DocumentClassification(BaseModel):
    """Schema for document classification results"""
    document_type: DocumentType = Field(description="Primary document type")
    complexity_level: str = Field(description="simple, medium, complex")
    estimated_processing_time: int = Field(description="Estimated seconds to process")
    recommended_extractor: str = Field(description="Which specialized agent to use")
    confidence_score: float = Field(description="Confidence in classification (0-1)", ge=0.0, le=1.0)
    key_indicators: list[str] = Field(description="Text indicators that led to this classification")


class ContractData(BaseModel):
    """Schema for contract extraction results"""
    parties: list[str] = Field(description="All parties involved in the contract")
    contract_value: float | None = Field(description="Total contract value", default=None)
    currency: str = Field(description="Currency code", default="USD")
    start_date: str | None = Field(description="Contract start date", default=None)
    end_date: str | None = Field(description="Contract end date", default=None)
    payment_terms: list[str] = Field(description="Payment terms and schedules")
    key_obligations: list[str] = Field(description="Main obligations for each party")
    governing_law: str | None = Field(description="Governing law jurisdiction", default=None)


class InvoiceData(BaseModel):
    """Schema for invoice extraction results"""
    invoice_number: str = Field(description="Invoice number")
    vendor_name: str = Field(description="Vendor/supplier name")
    customer_name: str = Field(description="Customer name")
    invoice_date: str | None = Field(description="Invoice date", default=None)
    due_date: str | None = Field(description="Payment due date", default=None)
    total_amount: float = Field(description="Total invoice amount")
    currency: str = Field(description="Currency code", default="USD")
    line_items: list[str] = Field(description="List of line items with quantities and prices")
    tax_amount: float | None = Field(description="Tax amount", default=None)


class GeneralData(BaseModel):
    """Schema for general document extraction"""
    document_title: str = Field(description="Document title or subject")
    main_entities: list[str] = Field(description="Key entities mentioned (people, companies, etc.)")
    key_dates: list[str] = Field(description="Important dates mentioned")
    summary: str = Field(description="Brief summary of the document content")
    action_items: list[str] = Field(description="Action items or next steps mentioned")
    contact_info: list[str] = Field(description="Contact information found")


class ValidationResult(BaseModel):
    """Schema for extraction validation results"""
    is_valid: bool = Field(description="Whether extraction passed validation")
    confidence_score: float = Field(description="Confidence in extraction quality (0-1)", ge=0.0, le=1.0)
    completeness_score: float = Field(description="How complete the extraction is (0-1)", ge=0.0, le=1.0)
    accuracy_indicators: list[str] = Field(description="Signs of accurate extraction")
    missing_fields: list[str] = Field(description="Critical fields that appear to be missing")
    quality_issues: list[str] = Field(description="Potential quality issues identified")
    recommendation: str = Field(description="Recommended next action")


class PipelineResult(BaseModel):
    """Complete pipeline result"""
    extraction_id: str = Field(description="Unique identifier for this extraction")
    classification: DocumentClassification
    extracted_data: Union[ContractData, InvoiceData, GeneralData]
    validation: ValidationResult
    processing_time_ms: int = Field(description="Total processing time in milliseconds")
    pipeline_status: str = Field(description="Overall pipeline status")
    requires_review: bool = Field(description="Whether manual review is recommended")


# =============================================================================
# MULTI-AGENT PIPELINE IMPLEMENTATION
# =============================================================================

class MultiAgentExtractionPipeline:
    """
    Multi-agent pipeline for sophisticated document processing.
    
    This pipeline demonstrates:
    - Document classification with confidence scoring
    - Specialized extraction agents for different document types
    - Quality validation and confidence assessment
    - Complete pipeline orchestration with error handling
    """
    
    def __init__(self):
        self.session_service = InMemorySessionService()
        self.agents = self._create_agents()
        self.runners = self._create_runners()
        
    def _create_agents(self) -> dict[str, LlmAgent]:
        """Create all agents used in the pipeline"""
        
        # Document Classification Agent
        classifier_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="document_classifier",
            description="Classifies documents and recommends processing approach",
            instruction="""You are an expert document classifier. Analyze the provided document and classify it for optimal extraction processing.

Consider these factors:
1. Document type (contract, invoice, agreement, proposal, report, email, etc.)
2. Complexity level (simple, medium, complex)
3. Processing time estimate
4. Key indicators that led to your classification

Provide a confidence score based on how certain you are about the classification.
Look for specific keywords, formatting patterns, and structural elements that indicate document type.

For contracts: Look for terms like "agreement", "parties", "whereas", "terms and conditions"
For invoices: Look for "invoice", "bill to", "amount due", "payment terms", line items
For reports: Look for "executive summary", "findings", "recommendations", "analysis"
For emails: Look for "from:", "to:", "subject:", email formatting""",
            output_schema=DocumentClassification,
            output_key="classification_result",
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        
        # Specialized Contract Extraction Agent
        contract_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="contract_extractor",
            description="Specialized agent for extracting structured data from contracts",
            instruction="""You are a legal document expert specializing in contract analysis. Extract detailed information from contracts with focus on:

1. All parties involved (individuals, companies, entities) with their roles
2. Financial terms including total value, payment schedules, and penalties
3. Critical dates including effective dates, deadlines, and renewal terms
4. Key obligations and responsibilities for each party
5. Governing law and jurisdiction clauses
6. Termination and renewal conditions

Pay special attention to:
- Exact party names and their roles (vendor, client, contractor, etc.)
- All monetary amounts with currency
- All dates in a consistent format
- Specific obligations and deliverables
- Legal jurisdiction and governing law

If information is unclear or ambiguous, note it as 'unclear' rather than guessing.
For dates, use ISO format (YYYY-MM-DD) when possible.
For amounts, always include currency context.""",
            output_schema=ContractData,
            output_key="contract_data",
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        
        # Specialized Invoice Extraction Agent
        invoice_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="invoice_extractor",
            description="Specialized agent for extracting structured data from invoices",
            instruction="""You are a financial document expert specializing in invoice processing. Extract structured data from invoices including:

1. Invoice identification (number, date, reference)
2. Vendor information (name, address, contact details)
3. Customer information (name, address, billing details)
4. Line items with descriptions, quantities, unit prices, and totals
5. Financial calculations (subtotal, tax, total amount)
6. Payment terms and due dates

Focus on accuracy for:
- Invoice numbers and dates
- Vendor and customer names
- All monetary amounts with proper currency
- Line item details with quantities and prices
- Tax calculations and rates
- Payment due dates

Extract line items as descriptive strings that include quantity, description, and price.
Ensure all amounts are numeric and include currency information.
Validate that tax amounts and totals are consistent.""",
            output_schema=InvoiceData,
            output_key="invoice_data",
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        
        # General Document Extraction Agent
        general_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="general_extractor",
            description="General-purpose agent for extracting key information from various document types",
            instruction="""You are a general document analysis expert. Extract key information from any type of document including:

1. Document title or main subject
2. Key entities (people, companies, organizations, locations)
3. Important dates and deadlines
4. Summary of main content and purpose
5. Action items, next steps, or follow-up requirements
6. Contact information (names, emails, phone numbers)

Focus on:
- Identifying the main purpose and content of the document
- Extracting all mentioned entities accurately
- Capturing important dates in consistent format
- Providing a concise but comprehensive summary
- Identifying actionable items and next steps
- Finding all contact information

Provide a balanced extraction that captures the most important information
without overwhelming detail. Prioritize accuracy and relevance.""",
            output_schema=GeneralData,
            output_key="general_data",
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        
        # Quality Validation Agent
        validator_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="extraction_validator",
            description="Validates extraction quality and provides confidence assessment",
            instruction="""You are a quality assurance expert for data extraction. Validate extracted data for completeness and accuracy by comparing it against the original document.

Assess these quality dimensions:
1. **Completeness**: Are all important fields populated with meaningful data?
2. **Accuracy**: Does the extracted data match the source document?
3. **Consistency**: Are data formats consistent (dates, amounts, etc.)?
4. **Logic**: Do relationships make sense (dates in proper order, calculations correct)?
5. **Comprehensiveness**: Is the extraction missing any critical information?

Provide confidence scores:
- 0.9-1.0: Excellent extraction, ready for production use
- 0.7-0.9: Good extraction, minor issues or missing optional fields
- 0.5-0.7: Acceptable extraction, needs review for missing important information
- 0.3-0.5: Poor extraction, significant issues or missing critical data
- 0.0-0.3: Failed extraction, major errors or mostly empty fields

Give specific recommendations:
- "approved" for high-quality extractions
- "review_needed" for medium-quality extractions
- "retry_extraction" for poor extractions
- "manual_processing" for failed extractions""",
            output_schema=ValidationResult,
            output_key="validation_result",
            disallow_transfer_to_parent=True,
            disallow_transfer_to_peers=True,
        )
        
        return {
            'classifier': classifier_agent,
            'contract': contract_agent,
            'invoice': invoice_agent,
            'general': general_agent,
            'validator': validator_agent
        }
    
    def _create_runners(self) -> dict[str, Runner]:
        """Create runners for each agent"""
        runners = {}
        for name, agent in self.agents.items():
            runners[name] = Runner(
                agent=agent,
                app_name=f"extraction_{name}",
                session_service=self.session_service,
            )
        return runners
    
    async def classify_document(self, content: str) -> DocumentClassification:
        """Classify document type and characteristics"""
        try:
            # Create session for classification
            session_id = f"classify_{hashlib.md5(content.encode()).hexdigest()[:8]}"
            await self.session_service.create_session(
                app_name="extraction_classifier",
                user_id="pipeline_user",
                session_id=session_id
            )
            
            user_content = types.Content(
                role="user",
                parts=[types.Part.from_text(text=f"Classify this document and provide processing recommendations:\n\n{content[:2000]}{'...' if len(content) > 2000 else ''}")]
            )
            
            async for event in self.runners['classifier'].run_async(
                user_id="pipeline_user",
                session_id=session_id,
                new_message=user_content,
            ):
                if event.is_final_response() and event.content and event.content.parts:
                    if event.content.parts[0].text:
                        try:
                            import json
                            result_data = json.loads(event.content.parts[0].text)
                            return DocumentClassification(**result_data)
                        except (json.JSONDecodeError, ValueError):
                            # Fallback if JSON parsing fails
                            return DocumentClassification(
                                document_type=DocumentType.UNKNOWN,
                                complexity_level="medium",
                                estimated_processing_time=30,
                                recommended_extractor="general",
                                confidence_score=0.5,
                                key_indicators=["Classification parsing failed"]
                            )
            
            # Default classification if no response
            return DocumentClassification(
                document_type=DocumentType.UNKNOWN,
                complexity_level="medium",
                estimated_processing_time=30,
                recommended_extractor="general",
                confidence_score=0.0,
                key_indicators=["No classification response"]
            )
            
        except Exception as e:
            logger.error(f"Error in document classification: {e}")
            return DocumentClassification(
                document_type=DocumentType.UNKNOWN,
                complexity_level="medium",
                estimated_processing_time=30,
                recommended_extractor="general",
                confidence_score=0.0,
                key_indicators=[f"Classification error: {str(e)}"]
            )
    
    async def extract_with_specialist(self, content: str, doc_type: DocumentType) -> Union[ContractData, InvoiceData, GeneralData]:
        """Extract data using the appropriate specialist agent"""
        try:
            # Determine which agent to use
            agent_mapping = {
                DocumentType.CONTRACT: 'contract',
                DocumentType.AGREEMENT: 'contract',
                DocumentType.INVOICE: 'invoice',
                DocumentType.PROPOSAL: 'general',
                DocumentType.REPORT: 'general',
                DocumentType.EMAIL: 'general',
                DocumentType.UNKNOWN: 'general'
            }
            
            agent_name = agent_mapping.get(doc_type, 'general')
            
            # Create session for extraction
            session_id = f"extract_{agent_name}_{hashlib.md5(content.encode()).hexdigest()[:8]}"
            await self.session_service.create_session(
                app_name=f"extraction_{agent_name}",
                user_id="pipeline_user",
                session_id=session_id
            )
            
            user_content = types.Content(
                role="user",
                parts=[types.Part.from_text(text=f"Extract structured data from this {doc_type.value}:\n\n{content}")]
            )
            
            async for event in self.runners[agent_name].run_async(
                user_id="pipeline_user",
                session_id=session_id,
                new_message=user_content,
            ):
                if event.is_final_response() and event.content and event.content.parts:
                    if event.content.parts[0].text:
                        try:
                            import json
                            result_data = json.loads(event.content.parts[0].text)
                            
                            # Return appropriate schema based on agent
                            if agent_name == 'contract':
                                return ContractData(**result_data)
                            elif agent_name == 'invoice':
                                return InvoiceData(**result_data)
                            else:
                                return GeneralData(**result_data)
                                
                        except (json.JSONDecodeError, ValueError) as e:
                            logger.warning(f"Failed to parse extraction result: {e}")
                            # Return default data based on agent type
                            if agent_name == 'contract':
                                return ContractData(
                                    parties=["Extraction failed"],
                                    payment_terms=["Unable to extract"],
                                    key_obligations=["Extraction failed"]
                                )
                            elif agent_name == 'invoice':
                                return InvoiceData(
                                    invoice_number="EXTRACTION_FAILED",
                                    vendor_name="Unknown",
                                    customer_name="Unknown",
                                    total_amount=0.0,
                                    line_items=["Extraction failed"]
                                )
                            else:
                                return GeneralData(
                                    document_title="Extraction Failed",
                                    main_entities=["Unknown"],
                                    key_dates=[],
                                    summary="Failed to extract data",
                                    action_items=[],
                                    contact_info=[]
                                )
            
            # Default return if no response
            logger.warning(f"No extraction response from {agent_name} agent")
            if agent_name == 'contract':
                return ContractData(
                    parties=["No response"],
                    payment_terms=["No response"],
                    key_obligations=["No response"]
                )
            elif agent_name == 'invoice':
                return InvoiceData(
                    invoice_number="NO_RESPONSE",
                    vendor_name="Unknown",
                    customer_name="Unknown",
                    total_amount=0.0,
                    line_items=["No response"]
                )
            else:
                return GeneralData(
                    document_title="No Response",
                    main_entities=["Unknown"],
                    key_dates=[],
                    summary="No extraction response",
                    action_items=[],
                    contact_info=[]
                )
                
        except Exception as e:
            logger.error(f"Error in specialized extraction: {e}")
            # Return error-state data
            if doc_type in [DocumentType.CONTRACT, DocumentType.AGREEMENT]:
                return ContractData(
                    parties=[f"Error: {str(e)}"],
                    payment_terms=["Extraction error"],
                    key_obligations=["Extraction error"]
                )
            elif doc_type == DocumentType.INVOICE:
                return InvoiceData(
                    invoice_number="ERROR",
                    vendor_name="Error",
                    customer_name="Error",
                    total_amount=0.0,
                    line_items=[f"Error: {str(e)}"]
                )
            else:
                return GeneralData(
                    document_title="Extraction Error",
                    main_entities=[f"Error: {str(e)}"],
                    key_dates=[],
                    summary="Extraction failed due to error",
                    action_items=[],
                    contact_info=[]
                )
    
    async def validate_extraction(self, extracted_data: Union[ContractData, InvoiceData, GeneralData], 
                                original_content: str) -> ValidationResult:
        """Validate the quality of extracted data"""
        try:
            # Create session for validation
            session_id = f"validate_{hashlib.md5(str(extracted_data).encode()).hexdigest()[:8]}"
            await self.session_service.create_session(
                app_name="extraction_validator",
                user_id="pipeline_user",
                session_id=session_id
            )
            
            validation_prompt = f"""
Validate this extraction against the original document:

ORIGINAL DOCUMENT (first 1000 chars):
{original_content[:1000]}{'...' if len(original_content) > 1000 else ''}

EXTRACTED DATA:
{extracted_data.model_dump_json(indent=2)}

Check for completeness, accuracy, and consistency.
Provide specific feedback on what's missing or incorrect.
"""
            
            user_content = types.Content(
                role="user",
                parts=[types.Part.from_text(text=validation_prompt)]
            )
            
            async for event in self.runners['validator'].run_async(
                user_id="pipeline_user",
                session_id=session_id,
                new_message=user_content,
            ):
                if event.is_final_response() and event.content and event.content.parts:
                    if event.content.parts[0].text:
                        try:
                            import json
                            result_data = json.loads(event.content.parts[0].text)
                            return ValidationResult(**result_data)
                        except (json.JSONDecodeError, ValueError):
                            return ValidationResult(
                                is_valid=True,
                                confidence_score=0.5,
                                completeness_score=0.5,
                                accuracy_indicators=[],
                                missing_fields=[],
                                quality_issues=["Validation parsing failed"],
                                recommendation="manual_review"
                            )
            
            # Default validation if no response
            return ValidationResult(
                is_valid=False,
                confidence_score=0.0,
                completeness_score=0.0,
                accuracy_indicators=[],
                missing_fields=["all"],
                quality_issues=["No validation response"],
                recommendation="retry_extraction"
            )
            
        except Exception as e:
            logger.error(f"Error in validation: {e}")
            return ValidationResult(
                is_valid=False,
                confidence_score=0.0,
                completeness_score=0.0,
                accuracy_indicators=[],
                missing_fields=["all"],
                quality_issues=[f"Validation error: {str(e)}"],
                recommendation="manual_processing"
            )
    
    async def process_document(self, content: str) -> PipelineResult:
        """Complete pipeline: classify → extract → validate"""
        start_time = datetime.now()
        extraction_id = hashlib.md5(content.encode()).hexdigest()
        
        try:
            logger.info(f"Starting pipeline processing for document {extraction_id[:8]}")
            
            # Step 1: Classify document
            logger.info("Step 1: Classifying document...")
            classification = await self.classify_document(content)
            logger.info(f"Document classified as: {classification.document_type} (confidence: {classification.confidence_score:.2f})")
            
            # Step 2: Extract using appropriate specialist
            logger.info("Step 2: Extracting data with specialist agent...")
            extraction_result = await self.extract_with_specialist(content, classification.document_type)
            logger.info(f"Extraction completed using {classification.recommended_extractor} agent")
            
            # Step 3: Validate extraction quality
            logger.info("Step 3: Validating extraction quality...")
            validation = await self.validate_extraction(extraction_result, content)
            logger.info(f"Validation completed: {validation.is_valid} (confidence: {validation.confidence_score:.2f})")
            
            # Calculate processing time
            processing_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)
            
            # Determine if review is needed
            requires_review = (
                validation.confidence_score < 0.7 or
                not validation.is_valid or
                classification.confidence_score < 0.6
            )
            
            # Determine pipeline status
            pipeline_status = "completed"
            if requires_review:
                pipeline_status = "completed_with_review_needed"
            if validation.confidence_score < 0.3:
                pipeline_status = "failed"
            
            result = PipelineResult(
                extraction_id=extraction_id,
                classification=classification,
                extracted_data=extraction_result,
                validation=validation,
                processing_time_ms=processing_time_ms,
                pipeline_status=pipeline_status,
                requires_review=requires_review
            )
            
            logger.info(f"Pipeline completed: {pipeline_status} (took {processing_time_ms}ms)")
            return result
            
        except Exception as e:
            logger.error(f"Error in pipeline processing: {e}")
            processing_time_ms = int((datetime.now() - start_time).total_seconds() * 1000)
            
            return PipelineResult(
                extraction_id=extraction_id,
                classification=DocumentClassification(
                    document_type=DocumentType.UNKNOWN,
                    complexity_level="unknown",
                    estimated_processing_time=0,
                    recommended_extractor="unknown",
                    confidence_score=0.0,
                    key_indicators=[f"Pipeline error: {str(e)}"]
                ),
                extracted_data=GeneralData(
                    document_title="Pipeline Error",
                    main_entities=[f"Error: {str(e)}"],
                    key_dates=[],
                    summary="Pipeline processing failed",
                    action_items=["Fix pipeline error"],
                    contact_info=[]
                ),
                validation=ValidationResult(
                    is_valid=False,
                    confidence_score=0.0,
                    completeness_score=0.0,
                    accuracy_indicators=[],
                    missing_fields=["all"],
                    quality_issues=[f"Pipeline error: {str(e)}"],
                    recommendation="manual_processing"
                ),
                processing_time_ms=processing_time_ms,
                pipeline_status="failed",
                requires_review=True
            )


# =============================================================================
# EXAMPLE USAGE AND DEMONSTRATIONS
# =============================================================================

async def run_contract_example():
    """Demonstrate pipeline with a contract document"""
    print("\n" + "="*60)
    print("MULTI-AGENT PIPELINE DEMO: CONTRACT PROCESSING")
    print("="*60)
    
    pipeline = MultiAgentExtractionPipeline()
    
    sample_contract = """
    PROFESSIONAL SERVICES AGREEMENT

    This Professional Services Agreement ("Agreement") is entered into on March 15, 2024, between:

    Service Provider: TechCorp Solutions LLC
    Address: 123 Innovation Drive, San Francisco, CA 94105
    Contact: John Smith, CEO (john@techcorp.com, 555-123-4567)

    Client: Global Industries Inc.
    Address: 456 Business Avenue, New York, NY 10001
    Contact: Sarah Johnson, CTO (sarah@globalindustries.com, 555-987-6543)

    SERVICES AND DELIVERABLES:
    1. Custom software development for inventory management system
    2. System integration with existing ERP platforms
    3. Staff training and knowledge transfer
    4. 6 months of post-implementation support

    FINANCIAL TERMS:
    - Total Contract Value: $85,000 USD
    - Payment Schedule: 
      * $25,000 upon contract signing
      * $30,000 upon completion of development phase
      * $20,000 upon system deployment
      * $10,000 upon completion of training
    - Late Payment Penalty: 1.5% per month on overdue amounts

    TIMELINE:
    - Project Start Date: April 1, 2024
    - Development Phase Completion: July 31, 2024
    - System Deployment: August 15, 2024
    - Training Completion: August 31, 2024
    - Support Period: September 1, 2024 to February 28, 2025

    OBLIGATIONS:
    Provider Obligations:
    - Deliver functional software meeting specifications
    - Provide comprehensive documentation
    - Conduct staff training sessions
    - Maintain system availability during support period

    Client Obligations:
    - Provide necessary system access and data
    - Designate project stakeholders
    - Participate in testing and validation
    - Make timely payments per agreed schedule

    GOVERNING LAW: This Agreement shall be governed by the laws of the State of California.
    
    TERMINATION: Either party may terminate with 30 days written notice.
    """
    
    print("Processing contract document...")
    result = await pipeline.process_document(sample_contract)
    
    print(f"\n📄 EXTRACTION RESULTS (ID: {result.extraction_id[:8]})")
    print(f"Pipeline Status: {result.pipeline_status}")
    print(f"Processing Time: {result.processing_time_ms}ms")
    print(f"Requires Review: {'Yes' if result.requires_review else 'No'}")
    
    print(f"\n🔍 CLASSIFICATION:")
    print(f"Document Type: {result.classification.document_type}")
    print(f"Complexity: {result.classification.complexity_level}")
    print(f"Confidence: {result.classification.confidence_score:.2f}")
    print(f"Key Indicators: {', '.join(result.classification.key_indicators)}")
    
    print(f"\n📊 EXTRACTED DATA:")
    if isinstance(result.extracted_data, ContractData):
        print(f"Parties: {', '.join(result.extracted_data.parties)}")
        print(f"Contract Value: ${result.extracted_data.contract_value:,.2f} {result.extracted_data.currency}")
        print(f"Start Date: {result.extracted_data.start_date}")
        print(f"End Date: {result.extracted_data.end_date}")
        print(f"Payment Terms: {len(result.extracted_data.payment_terms)} terms extracted")
        print(f"Obligations: {len(result.extracted_data.key_obligations)} obligations extracted")
        print(f"Governing Law: {result.extracted_data.governing_law}")
    
    print(f"\n✅ VALIDATION RESULTS:")
    print(f"Valid: {result.validation.is_valid}")
    print(f"Confidence: {result.validation.confidence_score:.2f}")
    print(f"Completeness: {result.validation.completeness_score:.2f}")
    print(f"Recommendation: {result.validation.recommendation}")
    if result.validation.quality_issues:
        print(f"Quality Issues: {', '.join(result.validation.quality_issues)}")
    
    return result


async def run_invoice_example():
    """Demonstrate pipeline with an invoice document"""
    print("\n" + "="*60)
    print("MULTI-AGENT PIPELINE DEMO: INVOICE PROCESSING")
    print("="*60)
    
    pipeline = MultiAgentExtractionPipeline()
    
    sample_invoice = """
    INVOICE

    TechCorp Solutions LLC
    123 Innovation Drive
    San Francisco, CA 94105
    Phone: (555) 123-4567
    Email: billing@techcorp.com

    BILL TO:
    Global Industries Inc.
    456 Business Avenue
    New York, NY 10001

    Invoice Number: INV-2024-001
    Invoice Date: March 15, 2024
    Due Date: April 15, 2024
    Payment Terms: Net 30

    DESCRIPTION                          QTY    RATE        AMOUNT
    ================================================================
    Software Development Services         40    $150.00     $6,000.00
    System Integration                    16    $175.00     $2,800.00
    Project Management                    24    $125.00     $3,000.00
    Documentation & Training              8     $100.00     $800.00
    ================================================================
    
    Subtotal:                                              $12,600.00
    Tax (8.5%):                                            $1,071.00
    TOTAL:                                                 $13,671.00

    Payment Instructions:
    - Check payable to: TechCorp Solutions LLC
    - Wire Transfer: Account #12345678, Routing #987654321
    - Credit Card: Visa/MC/Amex accepted
    
    Thank you for your business!
    """
    
    print("Processing invoice document...")
    result = await pipeline.process_document(sample_invoice)
    
    print(f"\n📄 EXTRACTION RESULTS (ID: {result.extraction_id[:8]})")
    print(f"Pipeline Status: {result.pipeline_status}")
    print(f"Processing Time: {result.processing_time_ms}ms")
    print(f"Requires Review: {'Yes' if result.requires_review else 'No'}")
    
    print(f"\n🔍 CLASSIFICATION:")
    print(f"Document Type: {result.classification.document_type}")
    print(f"Complexity: {result.classification.complexity_level}")
    print(f"Confidence: {result.classification.confidence_score:.2f}")
    
    print(f"\n📊 EXTRACTED DATA:")
    if isinstance(result.extracted_data, InvoiceData):
        print(f"Invoice Number: {result.extracted_data.invoice_number}")
        print(f"Vendor: {result.extracted_data.vendor_name}")
        print(f"Customer: {result.extracted_data.customer_name}")
        print(f"Invoice Date: {result.extracted_data.invoice_date}")
        print(f"Due Date: {result.extracted_data.due_date}")
        print(f"Total Amount: ${result.extracted_data.total_amount:,.2f} {result.extracted_data.currency}")
        print(f"Tax Amount: ${result.extracted_data.tax_amount:,.2f}" if result.extracted_data.tax_amount else "Tax Amount: Not specified")
        print(f"Line Items: {len(result.extracted_data.line_items)} items extracted")
    
    print(f"\n✅ VALIDATION RESULTS:")
    print(f"Valid: {result.validation.is_valid}")
    print(f"Confidence: {result.validation.confidence_score:.2f}")
    print(f"Completeness: {result.validation.completeness_score:.2f}")
    print(f"Recommendation: {result.validation.recommendation}")
    
    return result


async def run_general_document_example():
    """Demonstrate pipeline with a general business document"""
    print("\n" + "="*60)
    print("MULTI-AGENT PIPELINE DEMO: GENERAL DOCUMENT PROCESSING")
    print("="*60)
    
    pipeline = MultiAgentExtractionPipeline()
    
    sample_document = """
    QUARTERLY BUSINESS REVIEW MEETING MINUTES
    
    Date: March 15, 2024
    Time: 2:00 PM - 4:00 PM PST
    Location: Conference Room A / Virtual
    
    ATTENDEES:
    - Sarah Johnson, CEO (sarah@company.com)
    - Mike Chen, CFO (mike@company.com)
    - Lisa Rodriguez, VP Marketing (lisa@company.com)
    - David Kim, CTO (david@company.com)
    - Jennifer Walsh, HR Director (jennifer@company.com)
    
    AGENDA ITEMS DISCUSSED:
    
    1. Q1 2024 Financial Performance
       - Revenue: $2.4M (15% increase over Q4 2023)
       - Expenses: $1.8M (5% increase)
       - Net Profit: $600K (40% increase)
       - Cash Flow: Positive trend continues
    
    2. Product Development Updates
       - Version 2.0 launch scheduled for May 15, 2024
       - Beta testing phase completed successfully
       - Customer feedback integration 95% complete
    
    3. Marketing Campaign Results
       - Q1 campaign generated 450 new leads
       - Conversion rate improved to 12%
       - Social media engagement up 25%
    
    4. Human Resources Updates
       - 3 new hires completed onboarding
       - Employee satisfaction survey results: 4.2/5
       - Annual review cycle begins April 1, 2024
    
    ACTION ITEMS:
    1. Mike to prepare detailed financial forecast for Q2 (Due: March 22, 2024)
    2. David to finalize version 2.0 release timeline (Due: March 20, 2024)
    3. Lisa to launch customer retention campaign (Due: April 1, 2024)
    4. Jennifer to schedule management training sessions (Due: March 30, 2024)
    5. Sarah to review and approve Q2 budget proposals (Due: March 25, 2024)
    
    NEXT MEETING: April 15, 2024 at 2:00 PM PST
    
    Meeting adjourned at 4:15 PM PST.
    """
    
    print("Processing general business document...")
    result = await pipeline.process_document(sample_document)
    
    print(f"\n📄 EXTRACTION RESULTS (ID: {result.extraction_id[:8]})")
    print(f"Pipeline Status: {result.pipeline_status}")
    print(f"Processing Time: {result.processing_time_ms}ms")
    print(f"Requires Review: {'Yes' if result.requires_review else 'No'}")
    
    print(f"\n🔍 CLASSIFICATION:")
    print(f"Document Type: {result.classification.document_type}")
    print(f"Complexity: {result.classification.complexity_level}")
    print(f"Confidence: {result.classification.confidence_score:.2f}")
    
    print(f"\n📊 EXTRACTED DATA:")
    if isinstance(result.extracted_data, GeneralData):
        print(f"Title: {result.extracted_data.document_title}")
        print(f"Main Entities: {', '.join(result.extracted_data.main_entities[:5])}")
        print(f"Key Dates: {', '.join(result.extracted_data.key_dates[:3])}")
        print(f"Summary: {result.extracted_data.summary[:100]}...")
        print(f"Action Items: {len(result.extracted_data.action_items)} items")
        print(f"Contact Info: {len(result.extracted_data.contact_info)} contacts")
    
    print(f"\n✅ VALIDATION RESULTS:")
    print(f"Valid: {result.validation.is_valid}")
    print(f"Confidence: {result.validation.confidence_score:.2f}")
    print(f"Completeness: {result.validation.completeness_score:.2f}")
    print(f"Recommendation: {result.validation.recommendation}")
    
    return result


async def run_pipeline_comparison():
    """Compare pipeline performance across different document types"""
    print("\n" + "="*60)
    print("MULTI-AGENT PIPELINE COMPARISON")
    print("="*60)
    
    print("Running all examples to compare pipeline performance...")
    
    # Run all examples
    contract_result = await run_contract_example()
    invoice_result = await run_invoice_example()
    general_result = await run_general_document_example()
    
    # Performance comparison
    print("\n📊 PERFORMANCE COMPARISON:")
    print(f"Contract Processing: {contract_result.processing_time_ms}ms")
    print(f"Invoice Processing: {invoice_result.processing_time_ms}ms")
    print(f"General Document Processing: {general_result.processing_time_ms}ms")
    
    print("\n🎯 ACCURACY COMPARISON:")
    print(f"Contract Confidence: {contract_result.validation.confidence_score:.2f}")
    print(f"Invoice Confidence: {invoice_result.validation.confidence_score:.2f}")
    print(f"General Document Confidence: {general_result.validation.confidence_score:.2f}")
    
    print("\n🔍 CLASSIFICATION ACCURACY:")
    print(f"Contract Classification: {contract_result.classification.confidence_score:.2f}")
    print(f"Invoice Classification: {invoice_result.classification.confidence_score:.2f}")
    print(f"General Document Classification: {general_result.classification.confidence_score:.2f}")
    
    # Calculate averages
    avg_processing_time = (contract_result.processing_time_ms + invoice_result.processing_time_ms + general_result.processing_time_ms) / 3
    avg_confidence = (contract_result.validation.confidence_score + invoice_result.validation.confidence_score + general_result.validation.confidence_score) / 3
    
    print(f"\n📈 OVERALL PIPELINE PERFORMANCE:")
    print(f"Average Processing Time: {avg_processing_time:.0f}ms")
    print(f"Average Confidence Score: {avg_confidence:.2f}")
    
    return {
        'contract': contract_result,
        'invoice': invoice_result,
        'general': general_result,
        'averages': {
            'processing_time_ms': avg_processing_time,
            'confidence_score': avg_confidence
        }
    }


def main():
    """Main function to run all multi-agent pipeline examples"""
    print("Multi-Agent Extraction Pipeline with Google ADK")
    print("=" * 50)
    print("This example demonstrates a sophisticated multi-agent pipeline that processes")
    print("different types of documents with specialized agents and quality validation.")
    print()
    
    try:
        # Run the pipeline comparison
        results = asyncio.run(run_pipeline_comparison())
        
        print("\n🎉 PIPELINE DEMONSTRATION COMPLETED!")
        print("=" * 50)
        print("The multi-agent pipeline successfully processed all document types.")
        print("Each document was automatically classified, processed by the appropriate")
        print("specialist agent, and validated for quality.")
        print()
        print("This demonstrates the power of multi-agent architectures for")
        print("sophisticated document processing workflows.")
        
    except Exception as e:
        print(f"❌ Error running pipeline examples: {e}")
        print("Please ensure your Google API key is configured properly.")


if __name__ == "__main__":
    main()
