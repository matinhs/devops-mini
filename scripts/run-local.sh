#!/usr/bin/env bash
set -e
# activate venv if present
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

echo "Installing requirements (if needed)..."
pip install -r requirements.txt

echo "Starting app on 0.0.0.0:5000"
python app.py
