from api.nyc_api import fetch_nyc_accidents
import pandas as pd

df = fetch_nyc_accidents(2000)

OUTPUT_PATH = "data/nyc_accidents_clean.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("💾 CSV exportado en:", OUTPUT_PATH)
