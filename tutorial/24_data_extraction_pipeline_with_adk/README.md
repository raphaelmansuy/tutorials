# ADK Data Extraction Tutorial

This package contains hands-on examples and production patterns for structured data extraction using Google ADK GenAI.

- See the main tutorial in `../../working/24-data-extraction-pipeline-with-adk.md` for step-by-step guidance.
- Use `uv` for fast, reproducible Python environments.

## Quickstart

```sh
uv venv .venv
source .venv/bin/activate
uv pip install -e .[dev]
cp .env.example .env  # Edit credentials
```

## Project Structure

- `src/adk_data_extraction/` — Main package code
- `src/adk_data_extraction/examples/` — Example scripts for each tutorial section
- `tests/` — Unit and integration tests
- `notebooks/` — Jupyter notebooks for exploration
