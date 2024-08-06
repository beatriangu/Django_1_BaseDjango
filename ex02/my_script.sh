#!/bin/bash

# Script to set up virtual environment and install requirements for Django

# Constants
VENV_NAME="django_venv"
REQUIREMENTS_FILE="requirements.txt"

# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing..."
    pip install virtualenv
    if [ $? -ne 0 ]; then
        echo "Failed to install virtualenv. Aborting."
        exit 1
    fi
fi

# Create virtual environment using virtualenv
echo "Creating virtual environment $VENV_NAME"
virtualenv $VENV_NAME

# Activate virtual environment
echo "Activating virtual environment $VENV_NAME"
source $VENV_NAME/bin/activate

# Install requirements
echo "Installing requirements from $REQUIREMENTS_FILE"
pip install -r $REQUIREMENTS_FILE

# Deactivate virtual environment
echo "Deactivating virtual environment $VENV_NAME"
deactivate

echo "Setup completed successfully."
