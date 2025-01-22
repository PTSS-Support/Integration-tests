#!/usr/bin/env python3
"""
Setup script to configure VS Code for the integration testing project.
This script creates necessary directories and configuration files.
"""
import os
import json
from pathlib import Path

def create_directory_if_not_exists(path):
    """Create a directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def write_json_file(path, content):
    """Write JSON content to a file."""
    with open(path, 'w') as f:
        json.dump(content, f, indent=4)

def setup_vscode_config():
    """Set up VS Code configuration for the project."""
    # Create .vscode directory
    create_directory_if_not_exists('.vscode')

    # VS Code settings
    vscode_settings = {
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
        "python.analysis.extraPaths": ["${workspaceFolder}/src"],
        "python.testing.pytestEnabled": True,
        "python.testing.unittestEnabled": False,
        "python.testing.nosetestsEnabled": False,
        "python.testing.pytestArgs": [
            "tests"
        ],
        "editor.formatOnSave": True,
        "python.formatting.provider": "black",
        "python.linting.enabled": True,
        "python.linting.flake8Enabled": True
    }
    write_json_file('.vscode/settings.json', vscode_settings)

    # Pyright configuration
    pyright_config = {
        "venvPath": ".",
        "venv": ".venv",
        "pythonVersion": "3.9",
        "analysis": {
            "extraPaths": ["src"]
        }
    }
    write_json_file('pyrightconfig.json', pyright_config)

def main():
    """Main setup function."""
    # Create virtual environment if it doesn't exist
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        os.system('python -m venv .venv')
    
    # Set up VS Code configuration
    print("Setting up VS Code configuration...")
    setup_vscode_config()
    
    print("\nSetup complete! To finish configuration:")
    print("1. Activate the virtual environment:")
    print("   - On Windows: .\\.venv\\Scripts\\activate")
    print("   - On Unix/MacOS: source .venv/bin/activate")
    print("2. Install required packages:")
    print("   pip install -e .")
    print("\nAfter these steps, restart VS Code for changes to take effect.")

if __name__ == "__main__":
    main()