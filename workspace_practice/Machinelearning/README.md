# 🧠 Machinelearning Workspace Practice Guide

**Location:** Canada East | **Resource Group:** AI-102

## 📋 Workspace Overview
- **Purpose:** DP-100 Certification Practice
- **Compute:** Standard_DS11_v2 (Running)
- **Storage:** Azure Blob Storage
- **Region:** Canada East

## 🚀 Step-by-Step Practice Guide

### Phase 1: Environment Setup
#### Step 1.1: Connect to Workspace
```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
ml_client = MLClient(
    credential=credential,
    subscription_id="29f1cd2f-d0e2-413e-b913-1976b6924fa6",
    resource_group_name="AI-102",
    workspace_name="Machinelearning"
)
print("✅ Connected to Machinelearning workspace")
```

#### Step 1.2: Verify Resources
```python
# Check available computes
computes = list(ml_client.compute.list())
print(f"Available computes: {len(computes)}")
for compute in computes:
    print(f"- {compute.name} ({compute.type})")

# Check workspace info
workspace = ml_client.workspaces.get("Machinelearning")
print(f"Workspace: {workspace.display_name}")
print(f"Location: {workspace.location}")
```

### Phase 2: Data Management
#### Step 2.1: Create Data Asset
```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Upload sample dataset
my_data = Data(
    path="./sample_data.csv",
    type=AssetTypes.URI_FILE,
    description="Sample dataset for DP-100 practice",
    name="dp100-sample-data"
)

ml_client.data.create_or_update(my_data)
print("✅ Data asset created")
```

#### Step 2.2: Register Dataset
```python
# Register tabular dataset
from azure.ai.ml import Input

dataset = ml_client.data.get("dp100-sample-data", version="1")
print(f"Dataset registered: {dataset.name}")
```

### Phase 3: Model Development
#### Step 3.1: Create Training Script
```python
%%writefile train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv('data.csv')

# Prepare features
X = df.drop('target', axis=1)
y = df['target']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model.pkl')
print("Model trained and saved")
```

#### Step 3.2: Create Environment
```python
from azure.ai.ml.entities import Environment

env = Environment(
    name="dp100-env",
    description="Environment for DP-100 model training",
    conda_file={
        "channels": ["conda-forge", "defaults"],
        "dependencies": [
            "python=3.8",
            "pip",
            "pip": [
                "azureml-defaults",
                "scikit-learn",
                "pandas",
                "joblib"
            ]
        ]
    }
)

ml_client.environments.create_or_update(env)
print("✅ Environment created")
```

### Phase 4: Job Submission
#### Step 4.1: Configure Job
```python
from azure.ai.ml import command
from azure.ai.ml import Input, Output

# Configure job
job = command(
    code="./src",
    command="python train.py",
    environment="dp100-env@latest",
    compute="ml-compute-instance",
    inputs={
        "input_data": Input(
            type="uri_file",
            path="azureml://datastores/workspaceblobstore/paths/dp100-sample-data"
        )
    },
    outputs={
        "model_output": Output(
            type="uri_folder",
            path="azureml://datastores/workspaceblobstore/paths/model-outputs"
        )
    },
    experiment_name="dp100-experiment"
)

ml_client.jobs.create_or_update(job)
print("✅ Job submitted")
```

#### Step 4.2: Monitor Job
```python
# Get job status
job_name = job.name
job_status = ml_client.jobs.get(job_name)
print(f"Job status: {job_status.status}")

# Wait for completion
ml_client.jobs.stream(job_name)
```

### Phase 5: Model Management
#### Step 5.1: Register Model
```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

model = Model(
    path="azureml://datastores/workspaceblobstore/paths/model-outputs/model.pkl",
    name="dp100-logistic-regression",
    version="1",
    description="Logistic regression model trained on DP-100 dataset",
    type=AssetTypes.CUSTOM_MODEL
)

registered_model = ml_client.models.create_or_update(model)
print(f"✅ Model registered: {registered_model.name} v{registered_model.version}")
```

#### Step 5.2: Deploy Model
```python
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment

# Create endpoint
endpoint = ManagedOnlineEndpoint(
    name="dp100-endpoint",
    description="Endpoint for DP-100 model deployment"
)

ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Create deployment
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="dp100-endpoint",
    model=registered_model.id,
    instance_type="Standard_DS2_v2",
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(deployment).result()
print("✅ Model deployed")
```

## 📊 Practice Exercises

### Exercise 1: Data Exploration
1. Upload a dataset to Azure ML
2. Create data profiling reports
3. Visualize data distributions

### Exercise 2: Automated ML
1. Use AutoML for classification/regression
2. Compare model performances
3. Select best model

### Exercise 3: Pipeline Creation
1. Create ML pipelines
2. Add data preprocessing steps
3. Schedule pipeline runs

### Exercise 4: MLOps
1. Set up model monitoring
2. Implement A/B testing
3. Configure CI/CD pipelines

## 🎯 Next Steps
1. Complete all phases above
2. Experiment with different algorithms
3. Practice with real datasets
4. Deploy models to production

## 📚 Resources
- [Azure ML Documentation](https://docs.microsoft.com/azure/machine-learning/)
- [DP-100 Learning Path](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml/)
- [Sample Notebooks](https://github.com/Azure/azureml-examples)