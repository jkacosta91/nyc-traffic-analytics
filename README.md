# 🚦 NYC Traffic Accident Analysis & Prediction

## 📌 Objetivo

Pipeline real de datos para:

- 🔎 Análisis de accidentes en Nueva York
- 📊 Dashboard interactivo en Power BI
- 🤖 Modelo predictivo de zonas críticas de accidentes
- ⚙️ MLOps con Airflow, Docker y MLflow

### 🛠️ Tecnologías

- Python (API + ETL + IA)
- PostgreSQL (Docker)
- Power BI
- Docker
- Airflow (próximamente)
- MLflow (próximamente)

### 📡 Fuente de datos

Open Data NYC
<https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions/h9gi-nx95>

---

### 📦 Estructura del Proyecto

## ⚙️ Configuración rápida de Airflow (incluye Windows)

Airflow necesita que la ruta de la base de datos SQLite sea absoluta. En
Windows la ruta por defecto puede interpretarse como relativa (ejemplo del
error: `Cannot use relative path: sqlite:///C:\Users\<usuario>/airflow/airflow.db`).
Ejecuta el siguiente comando para inicializar Airflow con una ruta corregida:

```bash
python scripts/bootstrap_airflow.py
```

El script:

- Define `AIRFLOW_HOME` (usa `<repo>/airflow_home` si no está configurado).
- Fuerza la ruta de `airflow.db` a formato POSIX para que SQLite la trate como
  absoluta en Windows, macOS y Linux.
- Ejecuta `airflow db init` con esa configuración.

Si ya tienes `AIRFLOW_HOME` definido, se respetará y se usará esa carpeta para
la base de datos.
