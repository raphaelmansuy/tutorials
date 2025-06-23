.PHONY: help venv install test lint format clean run_basic_example run_legal_example run_multi_agent_example run_sequential_contract_pipeline test_multi_agent demo_multi_agent cli_contacts cli_legal cli_sequential_contract

help:
	@echo "ADK Data Extraction Tutorial Makefile"
	@echo "Available targets:"
	@echo "  venv      - Create virtual environment using uv"
	@echo "  install   - Install dependencies"
	@echo "  test      - Run tests"
	@echo "  lint      - Run linters (ruff, mypy)"
	@echo "  format    - Format code with black"
	@echo "  clean     - Remove .venv and __pycache__"
	@echo "  run_basic_example - Run basic_contact_extraction.py example"
	@echo "  run_legal_example - Run legal_document_analysis.py example"
	@echo "  run_multi_agent_example - Run multi_agent_pipeline.py example"
	@echo "  run_sequential_contract_pipeline - Run sequential_contract_pipeline.py example"
	@echo "  test_multi_agent - Run multi-agent pipeline test suite"
	@echo "  demo_multi_agent - Run simple multi-agent demo"
	@echo "  cli_contacts      - Run contact extraction via CLI"
	@echo "  cli_legal         - Run legal analysis via CLI"
	@echo "  cli_sequential_contract - Run sequential contract pipeline via CLI"

venv:
	uv venv .venv

install: venv
	. .venv/bin/activate && uv pip install -e .[dev]

test:
	. .venv/bin/activate && pytest

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

demo_multi_agent: install
	. .venv/bin/activate && python demo_multi_agent.py

cli_contacts: install
	. .venv/bin/activate && adk-extract-contacts

cli_legal: install
	. .venv/bin/activate && adk-analyze-legal

cli_sequential_contract: install
	. .venv/bin/activate && adk-sequential-contract
