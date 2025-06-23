.PHONY: help venv install test lint format clean demo run_basic_example run_legal_example run_multi_agent_example run_sequential_contract_pipeline test_multi_agent demo_multi_agent test_adk_discovery test_adk_structure adk_web adk_test_basic adk_test_sequential adk_test_hierarchical adk_test_legal cli_contacts cli_legal cli_sequential_contract python_cli_basic python_cli_demo python_cli_sequential python_cli_hierarchical python_cli_legal

help:
	@echo "ADK Data Extraction Tutorial Makefile"
	@echo ""
	@echo "🚀 Setup Commands:"
	@echo "  venv      - Create virtual environment using uv"
	@echo "  install   - Install dependencies"
	@echo ""
	@echo "🧪 Testing Commands:"
	@echo "  test                - Run pytest test suite"
	@echo "  test_adk_discovery  - Test ADK agent discovery structure"
	@echo "  test_adk_structure  - Verify all examples are ADK-compliant"
	@echo ""
	@echo "🏃 ADK Commands (Recommended):"
	@echo "  adk_web             - Start ADK web UI (interactive)"
	@echo "  adk_test_basic      - Test basic contact extraction with ADK"
	@echo "  adk_test_sequential - Test sequential contract pipeline with ADK"
	@echo "  adk_test_hierarchical - Test hierarchical document pipeline with ADK"
	@echo "  adk_test_legal      - Test legal document analysis with ADK"
	@echo ""
	@echo "🐍 Python CLI Examples:"
	@echo "  python_cli_basic      - Run basic contact extraction via Python CLI"
	@echo "  python_cli_demo       - Run Python CLI demonstration script"
	@echo "  python_cli_sequential - Info about sequential contract pipeline"
	@echo "  python_cli_hierarchical - Info about hierarchical document pipeline"
	@echo "  python_cli_legal      - Info about legal document analysis"
	@echo ""
	@echo "🔧 Development Commands:"
	@echo "  lint      - Run linters (ruff, mypy)"
	@echo "  format    - Format code with black"
	@echo "  clean     - Remove .venv and __pycache__"
	@echo ""
	@echo "📚 Legacy Examples:"
	@echo "  run_basic_example   - Run basic_contact_extraction.py example"
	@echo "  run_legal_example   - Run legal_document_analysis.py example"
	@echo "  run_multi_agent_example - Run multi_agent_pipeline.py example"
	@echo "  run_sequential_contract_pipeline - Run sequential_contract_pipeline.py example"
	@echo "  demo_multi_agent    - Run simple multi-agent demo"
	@echo "  cli_contacts        - Run contact extraction via CLI"
	@echo "  cli_legal           - Run legal analysis via CLI"
	@echo "  cli_sequential_contract - Run sequential contract pipeline via CLI"

venv:
	uv venv .venv

install: venv
	. .venv/bin/activate && uv pip install -e .[dev]

test:
	. .venv/bin/activate && pytest

# ADK Discovery and Structure Testing
test_adk_discovery: install
	@echo "🔍 Testing ADK agent discovery..."
	. .venv/bin/activate && cd src/adk_data_extraction/examples && python test_adk_discovery.py

test_adk_structure: test_adk_discovery
	@echo "✅ ADK structure verification complete"

# ADK Web Interface
adk_web: install test_adk_structure
	@echo "🌐 Starting ADK Web UI..."
	@echo "💡 Open http://localhost:8000 in your browser"
	@echo "📋 Select an example from the dropdown menu"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && adk web

# ADK Command Line Testing
adk_test_basic: install test_adk_structure
	@echo "🧪 Testing basic contact extraction with ADK..."
	@echo "ℹ️  This will start an interactive CLI. Type your test message and press Enter."
	@echo "📝 Try: 'Extract contacts from: Hi, I'm John Doe at Acme Corp. Email: john.doe@acme.com, Phone: 555-1234'"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	adk run basic_contact_extraction

adk_test_sequential: install test_adk_structure
	@echo "🧪 Testing sequential contract pipeline with ADK..." 
	@echo "ℹ️  This will start an interactive CLI. Type your test message and press Enter."
	@echo "📝 Try: 'Analyze this contract: SERVICE AGREEMENT between ABC Corp and XYZ Ltd. Term: 12 months starting Jan 1, 2024. Payment: \$$50,000 annual fee.'"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	adk run sequential_contract_pipeline

adk_test_hierarchical: install test_adk_structure
	@echo "🧪 Testing hierarchical document pipeline with ADK..."
	@echo "ℹ️  This will start an interactive CLI. Type your test message and press Enter."
	@echo "📝 Try: 'Process this invoice: INVOICE #12345 from Tech Solutions Inc. Amount: \$$2,500.00. Due: March 15, 2024.'"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	adk run hierarchical_document_pipeline

adk_test_legal: install test_adk_structure
	@echo "🧪 Testing legal document analysis with ADK..."
	@echo "ℹ️  This will start an interactive CLI. Type your test message and press Enter."
	@echo "📝 Try: 'Review this legal document: CONFIDENTIALITY AGREEMENT between parties. Confidential information includes trade secrets, business plans.'"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	adk run legal_document_analysis

# Test that we can list available agents
adk_list_agents: install test_adk_structure
	@echo "🔍 Listing available ADK agents..."
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	find . -name "agent.py" -exec dirname {} \; | sed 's|^\./||' | sort

# Demo command that shows available options
demo: install test_adk_structure adk_list_agents
	@echo "🎬 ADK Examples Demo"
	@echo ""
	@echo "Available agents for testing:"
	@$(MAKE) --silent adk_list_agents
	@echo ""
	@echo "To test interactively:"
	@echo "  make adk_web              # Web UI (recommended)"
	@echo "  make adk_test_basic       # Basic contact extraction CLI"
	@echo "  make adk_test_sequential  # Sequential contract pipeline CLI"
	@echo "  make adk_test_hierarchical # Hierarchical document pipeline CLI"
	@echo "  make adk_test_legal       # Legal document analysis CLI"
	@echo ""
	@echo "To test with Python CLI scripts:"
	@echo "  make python_cli_basic       # Basic contact extraction (Python)"
	@echo "  make python_cli_demo        # Python CLI demonstration"
	@echo "  make python_cli_sequential  # Info about sequential pipeline"
	@echo "  make python_cli_hierarchical # Info about hierarchical pipeline"
	@echo "  make python_cli_legal       # Info about legal document analysis"
	@echo ""
	@echo "💡 Note: ADK Web UI is the recommended interface for testing agents!"

lint:
	. .venv/bin/activate && ruff check src/ tests/
	. .venv/bin/activate && mypy src/

format:
	. .venv/bin/activate && black src/ tests/

clean:
	rm -rf .venv __pycache__ src/__pycache__ tests/__pycache__

run_basic_example: install
	. .venv/bin/activate && python -m adk_data_extraction.examples.basic_contact_extraction

run_legal_example: install
	. .venv/bin/activate && python -m adk_data_extraction.examples.legal_document_analysis

run_multi_agent_example: install
	. .venv/bin/activate && python -m adk_data_extraction.examples.multi_agent_pipeline

run_sequential_contract_pipeline: install
	. .venv/bin/activate && python -m adk_data_extraction.examples.sequential_contract_pipeline

test_multi_agent: install
	. .venv/bin/activate && python test_multi_agent_pipeline.py


cli_contacts: install
	. .venv/bin/activate && adk-extract-contacts

cli_legal: install
	. .venv/bin/activate && adk-analyze-legal

cli_sequential_contract: install
	. .venv/bin/activate && adk-sequential-contract

# Python CLI Examples
python_cli_basic: install test_adk_structure
	@echo "🐍 Running basic contact extraction via Python CLI..."
	@echo "💡 Example: Extract contacts from sample text"
	@echo "ℹ️  Note: This requires GOOGLE_API_KEY to be set in your environment"
	@echo "📝 Copy .env.example to .env and add your API key if needed"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	python contact_demo.py "Contact info: John Doe, Senior Developer at TechCorp. Email: john.doe@techcorp.com, Phone: +1-555-123-4567, Address: 123 Tech Street, Silicon Valley, CA 94000"

python_cli_demo: install test_adk_structure
	@echo "🐍 Running Python CLI demo script..."
	@echo "💡 This demonstrates how to use ADK programmatically"
	@echo "ℹ️  Note: This requires GOOGLE_API_KEY to be set in your environment"
	. .venv/bin/activate && cd src/adk_data_extraction/examples && \
	python contact_demo.py "Demo contact: Jane Smith, CTO at AI Corp. Email: jane@aicorp.com, Phone: 555-999-8888"

python_cli_sequential: install test_adk_structure
	@echo "🐍 Running sequential contract pipeline via Python CLI..."
	@echo "💡 Example: Process a sample contract"
	@echo "⚠️  Note: Complex CLI scripts have module import issues. Use 'make adk_web' instead."
	@echo "📋 The ADK web interface is the recommended way to test agents interactively."

python_cli_hierarchical: install test_adk_structure
	@echo "🐍 Running hierarchical document pipeline via Python CLI..."
	@echo "💡 Example: Process a sample invoice" 
	@echo "⚠️  Note: Complex CLI scripts have module import issues. Use 'make adk_web' instead."
	@echo "📋 The ADK web interface is the recommended way to test agents interactively."

python_cli_legal: install test_adk_structure
	@echo "🐍 Running legal document analysis via Python CLI..."
	@echo "💡 Example: Analyze a sample legal document"
	@echo "⚠️  Note: Complex CLI scripts have module import issues. Use 'make adk_web' instead."
	@echo "📋 The ADK web interface is the recommended way to test agents interactively."
