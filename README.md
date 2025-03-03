# Clasificación de Imágenes con IA usando Docker y MySQL

## ¿De qué trata este proyecto?

Este proyecto es una **aplicación web** que utiliza un **modelo de Inteligencia Artificial (IA)** para clasificar imágenes. El modelo que estamos utilizando se llama **MobileNetV2**, y está entrenado para reconocer diferentes objetos. La aplicación está desarrollada con **Streamlit**, lo que facilita su uso a través de un navegador. Todo el proyecto está contenido dentro de **contenedores Docker**, lo que hace que sea fácil de ejecutar en cualquier máquina. Además, las **predicciones** realizadas por el modelo de IA se almacenan en una **base de datos MySQL**, que también se ejecuta en un contenedor separado.

## Herramientas que usamos

- **Python 3.9**: Lenguaje de programación utilizado para desarrollar el proyecto.
- **Streamlit**: Herramienta para crear aplicaciones web de forma rápida y sencilla.
- **TensorFlow**: Librería utilizada para cargar el modelo de IA y realizar las predicciones.
- **MySQL**: Base de datos donde se guardan las predicciones realizadas por la IA.
- **Docker & Docker Compose**: Docker se utiliza para poner todo el proyecto en contenedores, y Docker Compose facilita la gestión de estos contenedores.

## ¿Cómo está organizado el proyecto?

Aquí tienes la estructura de los archivos importantes del proyecto:

├── app.py # El archivo donde está el código principal de la aplicación ├── Dockerfile # Instrucciones para crear la imagen de Docker ├── docker-compose.yml # Configuración de todos los servicios necesarios ├── requirements.txt # Las librerías necesarias para el proyecto └── README.md # Este archivo con la explicación


## Cómo instalar y ejecutar el proyecto

### Clonando el proyecto

Si aún no tienes el proyecto en tu computadora, clónalo con Git con el siguiente comando:

git clone https://github.com/guerrerito33/mi_proyecto_ml.git
cd mi_proyecto_ml
Ejecutar con Docker Compose
Para levantar todos los servicios que necesita el proyecto (como la aplicación web y la base de datos), usa Docker Compose. Solo debes correr este comando:

docker-compose up --build
Este comando construirá y levantará todos los contenedores necesarios. Una vez que termine, abre el navegador y visita:

http://localhost:8501
Aquí podrás ver y usar la aplicación web.

Usar una imagen Docker preconstruida
Si prefieres no crear los contenedores desde cero, puedes descargar una imagen ya lista desde Docker Hub. Para ello, sigue estos pasos:

# Descarga la imagen con el siguiente comando:
docker pull larazo2323/clasificador:latest
Luego, corre el contenedor de la imagen descargada:
docker run -d --name mi_clasificador lazaro2323/clasificador:latest
Después de esto, abre la aplicación en tu navegador en:
http://localhost:8501
Cómo usar la aplicación
Subir una imagen: Haz clic en el botón para cargar una imagen desde tu computadora.
Clasificación: El modelo de IA te mostrará el objeto que cree que está en la imagen (por ejemplo, perro, gato, etc.).
Guardar resultados: Las predicciones generadas por el modelo se guardarán automáticamente en la base de datos MySQL para que puedas consultarlas más tarde.
Ver las predicciones guardadas en MySQL
Si quieres ver las predicciones que se han guardado en la base de datos, sigue estos pasos:

# Ingresa al contenedor de MySQL con este comando:
docker exec -it mi_proyecto_ml-mysql_db-1 mysql -uroot -proot
Luego, selecciona la base de datos donde se guardan las predicciones:
USE inferencias_db;
# Para ver todas las predicciones almacenadas, solo escribe:
SELECT * FROM inferencias;
# Conclusión
Este proyecto crea una aplicación con Streamlit que clasifica imágenes usando un modelo de IA y guarda los resultados en MySQL. Se usa Docker Compose para manejar la app y la base de datos de forma automatizada.
El objetivo es hacer que la clasificación de imágenes sea rápida y eficiente, permitiendo almacenar las predicciones para futuras consultas. Con esta estructura, la aplicación queda lista para escalar y mejorar según sea necesario.
