# Imagen base con Python
FROM python:3.12-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

# Exponemos el puerto del servidor FastAPI
EXPOSE 8001

# Comando para ejecución del servidor
CMD ["uvicorn", "api.predict_api:app", "--host", "0.0.0.0", "--port", "8001"]
