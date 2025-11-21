from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 📌 Ruta del modelo entrenado
MODEL_PATH = "models/nyc_accident_rf.pkl"

# 📦 Cargar el modelo al iniciar la API
try:
    model = joblib.load(MODEL_PATH)
    print("🔍 Modelo cargado correctamente")
except Exception as e:
    print("❌ Error cargando el modelo:", e)

# 🏁 Inicializar la API
app = FastAPI(title="NYC Accident Severity Prediction API")

# 🧾 Esquema de datos de entrada (request)
class AccidentInput(BaseModel):
    hour: int
    day_of_week: int
    number_of_persons_injured: int
    number_of_persons_killed: int
    number_of_pedestrians_injured: int
    number_of_motorist_injured: int
    borough: str

# 🎯 Endpoint de predicción
@app.post("/predict")
def predict_severity(data: AccidentInput):
    try:
        # Convertir entrada a DataFrame
        input_df = pd.DataFrame([data.model_dump()])

        # 🔐 FORZAR ORDEN EXACTO DE VARIABLES
        expected_features = [
            "hour",
            "day_of_week",
            "number_of_persons_injured",
            "number_of_persons_killed",
            "number_of_pedestrians_injured",
            "number_of_motorist_injured",
            "borough"
        ]
        input_df = input_df[expected_features]

        # 🔮 Realizar predicción
        pred = model.predict(input_df)[0]

        # 🟢 Respuesta amigable
        return {
            "severity_prediction": int(pred),
            "message": "1 = Severe Injury/Fatality, 0 = Non-severe"
        }

    except Exception as e:
        return {"error": str(e)}
