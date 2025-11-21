import pandas as pd

INPUT_PATH = "data/nyc_accidents_clean.csv"
OUTPUT_PATH = "data/nyc_ml_ready.parquet"

def preprocess():
    print("📥 Cargando dataset...")
    df = pd.read_csv(INPUT_PATH)

    # Convertir fechas a datetime
    df["crash_date"] = pd.to_datetime(df["crash_date"], errors="coerce")

    # Crear variables de IA
    df["hour"] = pd.to_datetime(df["crash_time"], format="%H:%M", errors="coerce").dt.hour
    df["day_of_week"] = df["crash_date"].dt.dayofweek  # 0 = Monday

    # Variable objetivo (binary classification: accidentes graves)
    df["is_severe"] = (
        (df["number_of_persons_killed"] > 0) |
        (df["number_of_persons_injured"] > 1)
    ).astype(int)

    print("✨ Variables creadas → hour, day_of_week, is_severe")

    # Guardar como parquet para procesamiento en Spark
    df.to_parquet(OUTPUT_PATH, index=False)
    print(f"💾 Dataset guardado en {OUTPUT_PATH}")

if __name__ == "__main__":
    preprocess()
