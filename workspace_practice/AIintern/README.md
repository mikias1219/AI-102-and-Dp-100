# 🤖 AIintern Workspace Practice Guide

**Location:** Central US | **Resource Group:** ai-intern

## 📋 Workspace Overview
- **Purpose:** AI-102 Certification Practice
- **Compute:** Testcompute12345 (Compute Instance)
- **Storage:** Azure Blob Storage
- **Region:** Central US

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
    resource_group_name="ai-intern",
    workspace_name="AIintern"
)
print("✅ Connected to AIintern workspace")
```

#### Step 1.2: Verify Resources
```python
# Check available computes
computes = list(ml_client.compute.list())
print(f"Available computes: {len(computes)}")
for compute in computes:
    print(f"- {compute.name} ({compute.type})")

# Check workspace info
workspace = ml_client.workspaces.get("AIintern")
print(f"Workspace: {workspace.display_name}")
print(f"Location: {workspace.location}")
```

### Phase 2: Computer Vision Practice
#### Step 2.1: Upload Images
```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Upload image dataset
image_data = Data(
    path="./sample_images/",
    type=AssetTypes.URI_FOLDER,
    description="Sample images for AI-102 computer vision practice",
    name="ai102-image-dataset"
)

ml_client.data.create_or_update(image_data)
print("✅ Image dataset uploaded")
```

#### Step 2.2: Create Custom Vision Project
```python
# Use Azure Custom Vision or AutoML for image classification
from azure.cognitiveservices.vision.customvision import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient

# Initialize Custom Vision client
training_endpoint = "https://your-resource.cognitiveservices.azure.com/"
training_key = "your-training-key"

trainer = CustomVisionTrainingClient(training_key, training_endpoint)
```

### Phase 3: Natural Language Processing
#### Step 3.1: Text Analytics Setup
```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Initialize Text Analytics client
endpoint = "https://your-resource.cognitiveservices.azure.com/"
key = "your-text-analytics-key"

text_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
```

#### Step 3.2: Sentiment Analysis
```python
documents = [
    "I love this product!",
    "This is terrible.",
    "It's okay, nothing special."
]

response = text_client.analyze_sentiment(documents)
for doc in response:
    print(f"Text: {doc.sentences[0].text}")
    print(f"Sentiment: {doc.sentences[0].sentiment}")
    print(f"Confidence: {doc.sentences[0].confidence_scores}")
```

### Phase 4: Conversational AI
#### Step 4.1: QnA Maker Setup
```python
from azure.ai.qnamaker import QnAMakerClient
from azure.core.credentials import AzureKeyCredential

# Initialize QnA Maker client
endpoint = "https://your-resource.cognitiveservices.azure.com/"
key = "your-qna-key"

qna_client = QnAMakerClient(endpoint, AzureKeyCredential(key))
```

#### Step 4.2: Create Knowledge Base
```python
# Create knowledge base
kb_details = {
    "name": "AI-102-Knowledge-Base",
    "qna_pairs": [
        {
            "question": "What is Azure AI?",
            "answer": "Azure AI is a portfolio of AI services and tools."
        }
    ]
}

kb = qna_client.create_knowledgebase(kb_details)
print(f"Knowledge base created: {kb.knowledgebase_id}")
```

### Phase 5: Machine Learning Operations (MLOps)
#### Step 5.1: Model Monitoring Setup
```python
from azure.ai.ml.entities import ModelMonitoring
from azure.ai.ml.constants import MonitorSignalType

# Create model monitoring
monitoring = ModelMonitoring(
    name="ai102-model-monitor",
    model="azureml://registries/azureml/models/gpt-4o-mini/versions/1",
    signals=[
        {
            "type": MonitorSignalType.GENERATION_SAFETY_QUALITY,
            "metric_thresholds": {
                "self_harm": 0.1,
                "violence": 0.1
            }
        }
    ]
)

ml_client.model_monitoring.create_or_update(monitoring)
print("✅ Model monitoring configured")
```

## 📊 Practice Exercises

### Exercise 1: Computer Vision
1. Upload image dataset
2. Train custom vision model
3. Evaluate model performance
4. Deploy model for predictions

### Exercise 2: Natural Language Processing
1. Set up Text Analytics
2. Perform sentiment analysis
3. Extract key phrases
4. Recognize entities

### Exercise 3: Conversational AI
1. Create QnA knowledge base
2. Add custom questions/answers
3. Test conversational interface
4. Integrate with web app

### Exercise 4: Responsible AI
1. Implement content safety
2. Set up model monitoring
3. Configure fairness metrics
4. Create AI ethics guidelines

### Exercise 5: Azure OpenAI Integration
1. Connect to Azure OpenAI
2. Use GPT models for text generation
3. Implement prompt engineering
4. Create chat applications

## 🎯 Next Steps
1. Complete all AI-102 modules
2. Practice with real datasets
3. Deploy AI solutions
4. Implement monitoring and governance

## 📚 Resources
- [Azure AI Documentation](https://docs.microsoft.com/azure/ai-services/)
- [AI-102 Learning Path](https://docs.microsoft.com/learn/paths/develop-ai-solutions-azure/)
- [Azure OpenAI Samples](https://github.com/Azure/azure-openai-samples)