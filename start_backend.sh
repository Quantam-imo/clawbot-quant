#!/bin/bash
# Auto-export Databento API key from .env and start backend
set -e

# Load .env variables
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Start backend
/workspaces/clawbot-quant/.venv/bin/python -m uvicorn backend.api.server:app --reload --host 0.0.0.0 --port 8000
