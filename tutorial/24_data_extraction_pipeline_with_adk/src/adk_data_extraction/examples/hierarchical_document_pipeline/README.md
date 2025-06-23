# Hierarchical Document Pipeline

This example demonstrates a production-ready document processing system using Google ADK with advanced multi-agent coordination patterns.

## Architecture

The pipeline implements a hierarchical coordination pattern with the following components:

### Core Components

1. **Main Coordinator Agent** (`agent.py`)
   - Orchestrates the entire document processing workflow
   - Routes documents to appropriate specialist agents
   - Manages pipeline state and coordination

2. **Document Classifier** (`sub_agents/`)
   - Analyzes document content and structure
   - Determines document type (contract, invoice, agreement, etc.)
   - Recommends appropriate extraction strategy

3. **Specialist Agents** (`sub_agents/`)
   - `contract_specialist`: Handles contracts and legal agreements
   - `invoice_specialist`: Processes invoices and billing documents
   - `general_specialist`: Handles general documents and unknown types
   - `validation_specialist`: Performs quality assurance

4. **Schemas** (`schemas/`)
   - Type-safe data structures for all extraction results
   - Comprehensive validation schemas
   - Pipeline result aggregation

5. **Tools** (`tools/`)
   - State management utilities
   - Pipeline coordination functions
   - Logging and monitoring tools

## Key Features

- **Hierarchical Coordination**: Uses ADK's hierarchical agent pattern for complex workflows
- **Intelligent Routing**: Automatic document classification and routing to appropriate specialists
- **Quality Assurance**: Built-in validation and quality checking mechanisms
- **State Management**: Shared session state for seamless agent coordination
- **Error Handling**: Robust error handling and meaningful feedback
- **Monitoring**: Comprehensive logging and processing metrics

## Usage

### Basic Usage

```python
from hierarchical_document_pipeline.agent import HierarchicalDocumentPipeline

# Initialize pipeline
pipeline = HierarchicalDocumentPipeline()

# Process a document
document_content = "Your document content here..."
result = await pipeline.process_document(document_content)

print(f"Extraction ID: {result['extraction_id']}")
print(f"Status: {result['pipeline_status']}")
print(f"Processing Time: {result['processing_time_ms']}ms")
```

### Running the Example

```bash
# From the hierarchical_document_pipeline directory
python agent.py
```

## Quick Usage

### ADK Web UI (Recommended)
```bash
make adk_web
# Select "hierarchical_document_pipeline"
```

### ADK CLI  
```bash
make adk_test_hierarchical
```

### Python CLI Script
```bash
# From project root
make python_cli_hierarchical

# Or directly from the agent directory  
cd src/adk_data_extraction/examples/hierarchical_document_pipeline
python cli.py --text "DOCUMENT: ..."
python cli.py --file path/to/document.txt
```

#### Python CLI Examples
```bash
# Process document text
python cli.py --text "INVOICE #INV-2024-001 from Tech Solutions Inc. Amount: $2,500.00."

# Process document file
python cli.py --file sample_document.txt

# Help
python cli.py --help
```

## Pipeline Workflow

1. **Document Classification**
   - Analyzes document structure and content
   - Determines document type and complexity
   - Recommends appropriate extraction strategy

2. **Specialized Extraction**
   - Routes to contract, invoice, or general specialist
   - Extracts structured data using domain expertise
   - Returns schema-validated results

3. **Quality Validation**
   - Validates extraction completeness and accuracy
   - Provides confidence scores and quality metrics
   - Recommends next actions (approve, review, retry)

4. **Result Compilation**
   - Aggregates all pipeline results
   - Provides comprehensive extraction summary
   - Maintains audit trail and processing metadata

## Schema Definitions

### DocumentClassification
- `document_type`: Primary document category
- `complexity_level`: Processing difficulty assessment
- `confidence_score`: Classification confidence (0-1)
- `recommended_extractor`: Suggested specialist agent

### Extraction Schemas
- `ContractData`: Parties, terms, obligations, dates
- `InvoiceData`: Vendor, amounts, line items, payment terms
- `GeneralData`: Entities, dates, summary, action items

### ValidationSummary
- `is_valid`: Extraction quality assessment
- `confidence_score`: Extraction confidence (0-1)
- `completeness_score`: Data completeness (0-1)
- `issues`: Quality issues identified
- `recommendation`: Suggested next action

## ADK Best Practices Demonstrated

1. **Hierarchical Agent Pattern**: Main coordinator with specialized sub-agents
2. **Tool-based Coordination**: State management through shared tools
3. **Schema-driven Safety**: Type-safe data structures throughout
4. **Session Management**: Proper session lifecycle and state handling
5. **Error Handling**: Comprehensive error handling and recovery
6. **Monitoring**: Production-ready logging and metrics

## Extension Points

The pipeline can be extended with:

- Additional document type specialists
- Custom validation rules and quality metrics
- Integration with external systems (databases, APIs)
- Advanced preprocessing and post-processing steps
- Custom routing logic and decision trees

## Performance Considerations

- Parallel processing of independent pipeline stages
- Efficient state management for large documents
- Configurable timeout and retry mechanisms
- Resource monitoring and throttling capabilities
