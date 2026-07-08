import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and Target
X = data[["income", "age"]]
y = data["approved"]

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")
