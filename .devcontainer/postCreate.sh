#!/bin/bash
set -euo pipefail

# use a virtual environment
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
