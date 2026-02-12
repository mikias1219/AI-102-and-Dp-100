# AI-102 and DP-100 Practice Repository

This repository contains practice materials for Azure AI-102 and DP-100 certifications.

## Setup Instructions

### 1. Azure CLI Setup
```bash
# Login to Azure
az login

# Set default subscription (replace with your subscription ID)
az account set --subscription "29f1cd2f-d0e2-413e-b913-1976b6924fa6"

# Configure Azure ML workspace
az configure --defaults workspace=Machinelearning group=AI-102
```

### 2. Azure ML Studio Access
- **URL**: https://ml.azure.com/?wsid=/subscriptions/YOUR_SUBSCRIPTION_ID/resourcegroups/AI-102/workspaces/Machinelearning
- Create a **Standard_DS11_v2** compute instance in Compute → Compute instances

### 3. Local Development Environment

#### Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv azure_ml_env

# Activate virtual environment
source azure_ml_env/bin/activate  # On Windows: azure_ml_env\Scripts\activate
```

#### Install Azure ML SDK
```bash
# Install packages
pip install -r requirements.txt

# Or install individually:
pip install azure-ai-ml mltable azureml-mlflow
```

#### VS Code Setup
1. Open VS Code in this directory: `code .`
2. Install "Azure Machine Learning" extension from marketplace
3. Connect to your workspace via the extension

### 4. Verify Installation
```bash
# Activate environment and test imports
source azure_ml_env/bin/activate
python -c "import azure.ai.ml; import mltable; import azureml.mlflow; print('✅ All packages installed successfully!')"
```

## Contents

- Azure AI-102 exercises
- Azure DP-100 machine learning projects

## Project Files

- `requirements.txt` - Python dependencies for Azure ML
- `test_azure_ml.py` - Test script to verify Azure ML connection
- `dp100_practice.ipynb` - Jupyter notebook with DP-100 practice exercises
- `monitor_compute.py` - Script to monitor compute instance status
- `azure_ml_env/` - Virtual environment with all dependencies

## Useful Azure ML CLI Commands

```bash
# List resources
az ml workspace show
az ml dataset list
az ml compute list
az ml experiment list
az ml model list

# Monitor compute instance
python monitor_compute.py

# Test Azure ML connection
source azure_ml_env/bin/activate && python test_azure_ml.py
```

## Practice Exercises

1. **Run the test script**: Verify your Azure ML connection
2. **Monitor compute instance**: Use the monitoring script to check when it's ready
3. **Start practicing**: Open `dp100_practice.ipynb` and run through the exercises
4. **Experiment in Azure ML Studio**: Use the web interface for advanced features

## Your Environment Status

✅ **Azure CLI**: Logged in and configured
✅ **Azure ML Workspace**: Connected to "Machinelearning"
✅ **Compute Instance**: Standard_DS11_v2 (creating/running)
✅ **SDK Packages**: azure-ai-ml, mltable, azureml-mlflow installed
✅ **Virtual Environment**: azure_ml_env ready
✅ **Practice Resources**: Notebook and scripts created
✅ **Git Repository**: All changes committed and pushed