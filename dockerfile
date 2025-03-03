# Imagen base
FROM python:3.9

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copiar archivos
COPY requirements.txt .
COPY app.py .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de Streamlit
EXPOSE 8501

# Comando para ejecutar la app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
