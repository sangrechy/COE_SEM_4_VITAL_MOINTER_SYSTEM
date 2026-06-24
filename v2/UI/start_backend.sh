#!/usr/bin/env bash
# Starts the FastAPI backend for the Edge AI Wearable Health Monitor.
set -e

cd "$(dirname "$0")/backend"

echo ""
echo "╔════════════════════════════════════════╗"
echo "║  Edge AI Wearable Health Monitor       ║"
echo "║  Backend — FastAPI + Bleak             ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check Python 3.8+
python3 --version

# Install dependencies if needed
if ! python3 -c "import fastapi" &>/dev/null; then
  echo "Installing Python dependencies..."
  pip3 install -r requirements.txt
fi

echo "Starting backend on http://localhost:8000"
echo ""
python3 main.py
