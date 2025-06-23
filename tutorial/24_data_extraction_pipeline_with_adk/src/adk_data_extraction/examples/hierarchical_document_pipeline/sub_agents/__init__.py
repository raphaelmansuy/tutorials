"""
Sub-agents for Hierarchical Document Pipeline

This module contains specialized sub-agents for different document types
and processing steps in the hierarchical extraction pipeline.
"""

from google.adk.agents import LlmAgent

from ..schemas import (
    ContractData,
    DocumentClassification,
    GeneralData,
    InvoiceData,
    ValidationSummary,
)


def create_document_classifier() -> LlmAgent:
    """Create the document classification agent"""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="document_classifier",
        description="Classifies documents and determines processing approach",
        instruction="""You are an expert document classifier and processing coordinator.

IMPORTANT: You must respond with ONLY a JSON object that matches the DocumentClassification schema.

Your role:
1. Analyze document content and structure
2. Determine document type (contract, invoice, agreement, proposal, report, email, unknown)
3. Assess complexity level (simple, medium, complex)
4. Recommend appropriate extraction agent
5. Provide confidence scores and key indicators

Classification criteria:
- Contracts: Contains parties, terms, obligations, signatures
- Invoices: Contains vendor, amounts, line items, payment terms
- Agreements: Similar to contracts but more general
- Proposals: Contains project details, costs, timelines
- Reports: Analysis, findings, recommendations
- Emails: Communication format with headers

Respond with this JSON format:
{
    "document_type": "contract",
    "complexity_level": "medium",
    "estimated_processing_time": 45,
    "recommended_extractor": "contract_specialist",
    "confidence_score": 0.85,
    "key_indicators": ["parties", "payment terms", "signatures"]
}

Return ONLY the JSON, no additional text or explanation.""",
        output_schema=DocumentClassification,
        output_key="classification_result",
        disallow_transfer_to_parent=False,
        disallow_transfer_to_peers=True,
    )


def create_contract_specialist() -> LlmAgent:
    """Create the contract extraction specialist agent"""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="contract_specialist",
        description="Specialized agent for extracting data from contracts and agreements",
        instruction="""You are a contract analysis specialist with expertise in legal documents.

IMPORTANT: You must respond with ONLY a JSON object that matches the ContractData schema.

Your role:
1. Extract key contract information including parties, terms, and obligations
2. Identify financial terms, dates, and governing law
3. Analyze payment schedules and key obligations
4. Return structured data in the exact JSON format specified

Focus on extracting:
- All contracting parties (companies, individuals)
- Contract value and currency
- Start and end dates
- Payment terms and schedules
- Key obligations for each party
- Governing law jurisdiction

Extract contract data in this JSON format:
{
    "parties": ["Company A", "Company B"],
    "contract_value": 50000.00,
    "currency": "USD",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "payment_terms": ["Net 30", "Monthly payments"],
    "key_obligations": ["Deliver services", "Make payments"],
    "governing_law": "California"
}

Return ONLY the JSON, no additional text or explanation.""",
        output_schema=ContractData,
        output_key="contract_extraction",
        disallow_transfer_to_parent=False,
        disallow_transfer_to_peers=True,
    )


def create_invoice_specialist() -> LlmAgent:
    """Create the invoice extraction specialist agent"""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="invoice_specialist",
        description="Specialized agent for extracting data from invoices and bills",
        instruction="""You are an invoice processing specialist with expertise in financial documents.

IMPORTANT: You must respond with ONLY a JSON object that matches the InvoiceData schema.

Your role:
1. Extract all invoice details including numbers, amounts, and dates
2. Identify vendor and customer information
3. Process line items and calculate totals
4. Return structured data in the exact JSON format specified

Focus on extracting:
- Invoice number and dates
- Vendor and customer names
- Total amount and currency
- Line items with quantities and prices
- Tax amounts and payment terms

Extract invoice data in this JSON format:
{
    "invoice_number": "INV-2024-001",
    "vendor_name": "Acme Corp",
    "customer_name": "ABC Company",
    "invoice_date": "2024-01-15",
    "due_date": "2024-02-15",
    "total_amount": 1500.00,
    "currency": "USD",
    "line_items": ["Item 1: $500.00", "Item 2: $1000.00"],
    "tax_amount": 123.45
}

Return ONLY the JSON, no additional text or explanation.""",
        output_schema=InvoiceData,
        output_key="invoice_extraction",
        disallow_transfer_to_parent=False,
        disallow_transfer_to_peers=True,
    )


def create_general_specialist() -> LlmAgent:
    """Create the general document extraction specialist agent"""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="general_specialist",
        description="General-purpose agent for extracting key information from various documents",
        instruction="""You are a general document analysis specialist.

IMPORTANT: You must respond with ONLY a JSON object that matches the GeneralData schema.

Your role:
1. Analyze any type of document for key information
2. Extract entities, dates, summary, and action items
3. Return results in the exact JSON format specified by the schema
4. Provide comprehensive yet concise extraction

Extract general document data in this JSON format:
{
    "document_title": "Main subject or title",
    "main_entities": ["entity1", "entity2", "entity3"],
    "key_dates": ["2024-01-01", "2024-02-01"],
    "summary": "Brief overview of content and purpose",
    "action_items": ["action 1", "action 2"],
    "contact_info": ["email@example.com", "555-123-4567"]
}

Return ONLY the JSON, no additional text or explanation.""",
        output_schema=GeneralData,
        output_key="general_extraction",
        disallow_transfer_to_parent=False,
        disallow_transfer_to_peers=True,
    )


def create_validation_specialist() -> LlmAgent:
    """Create the validation specialist agent"""
    return LlmAgent(
        model="gemini-2.0-flash",
        name="validation_specialist",
        description="Quality assurance agent that validates extraction results",
        instruction="""You are a quality assurance specialist for data extraction validation.

IMPORTANT: You must respond with ONLY a JSON object that matches the ValidationSummary schema.

Your role:
1. Review extraction results from other agents
2. Check for completeness, accuracy, and consistency
3. Provide quality scores and recommendations
4. Return validation results in the exact JSON format specified

Validation criteria:
- Completeness: Are all expected fields populated?
- Accuracy: Does extracted data match the source document?
- Consistency: Are formats and relationships logical?
- Quality: Overall extraction quality assessment

Extract validation data in this JSON format:
{
    "is_valid": true,
    "confidence_score": 0.85,
    "completeness_score": 0.90,
    "issues": ["issue1", "issue2"],
    "recommendation": "approved"
}

Recommendations: "approved", "review_needed", "retry_extraction", or "manual_processing"

Return ONLY the JSON, no additional text or explanation.""",
        output_schema=ValidationSummary,
        output_key="validation_result",
        disallow_transfer_to_parent=False,
        disallow_transfer_to_peers=True,
    )
