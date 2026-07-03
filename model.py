import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (you can replace with real dataset later)
data = pd.DataFrame({
    'income': [50000, 20000, 80000, 30000, 60000, 40000, 70000, 25000],
    'age': [25, 45, 30, 50, 35, 28, 40, 55],
    'approved': [1, 0, 1, 0, 1, 1, 1, 0]
})

# Features and target
X = data[['income', 'age']]
y = data['approved']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction function
def predict_approval(income, age):
    return model.predict([[income, age]])
