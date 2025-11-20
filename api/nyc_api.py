import requests
import pandas as pd

# URL pública del dataset de colisiones
URL = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"

def fetch_nyc_accidents(limit=1000):
    params = {
        "$limit": limit,  # 👉 CORREGIDO: sin paréntesis
        "$order": "crash_date DESC"
    }

    response = requests.get(URL, params=params)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        raise Exception("❌ Error al consultar API de NYC")

    data = response.json()

    # Convertir a DataFrame
    df = pd.DataFrame(data)

    # Convertimos fechas a tipo datetime si existe crash_date
    if "crash_date" in df.columns:
        df["crash_date"] = pd.to_datetime(df["crash_date"])

    return df

if __name__ == "__main__":
    df = fetch_nyc_accidents(2000)
    print("\n📌 Muestras de datos NYC:")
    print(df.head())
    print(f"\n🚦 Total accidentes descargados: {len(df)}")
