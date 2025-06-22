#!/bin/bash
# Fast environment setup for ADK Data Extraction Tutorial
set -e

if ! command -v uv &> /dev/null; then
  echo "uv not found. Installing via pip..."
  pip install uv
fi

uv venv .venv
source .venv/bin/activate
uv pip install -e .[dev]

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env. Please edit it with your credentials."
fi

echo "✅ Environment ready. Activate with: source .venv/bin/activate"
