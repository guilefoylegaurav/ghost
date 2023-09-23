#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 OPENAI_API_KEY"
    exit 1
fi

export OPENAI_API_KEY="$1"

venv_name="myenv"

if [ ! -d "$venv_name" ]; then
    python3 -m venv "$venv_name"
fi

source "$venv_name/bin/activate"

pip3 install -r requirements.txt

deactivate

script_name="main.py"

current_dir=$(pwd)

bashrc_path="$HOME/.bashrc"
zshrc_path="$HOME/.zshrc"

echo "alias ghost=\"source $current_dir/$venv_name/bin/activate && python $current_dir/$script_name && deactivate\" " >> "$bashrc_path"

# Add the alias to .zshrc
echo "alias ghost=\"source $current_dir/$venv_name/bin/activate && python $current_dir/$script_name && deactivate\"" >> "$zshrc_path"

# Source the configuration files to apply the alias immediately
source "$bashrc_path"
source "$zshrc_path"

# Inform the user
echo "ghost has been set up successfully"