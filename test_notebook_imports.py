#!/usr/bin/env python3
"""
Test script to verify all notebook imports work correctly
"""

print("Testing Azure ML Practice Environment...")
print("=" * 50)

try:
    # Azure ML imports
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential
    print("✅ Azure ML SDK imports successful")

    # Data Science imports
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("✅ Data Science libraries imports successful")

    # Test basic functionality
    np.random.seed(42)
    data = pd.DataFrame({
        'feature1': np.random.normal(0, 1, 100),
        'feature2': np.random.normal(5, 2, 100),
        'target': np.random.randint(0, 2, 100)
    })

    X = data[['feature1', 'feature2']]
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"✅ Model training test successful (Accuracy: {accuracy:.3f})")

    # Test plotting
    plt.figure(figsize=(8, 6))
    plt.scatter(data['feature1'], data['feature2'], c=data['target'], cmap='viridis', alpha=0.6)
    plt.title('Test Plot - Data Visualization Working')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.colorbar(label='Target')
    plt.savefig('test_plot.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("✅ Data visualization test successful (plot saved as test_plot.png)")

    print("\n🎉 ALL TESTS PASSED!")
    print("\nEnvironment is ready for DP-100 practice!")
    print("\nTo use in Jupyter notebook:")
    print("1. Open dp100_practice.ipynb")
    print("2. Select kernel: 'Azure ML Environment'")
    print("3. Run cells sequentially")

except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please run: source azure_ml_env/bin/activate && pip install -r requirements.txt")

except Exception as e:
    print(f"❌ Test Error: {e}")