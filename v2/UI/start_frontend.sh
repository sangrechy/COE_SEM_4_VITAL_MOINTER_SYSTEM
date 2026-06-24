#!/usr/bin/env bash
# Starts the React frontend for the Edge AI Wearable Health Monitor.
set -e

cd "$(dirname "$0")/frontend"

echo ""
echo "╔════════════════════════════════════════╗"
echo "║  Edge AI Wearable Health Monitor       ║"
echo "║  Frontend — React                      ║"
echo "╚════════════════════════════════════════╝"
echo ""

if [ ! -d "node_modules" ]; then
  echo "Installing npm packages..."
  npm install
fi

echo "Starting React dev server on http://localhost:3000"
echo ""
npm start
