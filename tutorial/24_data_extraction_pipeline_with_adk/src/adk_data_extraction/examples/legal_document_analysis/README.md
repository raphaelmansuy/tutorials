# Legal Document Analysis Pipeline

This example demonstrates advanced legal document analysis using Google ADK with specialized agents for comprehensive legal document processing.

## Overview

The Legal Document Analysis Pipeline provides enterprise-grade legal document processing capabilities, including:

- Expert legal document analysis and data extraction
- Financial terms and obligations identification
- Compliance verification and risk assessment
- Multi-agent coordination for complex legal workflows
- Comprehensive legal data validation and reporting

## Architecture

### Core Components

1. **Main Coordinator Agent** (`agent.py`)
   - Orchestrates the complete legal analysis workflow
   - Manages communication between specialized legal agents
   - Provides integrated analysis results

2. **Specialized Legal Agents** (`agents/`)
   - `legal_analyzer`: Primary legal document extraction and analysis
   - `contract_reviewer`: Detailed contract review and risk assessment
   - `compliance_checker`: Legal compliance verification and validation

3. **Legal Schemas** (`schemas/`)
   - `DocumentType`: Enumeration of legal document types
   - `FinancialTerm`: Financial terms and monetary amounts
   - `LegalExtraction`: Comprehensive legal data extraction schema
   - `LegalAnalysisResult`: Complete analysis result aggregation

## Key Features

### Legal Document Analysis
- **Comprehensive Data Extraction**: Parties, dates, financial terms, obligations
- **Document Type Classification**: Contracts, agreements, proposals, legal briefs
- **Financial Terms Analysis**: Amounts, payment schedules, penalties, currencies
- **Legal Obligations Mapping**: Responsibilities and requirements for each party

### Risk Assessment
- **Contract Risk Analysis**: Identification of potential legal risks
- **Clause Assessment**: Analysis of unusual or problematic provisions
- **Liability Review**: Evaluation of indemnification and liability terms
- **Enforceability Assessment**: Review of legal enforceability

### Compliance Verification
- **Regulatory Compliance**: Verification against applicable laws and regulations
- **Legal Formalities**: Checking for required legal disclosures and formalities
- **Industry Standards**: Assessment against industry-specific requirements
- **Statutory Compliance**: Verification of statutory requirements

## Usage

### Basic Usage

```python
from legal_document_analysis.agent import LegalDocumentAnalysisPipeline

# Initialize pipeline
pipeline = LegalDocumentAnalysisPipeline()

# Analyze a document
result = await pipeline.analyze_document("contract.pdf")

print(f"Analysis Status: {result['analysis_status']}")
print(f"Processing Time: {result['processing_time_ms']}ms")
```

### Running the Example

```bash
# From the legal_document_analysis directory
python agent.py

# Or with a specific document
python agent.py path/to/legal/document.pdf
```

## Quick Usage

### ADK Web UI (Recommended)
```bash
make adk_web
# Select "legal_document_analysis"
```

### ADK CLI  
```bash
make adk_test_legal
```

### Python CLI Script
```bash
# From project root
make python_cli_legal

# Or directly from the agent directory  
cd src/adk_data_extraction/examples/legal_document_analysis
python cli.py --text "LEGAL DOCUMENT: ..."
python cli.py --file path/to/legal_document.txt
```

#### Python CLI Examples
```bash
# Analyze legal document text
python cli.py --text "CONFIDENTIALITY AGREEMENT between parties. Confidential information includes trade secrets."

# Analyze legal document file
python cli.py --file contract.txt

# Help
python cli.py --help
```

## Analysis Workflow

1. **Document Intake and Validation**
   - Read and validate document content
   - Determine document type and complexity
   - Initialize analysis session

2. **Primary Legal Analysis**
   - Extract all parties and their roles
   - Identify key dates and deadlines
   - Analyze financial terms and obligations
   - Determine governing law and jurisdiction

3. **Contract Review (if applicable)**
   - Detailed contract term analysis
   - Risk assessment of obligations
   - Review of termination and renewal clauses
   - Analysis of dispute resolution mechanisms

4. **Compliance Verification**
   - Check regulatory compliance requirements
   - Verify legal formalities and disclosures
   - Assess industry-specific requirements
   - Identify compliance gaps or issues

5. **Integrated Results**
   - Combine all analysis results
   - Provide comprehensive legal summary
   - Generate risk assessment report
   - Recommend next actions

## Schema Definitions

### LegalExtraction
- `document_type`: Classification of legal document
- `parties`: All parties involved with roles
- `key_dates`: Critical dates and deadlines
- `financial_terms`: Monetary amounts and payment terms
- `obligations`: Legal responsibilities and requirements
- `governing_law`: Applicable jurisdiction and law
- `effective_date`: When document becomes effective
- `expiration_date`: Document expiration or termination

### FinancialTerm
- `amount`: Monetary value
- `currency`: Currency code (USD, EUR, etc.)
- `description`: Context and purpose of amount
- `due_date`: Payment deadline or schedule

## Advanced Features

### Multi-Agent Coordination
- Specialized agents for different legal aspects
- Coordinated workflow management
- Integrated result compilation
- Comprehensive quality assurance

### Risk Assessment
- Automated risk identification
- Clause-level risk analysis
- Liability and indemnification review
- Recommendation generation

### Compliance Checking
- Regulatory requirement verification
- Legal formality validation
- Industry standard compliance
- Gap analysis and reporting

## Extension Points

The pipeline can be extended with:

- Additional legal document types (regulations, statutes, etc.)
- Industry-specific compliance modules
- Integration with legal databases and case law
- Advanced risk scoring and modeling
- Multi-language legal document support
- Integration with document management systems

## Professional Use Cases

- **Contract Review**: Automated contract analysis and risk assessment
- **Due Diligence**: Legal document review for mergers and acquisitions
- **Compliance Monitoring**: Ongoing compliance verification and reporting
- **Legal Research**: Extraction of legal precedents and citations
- **Document Classification**: Automated legal document categorization
- **Audit Support**: Legal document review for audit purposes

## Performance and Scalability

- Efficient processing of large legal documents
- Parallel analysis for multiple documents
- Session-based state management
- Comprehensive error handling and recovery
- Detailed logging and audit trails
