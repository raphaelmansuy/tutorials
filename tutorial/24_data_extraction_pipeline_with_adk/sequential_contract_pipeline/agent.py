"""
Service Contract Processing Pipeline - Sequential Pattern Example

This educational example demonstrates Google ADK's Sequential Pipeline Pattern
following the official documentation and samples.

Usage:
1. Run: adk run sequential_contract_pipeline
2. Type 'sample' to use the built-in sample contract
3. Or paste your own service contract document
"""

from google.adk.agents import LlmAgent, SequentialAgent
from pydantic import BaseModel, Field

# Sample service contract for testing
SAMPLE_CONTRACT = """
PROFESSIONAL SERVICES AGREEMENT

This Professional Services Agreement is effective March 1, 2024, between:

SERVICE PROVIDER: CloudTech Solutions Inc.
Principal Office: 789 Tech Plaza, Austin, TX 78701

CLIENT: Innovation Corp LLC
Business Address: 456 Business Center, Dallas, TX 75201

SERVICES: Cloud infrastructure consulting and migration services including:
• Current infrastructure assessment and analysis
• AWS cloud migration strategy and planning
• Cloud infrastructure implementation
• Data migration and system integration
• Staff training and knowledge transfer
• 3 months post-migration support

FINANCIAL TERMS:
Total Contract Value: $85,000 USD

Payment Schedule:
• $25,000 upon contract execution (March 1, 2024)
• $35,000 upon migration planning completion (May 1, 2024)
• $25,000 upon successful cloud deployment (July 15, 2024)

PROJECT TIMELINE:
Start Date: March 15, 2024
Planning Phase: March 15 - May 1, 2024
Migration Phase: May 1 - July 15, 2024
Support Period: July 16 - October 15, 2024
Contract End Date: October 15, 2024

LEGAL TERMS:
Governing Law: State of Texas
Termination Notice: 15 days written notice
Liability Cap: Total contract value ($85,000)

Signatures:
CloudTech Solutions Inc.: _________________ Date: _______
Innovation Corp LLC: _________________ Date: _______
"""


class ServiceContractData(BaseModel):
    """Schema for service contract extraction results"""
    service_provider: str = Field(description="Name of the service provider company")
    client_company: str = Field(description="Name of the client company")
    contract_value: float = Field(description="Total contract value in USD")
    service_description: str = Field(description="Brief description of services provided")
    start_date: str = Field(description="Contract start date")
    end_date: str = Field(description="Contract end date")
    duration_months: int = Field(description="Contract duration in months")
    payment_terms: list[str] = Field(description="Payment schedule and terms")
    total_payments: int = Field(description="Number of payment milestones")
    governing_law: str = Field(description="Governing law jurisdiction")
    termination_notice: str = Field(description="Required termination notice period")


class ValidationReport(BaseModel):
    """Schema for contract validation results"""
    is_complete: bool = Field(description="Whether all required fields are extracted")
    data_quality: str = Field(description="Overall data quality: excellent, good, fair, poor")
    missing_fields: list[str] = Field(description="List of missing or incomplete fields")
    data_issues: list[str] = Field(description="Data quality issues identified")
    confidence_score: float = Field(description="Confidence in extraction (0-1)", ge=0.0, le=1.0)
    recommendation: str = Field(description="Processing recommendation: approve, review, reject")


class ContractSummary(BaseModel):
    """Schema for final contract summary report"""
    contract_title: str = Field(description="Descriptive title for the contract")
    executive_summary: str = Field(description="Brief executive summary")
    key_highlights: list[str] = Field(description="Most important contract points")
    financial_overview: str = Field(description="Summary of financial terms")
    timeline_overview: str = Field(description="Summary of key dates and milestones")
    risk_factors: list[str] = Field(description="Potential risks or concerns identified")
    next_actions: list[str] = Field(description="Recommended follow-up actions")


# Step 1: Service Contract Data Extractor with built-in sample
service_data_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="ServiceDataExtractor",
    description="Extracts structured data from service contracts",
    instruction="""You are a Service Contract Data Extraction specialist.

WELCOME & SAMPLE CONTRACT:
If the user types 'sample', use this sample contract for processing:

PROFESSIONAL SERVICES AGREEMENT

This Professional Services Agreement is effective March 1, 2024, between:

SERVICE PROVIDER: CloudTech Solutions Inc.
Principal Office: 789 Tech Plaza, Austin, TX 78701

CLIENT: Innovation Corp LLC
Business Address: 456 Business Center, Dallas, TX 75201

SERVICES: Cloud infrastructure consulting and migration services including:
• Current infrastructure assessment and analysis
• AWS cloud migration strategy and planning
• Cloud infrastructure implementation
• Data migration and system integration
• Staff training and knowledge transfer
• 3 months post-migration support

FINANCIAL TERMS:
Total Contract Value: $85,000 USD

Payment Schedule:
• $25,000 upon contract execution (March 1, 2024)
• $35,000 upon migration planning completion (May 1, 2024)
• $25,000 upon successful cloud deployment (July 15, 2024)

PROJECT TIMELINE:
Start Date: March 15, 2024
Planning Phase: March 15 - May 1, 2024
Migration Phase: May 1 - July 15, 2024
Support Period: July 16 - October 15, 2024
Contract End Date: October 15, 2024

LEGAL TERMS:
Governing Law: State of Texas
Termination Notice: 15 days written notice
Liability Cap: Total contract value ($85,000)

EXTRACTION INSTRUCTIONS:
Your task is to extract key information from the service contract (sample or user-provided).

EXTRACTION FOCUS:
• Service Provider and Client company names
• Contract value and financial terms
• Service description and scope
• Start date, end date, and duration
• Payment schedule and terms
• Legal jurisdiction and termination clauses

Please extract dates in YYYY-MM-DD format when possible.
Extract monetary values as numbers (e.g., 85000.0 for $85,000).
Be precise and accurate with all extracted information.

FORMAT YOUR RESPONSE AS:
=== SERVICE CONTRACT DATA EXTRACTION ===

SERVICE PROVIDER: [Provider Company Name]
CLIENT COMPANY: [Client Company Name]
CONTRACT VALUE: [Total USD value]
SERVICE DESCRIPTION: [Brief service description]

TIMELINE:
- Start Date: [YYYY-MM-DD]
- End Date: [YYYY-MM-DD]
- Duration: [X months]

PAYMENT INFORMATION:
- Payment Terms: [List payment schedule/terms]
- Total Payments: [Number of payment milestones]

LEGAL FRAMEWORK:
- Governing Law: [Jurisdiction]
- Termination Notice: [Notice period required]

If the user provides no document and doesn't type 'sample', respond with:
"Welcome to the Service Contract Processing Pipeline!

Please either:
1. Type 'sample' to process our sample contract
2. Paste your service contract document for processing

I will extract key contract data, validate it, and generate a comprehensive summary report through our 3-step sequential pipeline."

Provide a clear, structured extraction of all contract data."""
)

# Step 2: Quality Validator
quality_validator = LlmAgent(
    model="gemini-2.0-flash",
    name="QualityValidator",
    description="Validates extraction quality and completeness",
    instruction="""You are a Contract Data Quality Validator.

Your task is to review the contract data extracted by the previous agent and assess its quality.

VALIDATION APPROACH:
1. Review the extracted contract data from the conversation above
2. Check data format and consistency
3. Assess overall data quality
4. Provide recommendations

VALIDATION CRITERIA:
• Completeness: Are all critical fields populated with meaningful data?
• Accuracy: Do the extracted values appear reasonable and consistent?
• Format: Are dates, amounts, and other structured data properly formatted?
• Consistency: Do related fields align logically (e.g., dates, payment terms)?

QUALITY LEVELS:
• EXCELLENT: Complete, accurate, well-formatted data (confidence > 0.9)
• GOOD: Minor gaps or formatting issues, generally reliable (confidence 0.7-0.9)
• FAIR: Some missing data or inconsistencies, needs review (confidence 0.5-0.7)
• POOR: Significant gaps, errors, or formatting problems (confidence < 0.5)

RECOMMENDATIONS:
• APPROVE: Data quality is sufficient for processing
• REVIEW: Data needs human review before processing
• REJECT: Data quality is too poor, requires re-extraction

FORMAT YOUR RESPONSE AS:
=== QUALITY VALIDATION REPORT ===

COMPLETENESS CHECK:
- Is Complete: [Yes/No]
- Missing Fields: [List any missing fields]

DATA QUALITY ASSESSMENT:
- Overall Quality: [EXCELLENT/GOOD/FAIR/POOR]
- Data Issues: [List any identified issues]
- Confidence Score: [0.0-1.0]

RECOMMENDATION: [APPROVE/REVIEW/REJECT]

VALIDATION SUMMARY:
[Provide detailed assessment of the extracted data quality]"""
)

# Step 3: Summary Reporter
summary_reporter = LlmAgent(
    model="gemini-2.0-flash",
    name="SummaryReporter",
    description="Creates comprehensive contract summary report",
    instruction="""You are a Contract Summary Report Generator.

Your task is to create a comprehensive summary report based on the contract data extracted and validated by the previous agents.

Review the conversation history to access:
• The original contract document provided by the user
• The structured contract data extracted by the ServiceDataExtractor
• The validation assessment provided by the QualityValidator

Use all this information to create your comprehensive summary.

FORMAT YOUR RESPONSE AS:
=== COMPREHENSIVE CONTRACT SUMMARY REPORT ===

CONTRACT TITLE: [Descriptive title based on service and parties]

EXECUTIVE SUMMARY:
[Concise overview of the contract purpose and scope]

KEY HIGHLIGHTS:
• [Most important contract point 1]
• [Most important contract point 2]
• [Most important contract point 3]
• [Additional highlights as needed]

FINANCIAL OVERVIEW:
[Summary of contract value, payment terms, and schedule]

TIMELINE OVERVIEW:
[Summary of key dates, duration, and important milestones]

RISK FACTORS:
• [Potential risk or concern 1]
• [Potential risk or concern 2]
• [Additional risks as identified]

NEXT ACTIONS:
• [Recommended follow-up action 1]
• [Recommended follow-up action 2]
• [Recommended follow-up action 3]
• [Additional actions as needed]

Provide a comprehensive, professional summary report."""
)

# Sequential Pipeline (Following ADK samples pattern exactly like LLM Auditor)
service_contract_pipeline = SequentialAgent(
    name="ServiceContractPipeline",
    description=(
        "Sequential pipeline for processing service contracts. "
        "Extracts contract data, validates the extraction quality, "
        "and generates a comprehensive summary report. "
        "Type 'sample' to use the built-in sample contract."
    ),
    sub_agents=[
        service_data_extractor,  # Step 1: Extract contract data
        quality_validator,       # Step 2: Validate data quality
        summary_reporter         # Step 3: Generate summary report
    ]
)

# For ADK compatibility, the root agent must be the SequentialAgent
root_agent = service_contract_pipeline
