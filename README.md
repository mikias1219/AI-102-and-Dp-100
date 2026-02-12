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
- **URL**: https://ml.azure.com/?wsid=/subscriptions/29f1cd2f-d0e2-413e-b913-1976b6924fa6/resourcegroups/AI-102/workspaces/Machinelearning
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

## Useful Azure ML CLI Commands

```bash
# List resources
az ml workspace show
az ml dataset list
az ml compute list
az ml experiment list
az ml model list

# Create compute instance (if needed via CLI)
az ml compute create --name my-compute-instance --type ComputeInstance --size Standard_DS11_v2
```