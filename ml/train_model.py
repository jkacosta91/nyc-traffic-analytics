import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import mlflow
import mlflow.sklearn

def train():
    df = pd.read_parquet("data/nyc_ml_ready.parquet")

    X = df[["hour", "day_of_week", "number_of_persons_injured", "number_of_persons_killed",
            "number_of_pedestrians_injured", "number_of_motorist_injured", "borough"]]
    y = df["is_severe"]

    categorical = ["borough"]
    numerical = ["hour", "day_of_week", "number_of_persons_injured", "number_of_persons_killed",
                 "number_of_pedestrians_injured", "number_of_motorist_injured"]

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical),
            ('num', 'passthrough', numerical)
        ]
    )

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model.fit(X_train, y_train)
        mlflow.sklearn.log_model(model, "nyc_accident_model")

    joblib.dump(model, "models/nyc_accident_rf.pkl")
    print("\n Modelo guardado correctamente con preprocesamiento incluído ✔")

if __name__ == "__main__":
    train()
