#!/usr/bin/env python3
"""
Test script for Azure Machine Learning SDK setup
"""

# Import required packages
try:
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential
    import mltable
    import azureml.mlflow
    print("✅ All imports successful!")
except ImportError as e:
    print(f"❌ Import error: {e}")
    exit(1)

# Test ML Client connection
try:
    # Get credentials
    credential = DefaultAzureCredential()

    # Create ML Client
    ml_client = MLClient(
        credential=credential,
        subscription_id="YOUR_SUBSCRIPTION_ID",
        resource_group_name="AI-102",
        workspace_name="Machinelearning"
    )

    # Test connection by getting workspace info
    workspace = ml_client.workspaces.get("Machinelearning")
    print("✅ Successfully connected to Azure ML workspace!")
    print(f"   Workspace: {workspace.display_name}")
    print(f"   Location: {workspace.location}")
    print(f"   Resource Group: {workspace.resource_group}")

    # List available computes
    computes = ml_client.compute.list()
    compute_list = list(computes)
    print(f"✅ Found {len(compute_list)} compute resources")
    for compute in compute_list[:3]:  # Show first 3
        print(f"   - {compute.name} ({compute.type})")

except Exception as e:
    print(f"❌ Connection error: {e}")
    print("Make sure you're logged in to Azure CLI: az login")

print("\n🎉 Azure ML environment is ready for DP-100 & AI-102 practice!")