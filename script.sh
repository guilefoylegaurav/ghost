#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 OPENAI_API_KEY"
    exit 1
fi

export OPENAI_API_KEY="$1"

venv_name="langchain_env"

if [ ! -d "$venv_name" ]; then
    python3 -m venv "$venv_name"
fi

source "$venv_name/bin/activate"

pip3 install -r requirements.txt


python3 main.py

deactivate
