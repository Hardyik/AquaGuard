import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv('C:/Users/Hardik/OneDrive/Documents/Projects/AquaGuard/water_potability.csv')

# Fill missing values
df = df.fillna(df.mean())

# Features and Target
X = df.drop('Potability', axis=1)
y = df['Potability']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print("✅ Model Accuracy:", round(accuracy_score(y_test, pred)*100, 2), "%")

# Save model
joblib.dump(model, 'water_model.pkl')
print("✅ Model saved as water_model.pkl")