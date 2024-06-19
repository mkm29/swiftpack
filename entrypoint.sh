#!/bin/bash

echo Activate the virtual environment
. /venv/bin/activate
echo Install the wheel package
pip install *.whl
echo Starting Uvicorn server
uvicorn --port 8000 swiftpack.src.main:create_app --reload --workers 1 --host 0.0.0.0