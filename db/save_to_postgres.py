import pandas as pd
from api.nyc_api import fetch_nyc_accidents
from sqlalchemy import create_engine
import json

def clean_data(df):
    # Convertir columnas dict a texto JSON
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].apply(
                lambda x: json.dumps(x) if isinstance(x, dict) else x
            )
    return df

def save_to_db(limit=2000):
    print("📥 Descargando datos desde la API...")
    df = fetch_nyc_accidents(limit)

    print("🧹 Limpiando columnas con JSON...")
    df = clean_data(df)

    print("🛢 Conectando a PostgreSQL...")

    engine = create_engine("postgresql://postgres:postgres@localhost:5433/traffic_db")

    print("💾 Guardando datos en tabla nyc_accidents...")
    df.to_sql("nyc_accidents", engine, if_exists="replace", index=False)

    print("✔ Datos guardados correctamente en traffic_db.nyc_accidents")

if __name__ == "__main__":
    save_to_db(2000)
