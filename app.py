import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import mysql.connector
from PIL import Image

# Cargar modelo preentrenado
modelo = tf.keras.applications.MobileNetV2(weights="imagenet")

# Conexión a la base de datos MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="mysql_db",
        user="root",
        password="root",
        database="inferencias_db"
    )

# Función para preprocesar imagen
def procesar_imagen(imagen):
    imagen = imagen.resize((224, 224))  # Redimensionar para el modelo
    imagen = np.array(imagen) / 255.0   # Normalizar valores
    imagen = np.expand_dims(imagen, axis=0)  # Agregar dimensión batch
    return imagen

# Función para predecir con el modelo
def predecir(imagen):
    imagen_procesada = procesar_imagen(imagen)
    predicciones = modelo.predict(imagen_procesada)
    etiqueta = tf.keras.applications.mobilenet_v2.decode_predictions(predicciones, top=1)[0][0][1]
    return etiqueta

# Guardar inferencia en MySQL
def guardar_inferencia(nombre, prediccion):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO inferencias (imagen, resultado) VALUES (%s, %s)", (nombre, prediccion))
    conexion.commit()
    conexion.close()

# Interfaz en Streamlit
st.title("Clasificación de Imágenes con MobileNetV2")
imagen_subida = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

if imagen_subida is not None:
    imagen = Image.open(imagen_subida)
    st.image(imagen, caption="Imagen Cargada", use_column_width=True)

    if st.button("Clasificar"):
        resultado = predecir(imagen)
        guardar_inferencia(imagen_subida.name, resultado)
        st.success(f"Predicción: {resultado}")
