# ADK Data Extraction Tutorial

This package contains hands-on examples and production patterns for structured data extraction using Google ADK GenAI.

- See the main tutorial in `../../working/24-data-extraction-pipeline-with-adk.md` for step-by-step guidance.
- Use `uv` for fast, reproducible Python environments.

## Features

- **Basic Contact Extraction**: Extract structured contact information from unstructured text
- **Legal Document Analysis**: Advanced document processing with financial term extraction
- **Multi-Agent Pipeline**: Sophisticated document classification, specialized extraction, and quality validation
- **Production-Ready**: Full test coverage, linting, and CI/CD configuration
- **CLI Tools**: Ready-to-use command-line interfaces for common tasks

## Prerequisites

- Python 3.11 or higher
- Google Cloud Platform account with ADK access
- Google API key or service account credentials

## Quickstart

```sh
# Create and activate virtual environment
uv venv .venv
source .venv/bin/activate

# Install the package with development dependencies
uv pip install -e .[dev]

# Set up environment variables
cp .env.example .env
# Edit .env with your Google API credentials
```

## Environment Setup

Configure your `.env` file with the following variables:

```bash
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
PROJECT_ID=your-gcp-project-id
LOCATION=us-central1
LOG_LEVEL=INFO
```

## Usage

### Command Line Tools

The package provides CLI tools for common extraction tasks:

```sh
# Extract contact information from text
adk-extract-contacts

# Analyze legal documents
adk-analyze-legal
```

### Python API

```python
import asyncio
from adk_data_extraction.examples.basic_contact_extraction import extract_contacts
from adk_data_extraction.examples.multi_agent_pipeline import MultiAgentExtractionPipeline

# Extract contacts from text
result = asyncio.run(extract_contacts("Your text here..."))
print(result)

# Use multi-agent pipeline for sophisticated document processing
pipeline = MultiAgentExtractionPipeline()
result = asyncio.run(pipeline.process_document("Your document here..."))
print(f"Document Type: {result.classification.document_type}")
print(f"Confidence: {result.validation.confidence_score}")
```

## Examples

### 1. Basic Contact Extraction
Extract contact information from emails, business cards, or any text:

```python
from adk_data_extraction.examples.basic_contact_extraction import extract_contacts
result = asyncio.run(extract_contacts("Hi, I'm John at john@acme.com"))
```

### 2. Legal Document Analysis
Analyze contracts, agreements, and legal documents:

```python
from adk_data_extraction.examples.legal_document_analysis import analyze_legal_document
result = asyncio.run(analyze_legal_document("path/to/contract.txt"))
```

### 3. Multi-Agent Pipeline
Sophisticated document processing with classification, specialized extraction, and validation:

```python
from adk_data_extraction.examples.multi_agent_pipeline import (
    MultiAgentExtractionPipeline,
    run_contract_example,
    run_invoice_example,
    run_general_document_example
)

# Complete pipeline demonstration
asyncio.run(run_contract_example())
asyncio.run(run_invoice_example())
asyncio.run(run_general_document_example())

# Or use the pipeline directly
pipeline = MultiAgentExtractionPipeline()
result = asyncio.run(pipeline.process_document("Your document content"))
```

## Project Structure

- `src/adk_data_extraction/` — Main package code
  - `examples/` — Example implementations
    - `basic_contact_extraction.py` — Contact extraction with Pydantic models
    - `legal_document_analysis.py` — Advanced document analysis
    - `multi_agent_pipeline.py` — Multi-agent document processing pipeline
- `tests/` — Unit and integration tests
- `test_multi_agent_pipeline.py` — Test suite for multi-agent examples
- `pyproject.toml` — Project configuration and dependencies
- `sample_contract.txt` — Sample data for testing
- `Makefile` — Development automation

## Development

### Testing

```sh
# Run all tests
pytest

# Run with coverage
pytest --cov=adk_data_extraction

# Run specific test types
pytest -m unit
pytest -m integration
```

### Code Quality

```sh
# Format code
ruff format src/ tests/

# Lint code
ruff check src/ tests/

# Type checking
pyright
```

### Optional Dependencies

Install additional features:

```sh
# Documentation tools
uv pip install -e .[docs]

# Jupyter notebook support
uv pip install -e .[jupyter]
```

## License

MIT License - see project configuration for details.
