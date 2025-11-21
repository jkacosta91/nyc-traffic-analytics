import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

# 📌 Load dataset
df = pd.read_parquet("data/nyc_ml_ready.parquet")

X = df[["hour", "day_of_week", "number_of_persons_injured"]]
y = df["is_severe"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🚀 Tracking experiment
with mlflow.start_run():

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # 📊 Log metrics and params
    mlflow.log_metric("accuracy", acc)
    mlflow.log_param("n_estimators", 100)

    # 💾 Save model
    mlflow.sklearn.log_model(model, "nyc_rf_model")

    print("🔗 Modelo registrado en MLflow")
    print(f"📊 Accuracy: {acc:.4f}")
