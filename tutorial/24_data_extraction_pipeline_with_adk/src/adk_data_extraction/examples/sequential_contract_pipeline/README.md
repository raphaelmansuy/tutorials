# Sequential Contract Pipeline

This example demonstrates a sequential multi-agent pattern for contract processing using Google ADK. It shows how to build a linear workflow where agents process documents in a predefined sequence, each building on the work of the previous agent.

## Overview

The Sequential Contract Pipeline provides specialized contract processing capabilities with:

- Sequential agent coordination pattern
- Contract-specific data extraction and enhancement
- Quality validation and comprehensive analysis
- Step-by-step processing workflow
- Incremental data improvement through multiple stages

## Architecture

### Core Components

1. **Main Sequential Coordinator** (`agent.py`)
   - Orchestrates the linear processing workflow
   - Manages sequential agent communication
   - Ensures proper workflow progression

2. **Sequential Processing Agents** (`sub_agents/`)
   - `contract_extractor`: Primary contract data extraction
   - `contract_enhancer`: Data enhancement and enrichment
   - `contract_validator`: Quality validation and assurance

3. **Contract Schemas** (`schemas/`)
   - `ContractData`: Core contract information schema
   - `ContractAnalysisResult`: Complete processing result
   - `ServiceContractData`: Specialized service contract schema

4. **Sample Data** (`data/`)
   - Sample contracts for testing and demonstration
   - Various contract types and complexity levels

## Key Features

### Sequential Processing Pattern
- **Linear Workflow**: Each agent builds on the previous agent's work
- **Incremental Enhancement**: Progressive improvement of extracted data
- **Quality Assurance**: Multi-stage validation and verification
- **Comprehensive Analysis**: Thorough contract review at each stage

### Contract Specialization
- **Contract-Specific Extraction**: Tailored for contract documents
- **Financial Terms Analysis**: Detailed payment and monetary terms
- **Legal Terms Processing**: Obligations, governing law, termination clauses
- **Party Identification**: Complete contracting party information

## Usage

### Basic Usage

```python
from sequential_contract_pipeline.agent import SequentialContractPipeline

# Initialize pipeline
pipeline = SequentialContractPipeline()

# Process a contract
contract_content = "Your contract content here..."
result = await pipeline.process_contract(contract_content)

print(f"Status: {result['processing_status']}")
print(f"Processing Time: {result['processing_time_ms']}ms")
```

### Running the Example

```bash
# From the sequential_contract_pipeline directory
python agent.py
```

### 3. Python CLI Script

Run the standalone Python CLI script:

```bash
# From project root
make python_cli_sequential

# Or directly from the agent directory  
cd src/adk_data_extraction/examples/sequential_contract_pipeline
python cli.py --text "CONTRACT: Service Agreement..."
python cli.py --file path/to/contract.txt
```

#### Python CLI Examples

```bash
# Process contract text
python cli.py --text "SERVICE AGREEMENT between ABC Corp and XYZ Ltd. Term: 12 months starting Jan 1, 2024."

# Process contract file
python cli.py --file sample_contract.txt

# Help
python cli.py --help
```

## Processing Workflow

The pipeline follows a strict sequential pattern:

### 1. Contract Extraction Stage
- **Primary Data Extraction**: Extract all key contract information
- **Party Identification**: Identify all contracting parties
- **Financial Terms**: Extract contract values, payment terms
- **Timeline Analysis**: Identify start dates, end dates, milestones
- **Legal Framework**: Governing law, jurisdiction, termination clauses

### 2. Contract Enhancement Stage
- **Data Enrichment**: Add missing details and context
- **Format Standardization**: Normalize dates, amounts, terms
- **Comprehensive Review**: Identify additional relevant information
- **Quality Improvement**: Enhance accuracy and completeness
- **Detail Expansion**: Complete party information, detailed obligations

### 3. Contract Validation Stage
- **Accuracy Verification**: Cross-reference with source document
- **Completeness Assessment**: Ensure all required elements present
- **Consistency Checking**: Verify logical consistency of extracted data
- **Quality Scoring**: Provide confidence and quality metrics
- **Final Review**: Comprehensive validation and recommendation

### 4. Results Integration
- **Sequential Compilation**: Integrate results from all stages
- **Comprehensive Summary**: Complete contract analysis report
- **Quality Assessment**: Overall processing quality metrics
- **Recommendations**: Suggested next actions or improvements

## Schema Definitions

### ContractData
- `parties`: All contracting parties
- `contract_value`: Total monetary value
- `currency`: Currency denomination
- `start_date`: Contract effective date
- `end_date`: Contract termination date
- `payment_terms`: Payment schedules and terms
- `key_obligations`: Primary responsibilities
- `governing_law`: Legal jurisdiction

### ContractAnalysisResult
- `contract_data`: Extracted and validated contract information
- `processing_status`: Workflow completion status
- `processing_time_ms`: Total processing duration
- `quality_score`: Quality assessment (0-1)
- `validation_notes`: Quality recommendations

## Sequential Pattern Benefits

### Progressive Enhancement
- Each stage builds on previous work
- Incremental improvement in data quality
- Comprehensive coverage through multiple passes
- Structured approach to complex extraction

### Quality Assurance
- Multi-stage validation and verification
- Cross-referencing between extraction stages
- Comprehensive quality assessment
- Error detection and correction

### Maintainability
- Clear separation of processing stages
- Easy to modify individual stages
- Straightforward debugging and monitoring
- Modular architecture for extensibility

## Extension Points

The pipeline can be extended with:

- Additional processing stages (risk assessment, compliance checking)
- Specialized contract type handlers (employment, real estate, etc.)
- Integration with legal databases and precedent systems
- Advanced validation rules and quality metrics
- Multi-language contract processing capabilities

## Use Cases

- **Contract Review Automation**: Automated initial contract analysis
- **Due Diligence Support**: Contract review for acquisitions
- **Compliance Monitoring**: Ongoing contract compliance verification
- **Legal Document Processing**: High-volume legal document analysis
- **Contract Database Population**: Structured data extraction for databases
- **Risk Assessment**: Contract risk identification and analysis

## Performance Considerations

- Sequential processing ensures data consistency
- Each stage builds incrementally on previous work
- Quality improves through multiple validation passes
- Processing time scales linearly with complexity
- Memory-efficient single-document processing model
