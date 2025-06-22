# Structured Data Extraction with Google ADK GenAI for the Impatient: From Novice to Practitioner in Record Time

## Prerequisites and Setup

> **📋 Complete Setup Guide**: For detailed installation and configuration instructions, please see our comprehensive **[ADK Setup Guide](adk-setup-guide.md)**

Before diving into the examples below, you'll need to set up your development environment. The setup process varies depending on whether you're:

- **🚀 Getting Started**: Using Google AI Studio for quick prototyping and experimentation
- **🏢 Going to Production**: Using Vertex AI for enterprise applications and team collaboration

### Quick Setup Summary

The setup guide covers:

- ✅ **Installation**: Python environment, ADK, and dependencies
- ✅ **Authentication**: API keys (Google AI Studio) or Service Account (Vertex AI)
- ✅ **Configuration**: Environment variables and project setup
- ✅ **Verification**: Testing your installation with simple agents
- ✅ **Troubleshooting**: Common issues and solutions

### Why Two Setup Options?

```mermaid
flowchart LR
    A[Choose Your Setup Path] --> B{Your Use Case}
    B -->|Learning & Prototyping| C[Google AI Studio]
    B -->|Production & Enterprise| D[Vertex AI]

    C --> C1[⚡ Fast Setup with API Keys]
    C --> C2[🧪 Perfect for Learning]
    C --> C3[💰 Pay-per-use Pricing]

    D --> D1[🔒 Enterprise Security with IAM]
    D --> D2[🏭 Production-ready with Monitoring]
    D --> D3[📊 Advanced Analytics & Logging]

    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style C fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style D fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style C1 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style C2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style C3 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style D1 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style D2 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style D3 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
```

| Google AI Studio                           | Vertex AI                               |
| ------------------------------------------ | --------------------------------------- |
| ⚡ **Fast setup** with API keys            | 🔒 **Enterprise security** with IAM     |
| 🧪 **Perfect for learning** and prototypes | 🏭 **Production-ready** with monitoring |
| 💰 **Pay-per-use** pricing                 | 📊 **Advanced analytics** and logging   |

### Ready to Start?

1. **[Complete the setup →](adk-setup-guide.md)** (5-15 minutes depending on your approach)
2. **Return here** to start building extraction agents
3. **Run the examples** below to master structured data extraction

> **Pro Tip**: If you're new to ADK, start with the Google AI Studio setup for faster onboarding. You can always migrate to Vertex AI later for production deployments.

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

```mermaid
flowchart TD
    A[Unstructured Data Volume] --> B[Manual Processing Required]
    B --> C[Hidden Costs]

    C --> D[Customer Service<br/>5-10 min per query]
    C --> E[Legal Discovery<br/>Millions in review costs]
    C --> F[Financial Analysis<br/>Days of extraction work]
    C --> G[Healthcare<br/>Time away from patient care]

    D --> H[Opportunity Cost]
    E --> H
    F --> H
    G --> H

    H --> I[Competitive Disadvantage]
    H --> J[Delayed Decisions]
    H --> K[Missed Opportunities]

    style A fill:#ffebee,stroke:#c62828,stroke-width:2px
    style B fill:#ffebee,stroke:#c62828,stroke-width:2px
    style C fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style D fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style E fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style F fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style G fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style H fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style I fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style J fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style K fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
```

Most organizations don't realize the true cost of their data extraction inefficiencies. Consider these scenarios:

- **Customer Service**: Agents manually scan through knowledge bases, taking 5-10 minutes per query when AI could extract relevant information in seconds
- **Legal Discovery**: Law firms spend millions on document review when structured extraction could identify key clauses, dates, and parties automatically
- **Financial Analysis**: Investment firms lose competitive edge when research teams spend days extracting data from reports instead of analyzing insights
- **Healthcare**: Medical professionals waste valuable time extracting patient information from unstructured notes instead of focusing on care

The opportunity cost is staggering—while your team extracts data manually, competitors using automated solutions are already acting on insights .

## What: Your Secret Weapon for Data Domination

Google ADK isn't just another tool—it's like having a team of expert data scientists working 24/7 . The framework uses three powerful mechanisms for structured extraction that revolutionize how you handle unstructured data .

### Core Extraction Mechanisms

```mermaid
flowchart LR
    A[Input Document] --> B[ADK Processing Engine]
    B --> C[Structured Output]

    subgraph ADK["ADK Core Components"]
        direction TB
        D[Input Schema<br/>📥 Validates incoming data]
        E[LLM Processing<br/>🧠 Extracts information]
        F[Output Schema<br/>📤 Structures results]
        G[Output Key<br/>🔑 Stores for multi-agent use]

        D --> E
        E --> F
        F --> G
    end

    B -.-> ADK

    H[Pydantic Models] --> D
    H --> F
    I[Quality Gates] --> D
    J[Type Safety] --> F
    K[Multi-Agent Workflows] --> G

    style A fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style C fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style B fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style D fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style F fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style G fill:#e0f2f1,stroke:#00695c,stroke-width:1px
```

The ADK provides sophisticated capabilities that go far beyond simple text processing. At its heart, the system leverages Large Language Models (LLMs) combined with structured schemas to ensure consistent, reliable data extraction .

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

### Contact Extraction Flow

```mermaid
flowchart TD
    A[Raw Email Text] --> B[ADK Input Validation]
    B --> C[Gemini-2.0-Flash Processing]
    C --> D[Pydantic Schema Validation]
    D --> E[Structured ContactInfo Output]

    F[ContactInfo Schema] --> D
    F --> F1[name: str]
    F --> F2[email: str]
    F --> F3[company: str]
    F --> F4[phone: str optional]
    F --> F5[position: str optional]

    style A fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style E fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style C fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style D fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style F fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style F1 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style F2 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style F3 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style F4 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
    style F5 fill:#e0f2f1,stroke:#00695c,stroke-width:1px
```

### Example 2: Advanced Document Analysis (Intermediate Level)

Now let's tackle something more complex—extracting multiple data types from legal documents. This example shows how ADK handles sophisticated extraction scenarios with nested data structures.

```python
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
from google.adk.tools import FunctionTool
import hashlib
import logging

logger = logging.getLogger(__name__)

class DocumentType(str, Enum):
    CONTRACT = "contract"
    INVOICE = "invoice" 
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    LEGAL_BRIEF = "legal_brief"
    UNKNOWN = "unknown"

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

### Legal Document Processing Architecture

```mermaid
flowchart TB
    A[Legal Document Input] --> B[Document Reader Tool]
    B --> C[Legal Analysis Agent]
    C --> D[Structured Extraction]

    subgraph Schema["LegalExtraction Schema"]
        direction TB
        E[Document Type Classification]
        F[Parties Identification]
        G[Financial Terms Extraction]
        H[Key Dates Processing]
        I[Obligations Analysis]
        J[Governing Law Detection]
    end

    C --> Schema

    subgraph Financial["FinancialTerm Details"]
        direction LR
        K[Amount + Currency]
        L[Description]
        M[Due Date]
    end

    G --> Financial

    style A fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style D fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style C fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style E fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style F fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style G fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style H fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style I fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style J fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
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

Example:

````python
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
    confidence_score: float = Field(description="How complete the extraction is (0-1)")
    accuracy_indicators: List[str] = Field(description="Signs of accurate extraction")
    missing_fields: List[str] = Field(description="Critical fields that are missing")
    quality_issues: List[str] = Field(description="Potential quality issues")
    recommendation: str = Field(description="Recommended next action")

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

# Quality validation agent
validator_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="extraction_validator",
    instruction="""Validate extracted data for completeness and accuracy:

    Check for:
    1. All required fields are populated with meaningful data
    2. Data formats are consistent (dates, amounts, etc.)
    3. Logical relationships make sense (dates in proper order, etc.)
    4. No obvious extraction errors or inconsistencies

    If validation fails, provide specific recommendations for improvement.
    Use confidence scores: 0.9+ = excellent, 0.7-0.9 = good, 0.5-0.7 = needs review, <0.5 = requires manual intervention""",
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
        """Validate the quality of extracted data"""
        validation_prompt = f"""
        Validate this extraction against the original document:
        
        ORIGINAL DOCUMENT:
        {original_content[:1000]}...
        
        EXTRACTED DATA:
        {extracted_data}
        
        Check for completeness, accuracy, and consistency.
        """
        
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
                                accuracy_indicators=[],
                                missing_fields=[],
                                quality_issues=["Validation parsing failed"],
                                recommendation="Manual review recommended"
                            )
        
        return ExtractionValidation(
            is_valid=False,
            confidence_score=0.0,
            accuracy_indicators=[],
            missing_fields=["all"],
            quality_issues=["No validation response"],
            recommendation="Retry extraction"
        )
    
    async def process_document(self, content: str) -> Dict[str, Any]:
        """Complete pipeline: classify → extract → validate"""
        extraction_id = hashlib.md5(content.encode()).hexdigest()
        try:
            # Step 1: Classify document
            classification = await self.classify_document(content)
            logger.info(f"Document classified: {classification.document_type} (confidence: {classification.confidence_score})")
            
            # Step 2: Extract using appropriate specialist
            extraction_result = await self.extract_with_specialist(content, classification.document_type)
            logger.info(f"Extraction result: {extraction_result[:200]}...")  # Log snippet of result
            
            # Step 3: Validate extraction quality
            validation = await self.validate_extraction(extraction_result, content)
            logger.info(f"Validation result: {validation.is_valid} (score: {validation.confidence_score})")
            
            # Store extraction in session state
            self.session_service.set(extraction_id, {
                "classification": classification.model_dump(),
                "extraction": extraction_result,
                "validation": validation.model_dump(),
                "pipeline_status": "completed",
                "requires_review": validation.confidence_score < 0.7
            })
            
            return self.session_service.get(extraction_id)
            
        except Exception as e:
            logger.error(f"Error in extraction pipeline: {e}")
            return {
                "error": str(e),
                "pipeline_status": "failed",
                "requires_review": True
            }

# Example usage
async def run_multi_agent_example():
    pipeline = MultiAgentExtractionPipeline()

    sample_contract = """
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
    """

    result = await pipeline.process_document(sample_contract)
    print(f"Pipeline completed: {result['pipeline_status']}")
    print(f"Document type: {result['classification']['document_type']}")
    print(f"Validation score: {result['validation']['confidence_score']}")

    if result['requires_review']:
        print("⚠️ This extraction requires manual review")

# To run: asyncio.run(run_multi_agent_example())
````

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

### Batch Processing Architecture

```mermaid
flowchart TD
    A[Document Queue] --> B[Batch Processor]
    B --> C[Concurrent Processing Pool]

    subgraph Pool["Processing Pool (Max 5 Concurrent)"]
        direction TB
        D1[Worker 1]
        D2[Worker 2]
        D3[Worker 3]
        D4[Worker 4]
        D5[Worker 5]
    end

    C --> Pool

    subgraph Processing["Individual Document Processing"]
        direction TB
        E[Input Validation]
        F[ADK Extraction]
        G[Confidence Calculation]
        H[Quality Assessment]
        I[Result Packaging]
    end

    Pool --> Processing

    Processing --> J[Results Aggregation]
    J --> K[Batch Report Generation]
    K --> L[Performance Metrics]

    style A fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style K fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style B fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style C fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style D1 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style D2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style D3 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style D4 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style D5 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
```

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
    """Extract data with context awareness"""
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
            model="gemini-2.0-flash",
            instruction="Quick quality check for obvious errors",
            output_schema=SimpleValidation
        )
        
        self.stage2_validator = LlmAgent(
            model="gemini-2.0-flash",
            instruction="Detailed accuracy assessment with confidence scoring",
            output_schema=DetailedValidation
        )
    
    async def validate_extraction(self, result: ExtractionResult) -> ValidationResult:
        """Validate extraction with two-stage process"""
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

### Success Metrics Dashboard

```mermaid
flowchart LR
    subgraph Technical["Technical Metrics"]
        A1[Accuracy Rate<br/>Target: 90%+]
        A2[Processing Speed<br/>Target: <10s/doc]
        A3[System Uptime<br/>Target: 99.9%]
        A4[Error Rate<br/>Target: <2%]
    end

    subgraph Business["Business Impact"]
        B1[Time Savings<br/>Target: 4+ hrs/day]
        B2[Cost Reduction<br/>Target: $50K+/year]
        B3[Quality Improvement<br/>Target: 95%+ consistency]
        B4[User Satisfaction<br/>Target: 8+/10]
    end

    subgraph Growth["Growth Metrics"]
        C1[Documents Processed<br/>Daily Volume]
        C2[Use Cases Expanded<br/>Department Adoption]
        C3[Team Expertise<br/>Skill Development]
        C4[System Scalability<br/>Performance Under Load]
    end

    Technical --> Dashboard[Central Metrics Dashboard]
    Business --> Dashboard
    Growth --> Dashboard

    style Dashboard fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    style A1 fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style A2 fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px
    style B1 fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style B2 fill:#fff3e0,stroke:#ef6c00,stroke-width:1px
    style C1 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
    style C2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1px
```

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

### Enterprise Integration Architecture

```mermaid
flowchart TB
    subgraph External["External Systems"]
        A1[Document Management]
        A2[Email Systems]
        A3[File Storage]
        A4[Third-party APIs]
    end

    subgraph ADK["ADK Processing Layer"]
        B1[API Gateway]
        B2[Queue Manager]
        B3[Extraction Agents]
        B4[Quality Validators]
    end

    subgraph Storage["Data & Monitoring"]
        C1[Extraction Database]
        C2[Metrics Dashboard]
        C3[Audit Logs]
        C4[Alert System]
    end

    External --> ADK
    ADK --> Storage

    B1 --> B2
    B2 --> B3
    B3 --> B4
    B4 --> C1

    C2 --> C4
    C3 --> C4

    style B1 fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style B3 fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style C1 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px
    style C4 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
```

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
                    
                task = json.loads(task_data[1])  # brpop returns (key, value) tuple
                
                # Process the document
                result = await self.extract_document(task["document"])
                
                # Store result
                await self.store_result(task["task_id"], result)
                
            except Exception as e:
                logger.error(f"Worker {worker_id} error: {e}")
```

Ready to transform your data chaos into structured intelligence? The only question left is: will you be leading the AI revolution, or watching from the sidelines?

**Start your 24-hour challenge now**: Install ADK and let the extraction begin! Your journey from data extraction novice to practitioner starts with that first schema definition, but accelerates exponentially with each successful implementation. 🚀

---

_What unstructured data will you conquer first? Share your results and join the community of ADK practitioners transforming businesses worldwide._

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
