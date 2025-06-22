# Structured Data Extraction with Google ADK GenAI for the Impatient: From Novice to Practitioner in Record Time

## Prerequisites and Setup

Before diving into structured data extraction, ensure you have the proper environment set up:

### Installation Requirements

```bash
# Install Google ADK and dependencies
pip install google-generativeai google-adk pydantic asyncio

# For additional document processing (optional)
pip install PyMuPDF python-docx pandas openpyxl
```

### API Key Configuration

1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Set your environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or in Python:

```python
import os
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

### Quick Test

```python
from google.adk.agents import LlmAgent
from google.adk.runtime import Runner
from google.adk.sessions import InMemorySessionService

# Test your setup with a simple agent
test_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="test_agent", 
    instruction="You are a helpful assistant."
)

print("✅ ADK setup successful!")
```

---

## Why: The Data Extraction Crisis That's Costing You Millions

Picture this: Sarah, a data analyst at a Fortune 500 company, spent three weeks manually extracting customer feedback from 10,000 emails . By the time she finished, the insights were outdated, and her company lost a major client. Sound familiar?

**Here's the brutal truth**: 80% of enterprise data is unstructured, and traditional extraction methods are like trying to drink from a fire hose with a teaspoon . While your competitors are drowning in data chaos, Google's Agent Development Kit (ADK) offers a lifeline that transforms this challenge into a competitive advantage .

```mermaid
flowchart TD
    A[Unstructured Data] -->|Traditional Methods| B[Manual Processing]
    A -->|ADK GenAI| C[Automated Extraction]
    B --> D[Weeks of Work]
    C --> E[Minutes to Complete]
    D --> F[Outdated Insights]
    E --> G[Real-time Intelligence]
    style A fill:#e8f5e8
    style C fill:#e8f5e8
    style E fill:#e8f5e8
    style G fill:#e8f5e8
```

Modern businesses face an unprecedented data deluge where critical information is locked away in emails, documents, PDFs, and web content . The cost of manual extraction isn't just measured in time—it's measured in missed opportunities, delayed decisions, and competitive disadvantage . Companies that master structured data extraction gain the ability to react faster, make better decisions, and automate processes that previously required armies of analysts .

### The Hidden Costs of Data Chaos

Most organizations don't realize the true cost of their data extraction inefficiencies . Consider these scenarios:

- **Customer Service**: Agents manually scan through knowledge bases, taking 5-10 minutes per query when AI could extract relevant information in seconds 
- **Legal Discovery**: Law firms spend millions on document review when structured extraction could identify key clauses, dates, and parties automatically 
- **Financial Analysis**: Investment firms lose competitive edge when research teams spend days extracting data from reports instead of analyzing insights 
- **Healthcare**: Medical professionals waste valuable time extracting patient information from unstructured notes instead of focusing on care 

The opportunity cost is staggering—while your team extracts data manually, competitors using automated solutions are already acting on insights .

## What: Your Secret Weapon for Data Domination

Google ADK isn't just another tool—it's like having a team of expert data scientists working 24/7 . The framework uses three powerful mechanisms for structured extraction that revolutionize how you handle unstructured data .

### Core Extraction Mechanisms

The ADK provides sophisticated capabilities that go far beyond simple text processing . At its heart, the system leverages Large Language Models (LLMs) combined with structured schemas to ensure consistent, reliable data extraction .

**Output Schema**: This defines exactly what structure you want your extracted data to follow, using Pydantic models for type safety and validation . Think of it as a blueprint that tells the AI exactly how to organize the extracted information.

**Input Schema**: This validates the format of incoming data, ensuring your extraction pipeline only processes properly formatted inputs . It acts as a quality gate that prevents malformed data from entering your system.

**Output Key**: This stores results for multi-agent workflows, allowing different extraction agents to access and build upon each other's work . It's essential for complex extraction pipelines where multiple specialized agents work together.

Think of ADK as a sophisticated assembly line where each agent specializes in specific extraction tasks, passing perfectly formatted data to the next stage . The framework's event-driven architecture ensures that every step of the extraction process is tracked, logged, and can be audited .

### Architecture That Scales

Unlike traditional extraction tools that break down under complex scenarios, ADK's multi-agent architecture allows you to build extraction systems that grow with your needs . You can start with simple single-agent extraction and gradually build complex pipelines with specialized agents for different document types, data formats, and extraction requirements .

The framework's context management system ensures that extraction agents maintain state across complex operations . This means an agent can remember previous extractions, reference earlier findings, and build cumulative knowledge throughout a session .

**🔍 Pause and Reflect**: What unstructured data in your organization could benefit from automated extraction right now?

## How: From Zero to Extraction Hero in 6 Comprehensive Examples

### Example 1: Basic Contact Extraction (Beginner Level)

Let's start with the foundation—extracting contact information from business emails. This example demonstrates the core concepts that you'll use in every ADK extraction project .

```python
from google.adk.agents import LlmAgent
from google.adk.runtime import Runner
from google.adk.sessions import InMemorySessionService
from pydantic import BaseModel, Field
from google.genai import types

class ContactInfo(BaseModel):
    name: str = Field(description="Full name of the contact")
    email: str = Field(description="Email address")
    company: str = Field(description="Company name")
    phone: str = Field(description="Phone number if available", default="")
    position: str = Field(description="Job title or position", default="")

contact_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="contact_extractor",
    description="Extracts contact information from text",
    instruction="""Extract contact information from the provided text. 
    Focus on accuracy and completeness. If information is unclear or missing, 
    leave those fields empty rather than guessing.""",
    output_schema=ContactInfo,
    output_key="extracted_contacts"
)

# Set up the extraction pipeline
session_service = InMemorySessionService()
runner = Runner(
    agent=contact_extractor,
    app_name="contact_extraction_app",
    session_service=session_service
)

# Example usage
async def extract_contacts(text_content):
    user_content = types.Content(role='user', parts=[types.Part(text=text_content)])
    
    async for event in runner.run_async(
        user_id="user_001", 
        session_id="session_001", 
        new_message=user_content
    ):
        if event.is_final_response() and event.content and event.content.parts:
            if event.content.parts[0].text:
                return event.content.parts[0].text
            
    return None  # No valid response found
```

This basic extractor demonstrates several key ADK principles :

1. **Pydantic Schema Definition**: The `ContactInfo` class provides type safety and automatic validation
2. **Clear Instructions**: The agent knows exactly what to extract and how to handle uncertainty
3. **Output Key**: Results are stored for potential use by other agents
4. **Event-Driven Processing**: The extraction happens asynchronously with proper event handling

**Pro Tip**: Using Pydantic models ensures type safety and automatic validation—no more malformed JSON responses! The Field descriptions guide the AI in understanding exactly what data to extract .

### Example 2: Advanced Document Analysis (Intermediate Level)

Now let's tackle something more complex—extracting multiple data types from legal documents. This example shows how ADK handles sophisticated extraction scenarios with nested data structures.

```python
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
from google.adk.tools import FunctionTool

class DocumentType(str, Enum):
    CONTRACT = "contract"
    INVOICE = "invoice" 
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    LEGAL_BRIEF = "legal_brief"

class FinancialTerm(BaseModel):
    amount: float = Field(description="Monetary amount")
    currency: str = Field(description="Currency code (USD, EUR, etc.)", default="USD")
    description: str = Field(description="Description of what this amount represents")
    due_date: Optional[str] = Field(description="When payment is due", default=None)

class LegalExtraction(BaseModel):
    document_type: DocumentType
    parties: List[str] = Field(description="All parties involved in the document")
    key_dates: List[str] = Field(description="Important dates mentioned (contracts, deadlines, etc.)")
    financial_terms: List[FinancialTerm] = Field(description="All monetary amounts and terms")
    obligations: List[str] = Field(description="Key obligations and responsibilities listed")
    governing_law: str = Field(description="Jurisdiction or governing law", default="")
    effective_date: Optional[str] = Field(description="When the document becomes effective")
    expiration_date: Optional[str] = Field(description="When the document expires")

# Create document reader tool using ADK's FunctionTool
async def read_document_content(file_path: str, tool_context) -> Dict:
    """Reads document content from various file formats"""
    try:
        # Basic file reading - in production, you'd integrate with 
        # document processing libraries like PyMuPDF for PDFs
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": f"Failed to read document: {str(e)}"}

document_reader_tool = FunctionTool(
    name="document_reader",
    description="Read document content from file path",
    func=read_document_content
)

legal_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="legal_analyzer",
    description="Specialized agent for analyzing legal documents",
    instruction="""You are an expert legal document analyzer. Extract structured information 
    from legal documents with extreme precision. Pay special attention to:
    
    1. All parties mentioned (individuals, companies, entities)
    2. Financial terms including amounts, payment schedules, and penalties
    3. Critical dates including effective dates, deadlines, and renewal terms
    4. Legal obligations and responsibilities for each party
    5. Governing law and jurisdiction clauses
    
    If information is unclear or ambiguous, mark it as 'unclear' rather than guessing.
    For dates, use ISO format (YYYY-MM-DD) when possible.
    For amounts, include currency and context.""",
    output_schema=LegalExtraction,
    tools=[document_reader_tool]
)

# Example usage with proper event handling
async def analyze_legal_document(document_path: str):
    session_service = InMemorySessionService()
    runner = Runner(
        agent=legal_agent,
        app_name="legal_analysis_app",
        session_service=session_service
    )
    
    user_content = types.Content(
        role='user', 
        parts=[types.Part(text=f"Please analyze the legal document at: {document_path}")]
    )
    
    async for event in runner.run_async(
        user_id="legal_user", 
        session_id="legal_session", 
        new_message=user_content
    ):
        if hasattr(event, 'content') and event.content:
            if hasattr(event.content, 'parts') and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        return part.text
    
    return "No analysis result available"
```

This advanced example introduces several sophisticated concepts :

- **Nested Data Structures**: Financial terms are complex objects with multiple fields
- **Enums for Consistency**: Document types are limited to predefined values
- **Tool Integration**: The agent can read various document formats
- **Domain-Specific Instructions**: The prompt is tailored for legal document nuances


### Example 3: Multi-Agent Extraction Pipeline (Advanced Level)

For complex scenarios, you need multiple specialized agents working together. This example demonstrates how to build a sophisticated extraction pipeline with quality control .

```mermaid
sequenceDiagram
    participant User
    participant Classifier
    participant Extractor
    participant Validator
    participant Enricher
    participant Database
    
    User->>Classifier: Raw Document
    Classifier->>Extractor: Document Type + Routing Info
    Extractor->>Validator: Raw Extracted Data
    Validator->>Enricher: Validated Data
    Enricher->>Database: Final Structured Output
    Database->>User: Confirmation + Results
    
    Note over Classifier: Identifies document type and complexity
    Note over Extractor: Performs specialized extraction
    Note over Validator: Ensures data quality and completeness
    Note over Enricher: Adds context and derived fields
```

```python
from google.adk.agents import SequentialAgent, LlmAgent
from google.adk.tools import FunctionTool

# Classification schema
class DocumentClassification(BaseModel):
    document_type: str = Field(description="Primary document type")
    complexity_level: str = Field(description="simple, medium, complex")
    estimated_processing_time: int = Field(description="Estimated seconds to process")
    recommended_extractor: str = Field(description="Which specialized agent to use")
    confidence_score: float = Field(description="Confidence in classification (0-1)")

# Validation schema
class ExtractionValidation(BaseModel):
    is_valid: bool = Field(description="Whether extraction passed validation")
    completeness_score: float = Field(description="How complete the extraction is (0-1)")
    accuracy_indicators: List[str] = Field(description="Signs of accurate extraction")
    missing_fields: List[str] = Field(description="Critical fields that are missing")
    quality_warnings: List[str] = Field(description="Potential quality issues")

# Create specialized agents
classifier_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="document_classifier",
    instruction="""Analyze the document and classify it for optimal extraction processing.
    Consider document type, complexity, length, and quality to recommend the best 
    extraction approach.""",
    output_schema=DocumentClassification,
    output_key="classification_result"
)

# Specialized extractors for different document types
contract_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="contract_extractor",
    instruction="""Extract detailed information from contracts with focus on:
    - Party details and roles
    - Financial terms and payment schedules
    - Performance obligations
    - Termination clauses
    - Renewal terms""",
    output_schema=LegalExtraction,
    output_key="contract_data"
)

invoice_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="invoice_extractor",
    instruction="""Extract structured data from invoices including:
    - Vendor and customer information
    - Line items with quantities and prices
    - Tax calculations
    - Payment terms and due dates
    - Invoice numbering and references""",
    output_schema=LegalExtraction,  # Could be InvoiceExtraction for more specificity
    output_key="invoice_data"
)

### Example 3: Multi-Agent Coordination (Advanced Level)

Real-world extraction often requires coordinating multiple specialized agents. Here's how to build a robust multi-agent system using ADK's core components.

```python
from typing import List, Dict, Any
import asyncio
from enum import Enum

class DocumentType(str, Enum):
    CONTRACT = "contract"
    INVOICE = "invoice"
    RESUME = "resume"
    LEGAL_BRIEF = "legal_brief"
    UNKNOWN = "unknown"

class DocumentClassification(BaseModel):
    document_type: DocumentType
    confidence: float = Field(description="Classification confidence 0-1")
    key_indicators: List[str] = Field(description="Text patterns that led to classification")

class ExtractionValidation(BaseModel):
    is_valid: bool = Field(description="Whether extraction meets quality standards")
    confidence_score: float = Field(description="Overall confidence in extraction")
    missing_fields: List[str] = Field(description="Required fields that were not found")
    quality_issues: List[str] = Field(description="Specific quality concerns")
    recommendation: str = Field(description="Recommended next action")

# Document classifier agent
classifier_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="document_classifier",
    description="Classifies incoming documents for proper routing",
    instruction=```You are an expert document classifier. Analyze the content and classify it into one of these types:
    - CONTRACT: Legal agreements, service contracts, employment contracts
    - INVOICE: Bills, invoices, payment requests, financial statements  
    - RESUME: CVs, resumes, job applications, professional profiles
    - LEGAL_BRIEF: Legal documents, court filings, legal analysis
    - UNKNOWN: Documents that don't fit the above categories
    
    Provide classification confidence and list the key text patterns that led to your decision.```,
    output_schema=DocumentClassification
)

# Specialized contract extractor
contract_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="contract_extractor",
    instruction=```Extract structured data from contracts and legal agreements:
    - All parties involved (names, roles, contact information)
    - Key terms and conditions
    - Financial obligations and payment terms
    - Important dates (effective date, expiration, milestones)
    - Governing law and jurisdiction
    - Termination clauses and conditions
    
    Be extremely precise with legal language and dates.```,
    output_schema=LegalExtraction
)

# Invoice extraction specialist
invoice_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="invoice_extractor", 
    instruction=```Extract structured data from invoices and financial documents:
    - Vendor information (name, address, tax ID)
    - Customer/billing information
    - Line items with descriptions, quantities, unit prices
    - Subtotals, taxes, and total amounts
    - Payment terms and due dates
    - Invoice numbers and reference codes
    
    Ensure all monetary amounts include currency and are properly formatted.```,
    output_schema=LegalExtraction  # In production, use InvoiceExtraction schema
)

# Quality validation agent
validator_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="extraction_validator",
    instruction=```Validate extracted data for completeness and accuracy:
    
    Check for:
    1. All required fields are populated with meaningful data
    2. Data formats are consistent (dates, amounts, etc.)
    3. Logical relationships make sense (dates in proper order, etc.)
    4. No obvious extraction errors or inconsistencies
    
    If validation fails, provide specific recommendations for improvement.
    Use confidence scores: 0.9+ = excellent, 0.7-0.9 = good, 0.5-0.7 = needs review, <0.5 = requires manual intervention```,
    output_schema=ExtractionValidation
)

class MultiAgentExtractionPipeline:
    def __init__(self):
        self.session_service = InMemorySessionService()
        self.agents = {
            'classifier': classifier_agent,
            'contract': contract_extractor,
            'invoice': invoice_extractor,
            'validator': validator_agent
        }
        self.runners = {}
        
        # Initialize runners for each agent
        for name, agent in self.agents.items():
            self.runners[name] = Runner(
                agent=agent,
                app_name=f"extraction_{name}",
                session_service=self.session_service
            )
    
    async def classify_document(self, content: str) -> DocumentClassification:
        ```Classify document to determine processing approach```
        user_message = types.Content(
            role='user',
            parts=[types.Part(text=f"Classify this document:\n\n{content}")]
        )
        
        async for event in self.runners['classifier'].run_async(
            user_id="pipeline_user",
            session_id=f"classify_{hash(content) % 10000}",
            new_message=user_message
        ):
            if hasattr(event, 'content') and event.content and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        try:
                            import json
                            return DocumentClassification.model_validate_json(part.text)
                        except:
                            # Fallback if JSON parsing fails
                            return DocumentClassification(
                                document_type=DocumentType.UNKNOWN,
                                confidence=0.5,
                                key_indicators=["Classification parsing failed"]
                            )
        
        return DocumentClassification(
            document_type=DocumentType.UNKNOWN,
            confidence=0.0,
            key_indicators=["No classification response"]
        )
    
    async def extract_with_specialist(self, content: str, doc_type: DocumentType) -> str:
        ```Route to appropriate specialist for extraction```
        agent_mapping = {
            DocumentType.CONTRACT: 'contract',
            DocumentType.INVOICE: 'invoice',
            DocumentType.LEGAL_BRIEF: 'contract'  # Use contract agent for legal docs
        }
        
        agent_name = agent_mapping.get(doc_type, 'contract')  # Default to contract agent
        
        user_message = types.Content(
            role='user',
            parts=[types.Part(text=f"Extract structured data from this {doc_type.value}:\n\n{content}")]
        )
        
        async for event in self.runners[agent_name].run_async(
            user_id="pipeline_user",
            session_id=f"extract_{agent_name}_{hash(content) % 10000}",
            new_message=user_message
        ):
            if hasattr(event, 'content') and event.content and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        return part.text
        
        return "No extraction result available"
    
    async def validate_extraction(self, extracted_data: str, original_content: str) -> ExtractionValidation:
        ```Validate the quality of extracted data```
        validation_prompt = f```
        Validate this extraction against the original document:
        
        ORIGINAL DOCUMENT:
        {original_content[:1000]}...
        
        EXTRACTED DATA:
        {extracted_data}
        
        Check for completeness, accuracy, and consistency.
        ```
        
        user_message = types.Content(
            role='user',
            parts=[types.Part(text=validation_prompt)]
        )
        
        async for event in self.runners['validator'].run_async(
            user_id="pipeline_user",
            session_id=f"validate_{hash(extracted_data) % 10000}",
            new_message=user_message
        ):
            if hasattr(event, 'content') and event.content and hasattr(event.content, 'parts'):
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        try:
                            import json
                            return ExtractionValidation.model_validate_json(part.text)
                        except:
                            return ExtractionValidation(
                                is_valid=True,
                                confidence_score=0.5,
                                missing_fields=[],
                                quality_issues=["Validation parsing failed"],
                                recommendation="Manual review recommended"
                            )
        
        return ExtractionValidation(
            is_valid=False,
            confidence_score=0.0,
            missing_fields=["all"],
            quality_issues=["No validation response"],
            recommendation="Retry extraction"
        )
    
    async def process_document(self, content: str) -> Dict[str, Any]:
        ```Complete pipeline: classify → extract → validate```
        try:
            # Step 1: Classify document
            classification = await self.classify_document(content)
            
            # Step 2: Extract using appropriate specialist
            extraction_result = await self.extract_with_specialist(content, classification.document_type)
            
            # Step 3: Validate extraction quality
            validation = await self.validate_extraction(extraction_result, content)
            
            return {
                "classification": classification.model_dump(),
                "extraction": extraction_result,
                "validation": validation.model_dump(),
                "pipeline_status": "completed",
                "requires_review": validation.confidence_score < 0.7
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "pipeline_status": "failed",
                "requires_review": True
            }

# Example usage
async def run_multi_agent_example():
    pipeline = MultiAgentExtractionPipeline()
    
    sample_contract = ```
    SERVICE AGREEMENT
    
    This Service Agreement ("Agreement") is entered into on March 15, 2024, between:
    
    Provider: TechCorp Solutions LLC
    Address: 123 Tech Street, San Francisco, CA 94105
    
    Client: Global Industries Inc.
    Address: 456 Business Ave, New York, NY 10001
    
    Services: Software development, maintenance, and technical support
    Term: 24 months beginning April 1, 2024 and ending March 31, 2026
    Payment: $15,000 monthly, due on the 1st of each month
    Late Fee: 1.5% per month on overdue amounts
    Governing Law: State of California
    ```
    
    result = await pipeline.process_document(sample_contract)
    print(f"Pipeline completed: {result['pipeline_status']}")
    print(f"Document type: {result['classification']['document_type']}")
    print(f"Validation score: {result['validation']['confidence_score']}")
    
    if result['requires_review']:
        print("⚠️ This extraction requires manual review")

# To run: asyncio.run(run_multi_agent_example())
```
```

This multi-agent architecture provides several advanced capabilities :

1. **Intelligent Routing**: Documents are automatically routed to the most appropriate extractor
2. **Quality Assurance**: Every extraction is validated before final output
3. **Specialized Processing**: Different document types get specialized handling
4. **Error Recovery**: Failed extractions can be re-routed or escalated

**Common Misconception**: Many believe you need separate tools for each document type. ADK's flexible schema system handles multiple formats with a single, well-designed agent pipeline .

### Example 4: High-Volume Processing (Expert Level)

For production scenarios requiring high throughput, you need efficient batch processing and error handling. This example shows how to build a robust high-volume extraction system.

```python
import asyncio
from typing import List, Dict, Any, AsyncGenerator
from concurrent.futures import ThreadPoolExecutor
import time
from dataclasses import dataclass

@dataclass
class ProcessingResult:
    document_id: str
    extraction_timestamp: str
    confidence_score: float
    processing_time_ms: int
    extracted_data: Dict[str, Any]
    warnings: List[str]
    status: str  # 'success', 'failed', 'needs_review'

class BatchExtractionProcessor:
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.session_service = InMemorySessionService()
        self.extraction_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="batch_extractor",
            description="High-throughput document extraction agent",
            instruction="""Extract structured data efficiently with focus on accuracy and speed.
            
            For each document:
            1. Identify document type quickly
            2. Extract key structured data
            3. Assign confidence score based on extraction quality
            4. Flag any processing issues or warnings
            
            Prioritize accuracy over speed, but aim for consistent performance.""",
            output_schema=LegalExtraction  # Use your specific schema
        )
        
        self.runner = Runner(
            agent=self.extraction_agent,
            app_name="batch_extraction",
            session_service=self.session_service
        )
    
    async def process_single_document(self, doc_id: str, content: str) -> ProcessingResult:
        """Process a single document and return structured result"""
        start_time = time.time()
        
        try:
            user_message = types.Content(
                role='user',
                parts=[types.Part(text=f"Extract structured data from this document:\n\n{content}")]
            )
            
            extraction_result = None
            async for event in self.runner.run_async(
                user_id="batch_user",
                session_id=f"batch_{doc_id}",
                new_message=user_message
            ):
                if hasattr(event, 'content') and event.content:
                    if hasattr(event.content, 'parts') and event.content.parts:
                        for part in event.content.parts:
                            if hasattr(part, 'text'):
                                extraction_result = part.text
                                break
                    if extraction_result:
                        break
            
            end_time = time.time()
            processing_time = int((end_time - start_time) * 1000)
            
            # Parse extraction result and determine confidence
            try:
                import json
                parsed_data = json.loads(extraction_result) if extraction_result else {}
                confidence = self._calculate_confidence(parsed_data, content)
                warnings = self._check_for_warnings(parsed_data, content)
                
                return ProcessingResult(
                    document_id=doc_id,
                    extraction_timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    confidence_score=confidence,
                    processing_time_ms=processing_time,
                    extracted_data=parsed_data,
                    warnings=warnings,
                    status='success' if confidence > 0.7 else 'needs_review'
                )
            except json.JSONDecodeError:
                return ProcessingResult(
                    document_id=doc_id,
                    extraction_timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    confidence_score=0.3,
                    processing_time_ms=processing_time,
                    extracted_data={'raw_response': extraction_result or ''},
                    warnings=['Failed to parse structured output'],
                    status='needs_review'
                )
                
        except Exception as e:
            end_time = time.time()
            processing_time = int((end_time - start_time) * 1000)
            
            return ProcessingResult(
                document_id=doc_id,
                extraction_timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                confidence_score=0.0,
                processing_time_ms=processing_time,
                extracted_data={},
                warnings=[f"Processing failed: {str(e)}"],
                status='failed'
            )
    
    def _calculate_confidence(self, data: Dict, original_content: str) -> float:
        """Calculate confidence score based on extraction completeness"""
        if not data:
            return 0.0
        
        # Basic confidence calculation - customize based on your needs
        filled_fields = sum(1 for v in data.values() if v and str(v).strip())
        total_fields = len(data)
        
        if total_fields == 0:
            return 0.0
        
        field_completeness = filled_fields / total_fields
        
        # Adjust based on content length vs extraction detail
        content_length = len(original_content)
        extraction_detail = len(str(data))
        
        if content_length > 1000 and extraction_detail < 100:
            field_completeness *= 0.8  # Penalize sparse extraction on long docs
        
        return min(0.95, field_completeness)  # Cap at 0.95 to avoid overconfidence
    
    def _check_for_warnings(self, data: Dict, content: str) -> List[str]:
        """Check for potential issues in extraction"""
        warnings = []
        
        if not data:
            warnings.append("No structured data extracted")
        
        # Check for common issues
        empty_fields = [k for k, v in data.items() if not v or str(v).strip() == '']
        if len(empty_fields) > len(data) * 0.5:
            warnings.append(f"Many empty fields: {', '.join(empty_fields[:3])}")
        
        # Check if extraction seems too brief for document length
        if len(content) > 2000 and len(str(data)) < 200:
            warnings.append("Extraction may be incomplete for document length")
        
        return warnings
    
    async def process_batch(self, documents: List[Dict[str, str]]) -> List[ProcessingResult]:
        """Process multiple documents concurrently"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        async def process_with_semaphore(doc):
            async with semaphore:
                return await self.process_single_document(doc['id'], doc['content'])
        
        # Process all documents concurrently with limit
        tasks = [process_with_semaphore(doc) for doc in documents]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Handle any exceptions
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append(ProcessingResult(
                    document_id=documents[i]['id'],
                    extraction_timestamp=time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                    confidence_score=0.0,
                    processing_time_ms=0,
                    extracted_data={},
                    warnings=[f"Task failed: {str(result)}"],
                    status='failed'
                ))
            else:
                processed_results.append(result)
        
        return processed_results
    
    def generate_batch_report(self, results: List[ProcessingResult]) -> Dict[str, Any]:
        """Generate summary report for batch processing"""
        total_docs = len(results)
        successful = sum(1 for r in results if r.status == 'success')
        needs_review = sum(1 for r in results if r.status == 'needs_review')
        failed = sum(1 for r in results if r.status == 'failed')
        
        avg_processing_time = sum(r.processing_time_ms for r in results) / total_docs if total_docs > 0 else 0
        avg_confidence = sum(r.confidence_score for r in results) / total_docs if total_docs > 0 else 0
        
        return {
            "batch_summary": {
                "total_documents": total_docs,
                "successful": successful,
                "needs_review": needs_review,
                "failed": failed,
                "success_rate": successful / total_docs if total_docs > 0 else 0,
                "average_processing_time_ms": round(avg_processing_time, 2),
                "average_confidence": round(avg_confidence, 3)
            },
            "performance_metrics": {
                "documents_per_second": total_docs / (avg_processing_time / 1000) if avg_processing_time > 0 else 0,
                "high_confidence_rate": sum(1 for r in results if r.confidence_score > 0.8) / total_docs if total_docs > 0 else 0
            },
            "issues": {
                "low_confidence_docs": [r.document_id for r in results if r.confidence_score < 0.5],
                "failed_docs": [r.document_id for r in results if r.status == 'failed'],
                "common_warnings": self._get_common_warnings(results)
            }
        }
    
    def _get_common_warnings(self, results: List[ProcessingResult]) -> Dict[str, int]:
        """Get frequency count of common warnings"""
        warning_counts = {}
        for result in results:
            for warning in result.warnings:
                warning_counts[warning] = warning_counts.get(warning, 0) + 1
        return dict(sorted(warning_counts.items(), key=lambda x: x[1], reverse=True)[:5])

# Example usage for high-volume processing
async def run_batch_processing_example():
    processor = BatchExtractionProcessor(max_concurrent=3)
    
    # Sample documents (in production, load from your data source)
    sample_documents = [
        {
            "id": "contract_001",
            "content": "SERVICE AGREEMENT\nThis agreement is between TechCorp and Client Inc...",
        },
        {
            "id": "invoice_002", 
            "content": "INVOICE #INV-2024-001\nBill To: Customer ABC\nAmount: $5,000...",
        },
        {
            "id": "contract_003",
            "content": "EMPLOYMENT CONTRACT\nEmployee: John Smith\nStart Date: 2024-01-15...",
        }
    ]
    
    print("Starting batch processing...")
    results = await processor.process_batch(sample_documents)
    
    # Generate and display report
    report = processor.generate_batch_report(results)
    print(f"\nBatch Processing Complete!")
    print(f"Success Rate: {report['batch_summary']['success_rate']:.2%}")
    print(f"Average Processing Time: {report['batch_summary']['average_processing_time_ms']}ms")
    print(f"Average Confidence: {report['batch_summary']['average_confidence']:.3f}")
    
    if report['issues']['failed_docs']:
        print(f"Failed Documents: {report['issues']['failed_docs']}")

# To run: asyncio.run(run_batch_processing_example())
```


### Example 5: Multi-Modal Extraction with Images and Text (Advanced)

Modern extraction often involves multiple data types. This example shows how to extract structured data from documents that contain both text and images .

```python
from google.genai.types import Part
import base64

class MultiModalExtraction(BaseModel):
    text_content: str = Field(description="Extracted text content")
    image_descriptions: List[str] = Field(description="Descriptions of images found")
    tables_extracted: List[Dict] = Field(description="Structured data from tables")
    charts_data: List[Dict] = Field(description="Data extracted from charts/graphs")
    document_layout: str = Field(description="Overall document structure description")
    quality_assessment: str = Field(description="Assessment of extraction quality")

async def process_image_content(image_data: bytes, tool_context) -> Dict:
    """Process image content using vision capabilities"""
    try:
        # Convert image to base64 for processing
        image_b64 = base64.b64encode(image_data).decode()
        
        # Create vision-enabled content
        image_part = Part(inline_data={
            'mime_type': 'image/jpeg',
            'data': image_b64
        })
        
        # Process with vision model
        # This would use Gemini's vision capabilities
        return {
            "status": "success",
            "description": "Extracted image content",
            "tables": [],  # Extracted table data
            "charts": []   # Extracted chart data
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

multimodal_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="multimodal_extractor",
    instruction="""Extract structured information from documents containing both text and images.
    
    For text content:
    - Extract key information following the schema
    - Maintain semantic relationships
    - Preserve important formatting
    
    For images:
    - Describe visual content
    - Extract data from tables and charts
    - Identify diagrams and their relationships to text
    
    For overall document:
    - Understand layout and structure
    - Connect text and visual elements
    - Assess extraction completeness""",
    output_schema=MultiModalExtraction,
    tools=[process_image_content]
)
```


### Example 6: Enterprise-Scale Extraction with Error Recovery (Expert Level)

For enterprise deployments, you need robust error handling, retry logic, and quality assurance using ADK's callback system.

```python
import logging
from typing import Optional, Dict, Any
import time
import hashlib

class EnterpriseExtraction(BaseModel):
    extraction_id: str = Field(description="Unique extraction identifier")
    source_document_hash: str = Field(description="Hash of source document for tracking")
    extraction_quality: float = Field(description="Quality score 0-1")
    retry_count: int = Field(description="Number of retry attempts")
    processing_stage: str = Field(description="Current processing stage")
    extracted_entities: Dict = Field(description="All extracted entities")
    confidence_scores: Dict = Field(description="Confidence for each extracted field")
    audit_trail: List[str] = Field(description="Processing audit trail")
    warnings: List[str] = Field(description="Processing warnings and issues")

class EnterpriseExtractionPipeline:
    def __init__(self):
        self.session_service = InMemorySessionService()
        self.logger = logging.getLogger(__name__)
        
        # Primary extraction agent with callbacks
        self.primary_extractor = LlmAgent(
            model="gemini-2.0-flash",
            name="enterprise_extractor",
            description="Enterprise-grade document extraction with quality validation",
            instruction="""You are an enterprise-grade document extraction specialist.
            
            Requirements:
            - Maximum accuracy and completeness
            - Detailed confidence scoring for each extracted field
            - Comprehensive error handling and reporting
            - Structured output with quality indicators
            
            For each document:
            1. Analyze document type and complexity
            2. Extract all relevant structured data
            3. Assign confidence scores to each field (0.0-1.0)
            4. Identify potential quality issues or ambiguities
            5. Provide processing recommendations
            
            Never guess or fabricate information. Mark uncertain extractions clearly.""",
            output_schema=LegalExtraction,  # Use appropriate schema
            before_tool_callback=self.validate_input,
            after_tool_callback=self.validate_output
        )
        
        # Fallback extractor with simpler approach
        self.fallback_extractor = LlmAgent(
            model="gemini-1.5-pro",  # Different model for diversity
            name="fallback_extractor",
            description="Fallback extraction with simplified approach",
            instruction="""Simplified extraction approach for challenging documents.
            Focus on extracting the most obvious and certain information.
            Be conservative with confidence scores.""",
            output_schema=LegalExtraction
        )
        
        # Initialize runners
        self.primary_runner = Runner(
            agent=self.primary_extractor,
            app_name="enterprise_primary",
            session_service=self.session_service
        )
        
        self.fallback_runner = Runner(
            agent=self.fallback_extractor,
            app_name="enterprise_fallback", 
            session_service=self.session_service
        )
    
    async def validate_input(self, callback_context, tool, args, tool_context) -> Optional[Dict]:
        """Validate input before processing (ADK callback)"""
        try:
            # Check if we can access the input content
            if hasattr(tool_context, 'user_message'):
                content = str(tool_context.user_message)
                
                if len(content.strip()) < 20:
                    self.logger.warning("Document content too short for meaningful extraction")
                    return {"warning": "Very short document content"}
                
                # Check for potential sensitive patterns (basic example)
                if self.contains_sensitive_patterns(content):
                    self.logger.warning("Document may contain sensitive information")
                    return {"warning": "Potential sensitive content detected"}
            
            return None  # Allow processing to continue
            
        except Exception as e:
            self.logger.error(f"Input validation error: {e}")
            return {"warning": f"Input validation issue: {str(e)}"}
    
    async def validate_output(self, callback_context, tool, result, tool_context) -> Dict:
        """Validate output after processing (ADK callback)"""
        try:
            # Basic output validation
            if not result:
                self.logger.warning("Empty extraction result")
                return {"warning": "No extraction result generated"}
            
            # You can add more sophisticated validation here
            self.logger.info("Extraction completed successfully")
            return result
            
        except Exception as e:
            self.logger.error(f"Output validation error: {e}")
            return result  # Return original result on validation error
    
    def contains_sensitive_patterns(self, content: str) -> bool:
        """Basic check for potentially sensitive content patterns"""
        sensitive_indicators = [
            'social security', 'ssn:', 'password:', 'credit card',
            'confidential', 'classified', 'private key', 'api key'
        ]
        content_lower = content.lower()
        return any(indicator in content_lower for indicator in sensitive_indicators)
    
    def calculate_quality_score(self, extracted_data: str, original_content: str) -> float:
        """Calculate extraction quality score based on multiple factors"""
        try:
            if not extracted_data:
                return 0.0
            
            # Basic quality indicators
            content_length = len(original_content)
            extraction_length = len(extracted_data)
            
            # Quality factors
            length_ratio = min(extraction_length / max(content_length * 0.1, 100), 1.0)
            
            # Check if extraction looks structured (contains JSON-like patterns)
            structured_indicators = ['{', '}', '":', '[', ']']
            structure_score = sum(1 for indicator in structured_indicators if indicator in extracted_data) / len(structured_indicators)
            
            # Combine factors
            quality_score = (length_ratio * 0.4) + (structure_score * 0.6)
            
            return min(quality_score, 0.95)  # Cap at 0.95 to avoid overconfidence
            
        except Exception as e:
            self.logger.error(f"Quality calculation error: {e}")
            return 0.5  # Default moderate quality
    
    async def extract_with_retry(self, document_content: str, max_retries: int = 3) -> EnterpriseExtraction:
        """Extract with automatic retry and fallback strategies"""
        extraction_id = hashlib.md5(document_content[:500].encode()).hexdigest()[:12]
        document_hash = hashlib.sha256(document_content.encode()).hexdigest()[:16]
        audit_trail = []
        warnings = []
        
        for attempt in range(max_retries):
            try:
                audit_trail.append(f"Primary attempt {attempt + 1} started at {time.strftime('%H:%M:%S')}")
                
                user_message = types.Content(
                    role='user',
                    parts=[types.Part(text=f"Extract structured data from this document:\n\n{document_content}")]
                )
                
                extraction_result = None
                async for event in self.primary_runner.run_async(
                    user_id="enterprise_user",
                    session_id=f"extract_{extraction_id}_{attempt}",
                    new_message=user_message
                ):
                    if hasattr(event, 'content') and event.content:
                        if hasattr(event.content, 'parts') and event.content.parts:
                            for part in event.content.parts:
                                if hasattr(part, 'text'):
                                    extraction_result = part.text
                                    break
                        if extraction_result:
                            break
                
                if extraction_result:
                    quality_score = self.calculate_quality_score(extraction_result, document_content)
                    
                    if quality_score >= 0.6:  # Acceptable quality threshold
                        audit_trail.append(f"Primary extraction successful, quality: {quality_score:.3f}")
                        
                        return EnterpriseExtraction(
                            extraction_id=extraction_id,
                            source_document_hash=document_hash,
                            extraction_quality=quality_score,
                            retry_count=attempt,
                            processing_stage="primary_complete",
                            extracted_entities={"raw_extraction": extraction_result},
                            confidence_scores={"overall": quality_score},
                            audit_trail=audit_trail,
                            warnings=warnings
                        )
                    else:
                        warnings.append(f"Primary attempt {attempt + 1} low quality: {quality_score:.3f}")
                        audit_trail.append(f"Quality too low: {quality_score:.3f}, retrying")
                else:
                    warnings.append(f"Primary attempt {attempt + 1} returned no result")
                    audit_trail.append("No extraction result from primary attempt")
                
            except Exception as e:
                error_msg = f"Primary attempt {attempt + 1} failed: {str(e)}"
                warnings.append(error_msg)
                audit_trail.append(error_msg)
                self.logger.error(error_msg)
        
        # All primary attempts failed or low quality, try fallback
        try:
            audit_trail.append("Attempting fallback extraction")
            
            user_message = types.Content(
                role='user',
                parts=[types.Part(text=f"Extract basic structured data from:\n\n{document_content[:2000]}")]  # Limit content for fallback
            )
            
            fallback_result = None
            async for event in self.fallback_runner.run_async(
                user_id="enterprise_user",
                session_id=f"fallback_{extraction_id}",
                new_message=user_message
            ):
                if hasattr(event, 'content') and event.content:
                    if hasattr(event.content, 'parts') and event.content.parts:
                        for part in event.content.parts:
                            if hasattr(part, 'text'):
                                fallback_result = part.text
                                break
                    if fallback_result:
                        break
            
            if fallback_result:
                quality_score = self.calculate_quality_score(fallback_result, document_content) * 0.8  # Penalize fallback
                audit_trail.append(f"Fallback extraction completed, quality: {quality_score:.3f}")
                
                return EnterpriseExtraction(
                    extraction_id=extraction_id,
                    source_document_hash=document_hash,
                    extraction_quality=quality_score,
                    retry_count=max_retries,
                    processing_stage="fallback_complete",
                    extracted_entities={"fallback_extraction": fallback_result},
                    confidence_scores={"overall": quality_score},
                    audit_trail=audit_trail,
                    warnings=warnings + ["Used fallback extraction method"]
                )
            
        except Exception as e:
            error_msg = f"Fallback extraction failed: {str(e)}"
            warnings.append(error_msg)
            audit_trail.append(error_msg)
            self.logger.error(error_msg)
        
        # All methods failed - return failure result
        audit_trail.append("All extraction methods failed")
        return EnterpriseExtraction(
            extraction_id=extraction_id,
            source_document_hash=document_hash,
            extraction_quality=0.0,
            retry_count=max_retries,
            processing_stage="failed",
            extracted_entities={},
            confidence_scores={},
            audit_trail=audit_trail,
            warnings=warnings + ["Complete extraction failure - manual intervention required"]
        )

# Example usage
async def enterprise_extraction_example():
    pipeline = EnterpriseExtractionPipeline()
    
    complex_document = """
    COMPLEX SERVICE AGREEMENT - CONFIDENTIAL
    
    This Master Service Agreement ("Agreement") is entered into as of March 15, 2024,
    between TechCorp Solutions LLC, a Delaware limited liability company ("Provider"),
    and Global Industries International Inc., a New York corporation ("Client").
    
    WHEREAS, Provider offers specialized software development, cloud infrastructure,
    and technical consulting services; and
    
    WHEREAS, Client requires comprehensive technology solutions for their global operations;
    
    NOW THEREFORE, the parties agree as follows:
    
    1. SERVICES: Provider shall deliver:
       - Custom software development (24-month project)
       - Cloud infrastructure setup and maintenance
       - 24/7 technical support and monitoring
       - Staff augmentation services as needed
    
    2. FINANCIAL TERMS:
       - Base fee: $50,000 monthly for core services
       - Development milestone payments: $100,000 per completed phase (5 phases total)
       - Support retainer: $15,000 monthly
       - Overtime rate: $200/hour for emergency support
    
    3. TERM: Initial term of 36 months beginning April 1, 2024
       Auto-renewal for successive 12-month periods unless terminated
    
    4. GOVERNING LAW: State of Delaware
    
    [Document continues with detailed terms...]
    """
    
    print("Starting enterprise extraction with retry logic...")
    result = await pipeline.extract_with_retry(complex_document)
    
    print(f"\nExtraction Results:")
    print(f"Quality Score: {result.extraction_quality:.3f}")
    print(f"Processing Stage: {result.processing_stage}")
    print(f"Retry Count: {result.retry_count}")
    print(f"Warnings: {len(result.warnings)}")
    
    if result.warnings:
        print("Issues encountered:")
        for warning in result.warnings[-3:]:  # Show last 3 warnings
            print(f"  - {warning}")
    
    if result.extraction_quality > 0.6:
        print("✅ Extraction successful - ready for production use")
    elif result.extraction_quality > 0.3:
        print("⚠️ Extraction partially successful - review recommended")
    else:
        print("❌ Extraction failed - manual intervention required")

# To run: asyncio.run(enterprise_extraction_example())
```
                extraction_quality=0.0,
                retry_count=max_retries,
                processing_stage="failed",
                extracted_entities={},
                confidence_scores={},
                audit_trail=audit_trail
            )

# Usage in production environment
async def production_extraction_workflow():
    extractor = EnterpriseExtractionAgent()
    
    documents = get_document_queue()  # Your document source
    
    for document in documents:
        try:
            result = await extractor.extract_with_retry(document.content)
            
            if result.extraction_quality >= 0.7:
                await store_successful_extraction(result)
            else:
                await route_to_manual_review(result)
                
        except Exception as e:
            logging.error(f"Critical extraction failure for document {document.id}: {e}")
            await handle_critical_failure(document)
```

## When: Real-World Applications That Drive Results

### 📊 Business Intelligence and Analytics

The power of structured extraction shines brightest in business intelligence scenarios where unstructured data contains critical insights .

**Customer Feedback Analysis**: Modern businesses receive thousands of customer feedback messages daily across email, social media, chat logs, and survey responses . Traditional sentiment analysis tools only scratch the surface. ADK's structured extraction can simultaneously identify:

- Specific product features mentioned
- Sentiment scores for individual aspects
- Suggested improvements or feature requests
- Customer demographics and usage patterns
- Priority levels based on urgency indicators
- Actionable items for different departments

**Market Research Automation**: Investment firms and consulting companies spend enormous resources on market research . ADK can automate the extraction of competitive intelligence from:

- Earnings calls and financial reports
- Industry analyst reports
- News articles and press releases
- Patent filings and technical documents
- Social media discussions and forums
- Government regulatory filings

**Financial Data Processing**: Financial institutions process millions of documents containing critical data . Structured extraction enables automatic processing of:

- Loan applications with risk assessment indicators
- Insurance claims with damage estimates and coverage details
- Trading documents with regulatory compliance markers
- Audit reports with finding categorizations
- Credit reports with standardized risk scoring


### 🏥 Healthcare and Compliance

Healthcare organizations face unique challenges with patient data, regulatory requirements, and clinical documentation .

**Medical Records Processing**: Clinical notes contain vast amounts of unstructured information that impacts patient care . ADK can extract:

- Patient symptoms and medical history
- Treatment plans and medication schedules
- Diagnostic test results and interpretations
- Follow-up requirements and care instructions
- Risk factors and contraindications
- Insurance and billing information

**Clinical Research Data**: Pharmaceutical companies and research institutions need to extract data from clinical trial documents :

- Patient enrollment criteria and demographics
- Adverse event reports with severity classifications
- Treatment efficacy measurements
- Protocol deviations and their impact
- Safety monitoring data
- Regulatory compliance indicators

**Insurance Claims Processing**: Healthcare insurers process millions of claims requiring structured data extraction :

- Medical procedure codes and descriptions
- Provider information and credentials
- Patient eligibility and coverage details
- Pre-authorization requirements
- Claim status and processing notes
- Appeal and denial reasons


### 💼 Legal and Professional Services

Legal professionals deal with massive volumes of unstructured documents where precision is critical .

**Contract Analysis and Management**: Law firms and corporate legal departments need to analyze thousands of contracts :

- Party identification and roles
- Financial terms and payment schedules
- Performance obligations and deadlines
- Termination and renewal clauses
- Governing law and jurisdiction
- Risk factors and liability limitations

**Discovery and Due Diligence**: Legal discovery processes involve reviewing massive document sets :

- Privileged communication identification
- Key date and deadline extraction
- Relevant party and entity mentions
- Document classification and prioritization
- Redaction requirements identification
- Chain of custody documentation

**Regulatory Compliance Monitoring**: Organizations must monitor regulatory changes and ensure compliance :

- New regulation identification and impact assessment
- Compliance requirement extraction
- Policy update requirements
- Training and implementation needs
- Audit trail documentation
- Risk assessment indicators


### 🏭 Operations and Automation

Operational efficiency gains from structured extraction can transform business processes .

**Supply Chain Documentation**: Modern supply chains generate enormous amounts of unstructured data :

- Purchase orders and invoicing details
- Shipping and logistics documentation
- Quality control reports and certifications
- Supplier performance metrics
- Inventory level notifications
- Compliance and regulatory documentation

**Customer Service Automation**: Support organizations can dramatically improve efficiency :

- Ticket classification and priority assignment
- Solution recommendation based on historical data
- Escalation criteria and routing rules
- Customer satisfaction indicators
- Knowledge base article suggestions
- Performance metrics and KPI tracking

**Human Resources Processing**: HR departments handle vast amounts of unstructured employee data :

- Resume and application screening
- Performance review analysis
- Training needs assessment
- Compliance documentation
- Employee feedback categorization
- Policy acknowledgment tracking

**⚡ Quick Quiz**: Which use case matches your current business challenge? (Remember this—it'll guide your implementation!)

## Pro Tips: Insider Secrets for Maximum Impact

### 🎯 Performance Optimization Strategies

Achieving production-ready performance requires attention to specific optimization techniques that can dramatically improve both speed and accuracy .

**Schema Design for Speed**: The structure of your Pydantic schemas directly impacts extraction performance . Design schemas that are:

- **Specific but not overly complex**: Aim for 5-15 fields per schema rather than monolithic structures with 50+ fields
- **Well-documented**: Each field should have clear descriptions that guide the AI precisely
- **Hierarchically organized**: Use nested structures to group related fields logically
- **Type-safe**: Leverage Python's typing system for automatic validation

```python
# Optimized schema design
class OptimizedExtraction(BaseModel):
    # Core identification (always include)
    document_id: str = Field(description="Unique document identifier")
    
    # Primary content (essential fields only)
    main_entities: List[str] = Field(description="Primary entities mentioned", max_items=10)
    key_dates: List[str] = Field(description="Critical dates in ISO format", max_items=5)
    
    # Secondary content (optional but useful)
    financial_data: Optional[FinancialSummary] = Field(description="Financial information if present")
    
    # Metadata (for quality control)
    confidence_score: float = Field(description="Extraction confidence 0-1", ge=0.0, le=1.0)
```

**Prompt Engineering for Accuracy**: Your instruction prompts are the single most important factor in extraction quality . Effective prompts should:

- **Set clear expectations**: Tell the AI exactly what constitutes success
- **Provide examples**: Include 2-3 examples of perfect extractions
- **Handle edge cases**: Specify what to do with ambiguous or missing information
- **Enforce formatting**: Require specific date formats, currency handling, etc.

**Batch Processing Optimization**: For high-volume scenarios, implement intelligent batching strategies :

- **Document similarity grouping**: Process similar document types together
- **Size-based batching**: Group documents by complexity for optimal resource utilization
- **Priority queuing**: Process urgent documents first while maintaining throughput
- **Load balancing**: Distribute work across multiple agent instances


### 🚨 Common Pitfalls to Avoid

Learning from others' mistakes can save you weeks of troubleshooting .

**Over-Engineering the Schema**: The most common mistake is creating overly complex schemas that confuse the AI . Signs you're over-engineering:

- Schemas with more than 20 top-level fields
- Deeply nested structures (more than 3 levels)
- Ambiguous field names or descriptions
- Optional fields that aren't truly optional

**Ignoring Error Handling**: Production systems must handle failures gracefully :

```python
# Robust error handling pattern
async def safe_extraction(document_content: str) -> ExtractionResult:
    try:
        result = await extractor.extract(document_content)
        
        # Validate result quality
        if result.confidence_score < MIN_CONFIDENCE:
            return await fallback_extraction(document_content)
        
        return result
        
    except ValidationError as e:
        logger.warning(f"Schema validation failed: {e}")
        return await simplified_extraction(document_content)
        
    except Exception as e:
        logger.error(f"Extraction failed completely: {e}")
        return create_error_result(str(e))
```

**Skipping Quality Evaluation**: Without systematic evaluation, you can't improve your extraction quality :

- **Establish baseline metrics**: Measure accuracy, completeness, and processing time
- **Create test datasets**: Maintain gold-standard examples for consistent evaluation
- **Monitor drift**: Track performance changes over time as models and data evolve
- **A/B testing**: Compare different prompt strategies and schema designs


### 🔧 Advanced Techniques

These sophisticated approaches separate production-ready systems from prototype experiments .

**Context-Aware Extraction**: Use the full power of ADK's context management :

```python
def context_aware_extractor(document: str, tool_context: ToolContext) -> dict:
    # Access previous extractions for consistency
    previous_extractions = tool_context.state.get("recent_extractions", [])
    
    # Use document artifacts for large files
    if len(document) > 50000:  # Large document
        # Store as artifact and process in chunks
        artifact_part = types.Part(text=document)
        tool_context.save_artifact("large_document.txt", artifact_part)
        return process_large_document_chunks(tool_context)
    
    # Standard processing for normal-sized documents
    return standard_extraction(document, previous_extractions)
```

**Multi-Stage Quality Validation**: Implement layered validation for critical applications :

```python
class QualityValidator:
    def __init__(self):
        self.stage1_validator = LlmAgent(
            instruction="Quick quality check for obvious errors",
            output_schema=SimpleValidation
        )
        
        self.stage2_validator = LlmAgent(
            instruction="Detailed accuracy assessment with confidence scoring",
            output_schema=DetailedValidation
        )
    
    async def validate_extraction(self, result: ExtractionResult) -> ValidationResult:
        # Stage 1: Fast validation
        quick_check = await self.stage1_validator.validate(result)
        if not quick_check.passes_basic_checks:
            return ValidationResult(status="failed", stage="basic_validation")
        
        # Stage 2: Detailed validation
        detailed_check = await self.stage2_validator.validate(result)
        return ValidationResult(
            status="passed" if detailed_check.confidence > 0.8 else "review_needed",
            confidence=detailed_check.confidence,
            stage="detailed_validation"
        )
```

**Adaptive Processing Strategies**: Implement intelligent routing based on document characteristics :

```python
class AdaptiveProcessor:
    def __init__(self):
        self.simple_extractor = create_fast_extractor()
        self.complex_extractor = create_thorough_extractor()
        self.specialist_extractors = {
            "legal": create_legal_extractor(),
            "financial": create_financial_extractor(),
            "medical": create_medical_extractor()
        }
    
    async def route_document(self, document: str) -> ExtractionResult:
        # Analyze document characteristics
        analysis = await self.analyze_document(document)
        
        if analysis.complexity == "simple":
            return await self.simple_extractor.extract(document)
        elif analysis.domain in self.specialist_extractors:
            return await self.specialist_extractors[analysis.domain].extract(document)
        else:
            return await self.complex_extractor.extract(document)
```


## Your 24-Hour Challenge: From Learning to Leading

**Here's your mission** (choose to accept it): Pick one unstructured data source in your organization and build a production-ready extraction agent within 24 hours.

### Hour-by-Hour Action Plan

#### Hours 1-3: Foundation Setup

- Install ADK and set up your development environment
- Choose your target data source and define success criteria
- Create your first basic schema using the contact extraction example as a template
- Test the basic setup with 2-3 sample documents

#### Hours 4-8: Schema Development and Testing

- Design your production schema based on your specific use case
- Write comprehensive extraction instructions with examples
- Implement basic error handling and validation
- Test with 10-20 diverse documents to identify edge cases

#### Hours 9-16: Advanced Features and Optimization

- Add quality validation and confidence scoring
- Implement retry logic and fallback strategies
- Create a simple evaluation framework to measure accuracy
- Optimize performance for your expected document volume

#### Hours 17-22: Production Readiness

- Add comprehensive logging and monitoring
- Implement safety filters for sensitive content
- Create deployment scripts and documentation
- Conduct final testing with production-like data volumes

#### Hours 23-24: Deployment and Monitoring

- Deploy to your target environment
- Monitor initial performance and accuracy metrics
- Document lessons learned and improvement opportunities
- Plan next iteration based on real-world feedback

### Success Metrics for Your 24-Hour Challenge

**Technical Achievements**:

- ✅ Extract at least 5 different field types with 90%+ accuracy
- ✅ Process 100+ documents without system failures
- ✅ Achieve average processing time under 10 seconds per document
- ✅ Implement comprehensive error handling that gracefully manages failures

**Business Impact**:

- ✅ Save at least 4 hours of manual work compared to previous methods
- ✅ Improve data quality with structured, validated outputs
- ✅ Create reusable extraction pipeline for future documents
- ✅ Generate actionable insights that drive business decisions

**Knowledge and Skills**:

- ✅ Master ADK's core concepts: agents, schemas, and tools
- ✅ Understand production considerations: error handling, monitoring, and optimization
- ✅ Build confidence in tackling more complex extraction challenges
- ✅ Create foundation for scaling to enterprise-level solutions


### Real-World Success Stories

**Case Study 1: Legal Firm Contract Analysis**
A mid-size law firm reduced contract review time from 3 hours per document to 15 minutes using ADK structured extraction . They achieved:

- 95% accuracy in extracting key terms and dates
- 85% reduction in manual review time
- 100% improvement in consistency across reviewers
- \$500K annual savings in labor costs

**Case Study 2: Healthcare Claims Processing**
A regional insurance company automated their claims processing pipeline :

- Processing time reduced from 48 hours to 2 hours
- Error rate decreased from 12% to 2%
- Customer satisfaction increased by 40%
- Operational costs reduced by 60%

**Case Study 3: Financial Services Risk Assessment**
An investment firm automated their due diligence document analysis :

- Document processing speed increased 10x
- Risk factor identification improved by 30%
- Regulatory compliance accuracy reached 99.5%
- Analysis quality became consistent across all analysts


### Building Your Extraction Center of Excellence

#### Month 1: Foundation

- Establish extraction standards and best practices
- Train team members on ADK fundamentals
- Create reusable schema templates for common document types
- Build quality evaluation frameworks

#### Month 2: Expansion

- Add specialized extractors for different business domains
- Implement advanced multi-agent workflows
- Create self-service tools for business users
- Establish monitoring and alerting systems

#### Month 3: Optimization

- Fine-tune performance based on production data
- Implement advanced safety and compliance features
- Build integration with existing business systems
- Create documentation and training materials

**Remember**: Every expert was once a beginner who refused to give up. Your journey to data extraction mastery starts with that first line of code, but it accelerates exponentially with each successful implementation.

## Advanced Production Patterns

### Enterprise Integration Strategies

Moving beyond prototype to production requires sophisticated integration patterns that scale with your organization's needs .

**API Gateway Integration**: Most enterprises need to expose extraction capabilities through standardized APIs :

```python
from fastapi import FastAPI, HTTPException
from google.adk.agents import LlmAgent
import asyncio

app = FastAPI(title="Enterprise Extraction API")

class ExtractionAPI:
    def __init__(self):
        self.extractors = {
            "contracts": ContractExtractor(),
            "invoices": InvoiceExtractor(),
            "reports": ReportExtractor()
        }
        
    async def extract_document(self, document_type: str, content: str) -> dict:
        if document_type not in self.extractors:
            raise HTTPException(status_code=400, detail="Unsupported document type")
        
        extractor = self.extractors[document_type]
        result = await extractor.extract(content)
        
        return {
            "extraction_id": generate_unique_id(),
            "document_type": document_type,
            "extracted_data": result.dict(),
            "confidence_score": result.confidence_score,
            "processing_time_ms": result.processing_time_ms
        }

extraction_api = ExtractionAPI()

@app.post("/extract/{document_type}")
async def extract_endpoint(document_type: str, content: str):
    return await extraction_api.extract_document(document_type, content)
```

**Database Integration Patterns**: Production systems require robust data persistence strategies :

```python
class ExtractionDatabase:
    def __init__(self, connection_string: str):
        self.db = create_database_connection(connection_string)
        
    async def store_extraction(self, result: ExtractionResult) -> str:
        """Store extraction with full audit trail"""
        extraction_record = {
            "id": result.extraction_id,
            "document_hash": hash_document(result.source_document),
            "extracted_data": result.extracted_data,
            "confidence_scores": result.confidence_scores,
            "processing_metadata": result.metadata,
            "created_at": datetime.utcnow(),
            "schema_version": result.schema_version
        }
        
        # Store with versioning for schema evolution
        await self.db.extractions.insert_one(extraction_record)
        return extraction_record["id"]
        
    async def query_extractions(self, filters: dict) -> List[ExtractionResult]:
        """Query stored extractions with flexible filtering"""
        cursor = self.db.extractions.find(filters)
        return [ExtractionResult.from_dict(doc) async for doc in cursor]
```

**Message Queue Integration**: For high-volume scenarios, implement asynchronous processing :

```python
import asyncio
from asyncio import Queue
import aioredis

class ExtractionQueue:
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)
        self.processing_queue = Queue()
        
    async def enqueue_document(self, document: dict) -> str:
        """Add document to processing queue"""
        task_id = generate_task_id()
        task_data = {
            "task_id": task_id,
            "document": document,
            "submitted_at": datetime.utcnow().isoformat(),
            "status": "queued"
        }
        
        await self.redis.lpush("extraction_queue", json.dumps(task_data))
        return task_id
        
    async def process_queue(self, num_workers: int = 4):
        """Process documents with multiple workers"""
        workers = [
            asyncio.create_task(self.worker(f"worker_{i}"))
            for i in range(num_workers)
        ]
        
        await asyncio.gather(*workers)
        
    async def worker(self, worker_id: str):
        """Individual worker for processing documents"""
        while True:
            try:
                # Get next task from queue
                task_data = await self.redis.brpop("extraction_queue", timeout=30)
                if not task_data:
                    continue
                    
                task = json.loads(task_data)
                
                # Process the document
                result = await self.extract_document(task["document"])
                
                # Store result
                await self.store_result(task["task_id"], result)
                
            except Exception as e:
                logger.error(f"Worker {worker_id} error: {e}")
                await asyncio.sleep(5)  # Brief pause before retry
```

### Monitoring and Observability

Production extraction systems require comprehensive monitoring to ensure reliability and performance .

**Performance Monitoring Dashboard**:

```python
class ExtractionMonitor:
    def __init__(self):
        self.metrics = {
            "total_extractions": 0,
            "successful_extractions": 0,
            "failed_extractions": 0,
            "average_processing_time": 0.0,
            "average_confidence_score": 0.0
        }
        
    async def record_extraction(self, result: ExtractionResult):
        """Record extraction metrics"""
        self.metrics["total_extractions"] += 1
        
        if result.success:
            self.metrics["successful_extractions"] += 1
            
            # Update rolling averages
            self.update_average("average_processing_time", result.processing_time_ms)
            self.update_average("average_confidence_score", result.confidence_score)
        else:
            self.metrics["failed_extractions"] += 1
            
    def update_average(self, metric_name: str, new_value: float):
        """Update rolling average for metric"""
        current_avg = self.metrics[metric_name]
        total_count = self.metrics["successful_extractions"]
        
        # Calculate new rolling average
        self.metrics[metric_name] = (
            (current_avg * (total_count - 1) + new_value) / total_count
        )
        
    def get_health_status(self) -> dict:
        """Get system health metrics"""
        success_rate = (
            self.metrics["successful_extractions"] / 
            max(self.metrics["total_extractions"], 1)
        )
        
        return {
            "status": "healthy" if success_rate > 0.95 else "degraded",
            "success_rate": success_rate,
            "average_processing_time": self.metrics["average_processing_time"],
            "average_confidence": self.metrics["average_confidence_score"],
            "total_processed": self.metrics["total_extractions"]
        }
```

Ready to transform your data chaos into structured intelligence? The only question left is: will you be leading the AI revolution, or watching from the sidelines? 

**Start your 24-hour challenge now**: Install ADK and let the extraction begin! Your journey from data extraction novice to practitioner starts with that first schema definition, but accelerates exponentially with each successful implementation. 🚀

---

*What unstructured data will you conquer first? Share your results and join the community of ADK practitioners transforming businesses worldwide.*

## References and Further Reading

### Official Google ADK Documentation

- [ADK Overview and Getting Started](https://google.github.io/adk-docs/)
- [LLM Agents Documentation](https://google.github.io/adk-docs/agents/llm-agents/)
- [Multi-Agent Systems](https://google.github.io/adk-docs/agents/multi-agents/)
- [Tools and Function Calling](https://google.github.io/adk-docs/tools/)
- [Events and Streaming](https://google.github.io/adk-docs/events/)
- [Safety and Evaluation](https://google.github.io/adk-docs/safety/)
- [Deployment Guide](https://google.github.io/adk-docs/deploy/)
- [Official Tutorials](https://google.github.io/adk-docs/tutorials/)

### Additional Resources

- [Gemini API Structured Data Extraction](https://ai.google.dev/gemini-api/tutorials/extract_structured_data)
- [Pydantic AI for Output Validation](https://ai.pydantic.dev/output/)
- [AgentOps Integration with ADK](https://docs.agentops.ai/v2/integrations/google_adk)

### Community Examples

- [ADK Example Repository](https://github.com/gremlin961/google_adk_example)
- [ADK Walkthrough](https://github.com/sokart/adk-walkthrough)
- [Pratik's ADK Tutorial](https://github.com/pratik008/adk-tutorial)

