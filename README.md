¿De qué trata este proyecto?
Este proyecto es una aplicación web que usa un modelo de Inteligencia Artificial (IA) para clasificar imágenes. El modelo que estamos usando se llama MobileNetV2 y ya está entrenado para reconocer diferentes objetos. La aplicación está hecha con Streamlit para que sea fácil de usar a través de tu navegador, y todo funciona dentro de contenedores Docker para facilitar su ejecución. Además, las predicciones que hace la IA se guardan en una base de datos MySQL que también está dentro de otro contenedor.

Herramientas que usamos
Python 3.9: Es el lenguaje que usamos para programar el proyecto.
Streamlit: Es una herramienta para crear aplicaciones web de manera rápida y fácil.
TensorFlow: Usamos esta librería para cargar el modelo de IA y hacer las predicciones.
MySQL: Es la base de datos donde guardamos las predicciones que hace la IA.
Docker & Docker Compose: Usamos Docker para poner todo en contenedores y Docker Compose para gestionar todo eso de forma sencilla.
¿Cómo está organizado el proyecto?
Aquí te explico qué hay en cada archivo importante:

├── app.py                # El archivo donde está el código principal de la app
├── Dockerfile            # Instrucciones para crear la imagen de Docker
├── docker-compose.yml    # Configuración de todos los servicios que necesitamos
├── requirements.txt      # Las librerías que necesitamos instalar
└── README.md             # Este archivo con la explicación
Cómo instalar y ejecutar el proyecto
Clonando el proyecto
Si aún no tienes el proyecto en tu computadora, puedes clonarlo con Git:

git clone https://github.com/guerrerito33/mi_proyecto_ml.git
cd mi_proyecto_ml
Ejecutar con Docker Compose
Para levantar todo lo que necesita el proyecto (como la app web y la base de datos), usa Docker Compose. Solo tienes que correr este comando:


docker-compose up --build
Esto va a construir y levantar todos los contenedores. Una vez que se termine, abre el navegador y ve a:

http://localhost:8501
Aquí podrás ver y usar la aplicación web.

Usar una imagen Docker preconstruida
Si prefieres no crear los contenedores desde cero, puedes descargar una imagen ya lista desde Docker Hub. Solo sigue estos pasos:

Descarga la imagen con este comando:
docker pull larazo2323/clasificador:latest
Luego, corre el contenedor de la imagen:

docker run -d --name mi_clasificador lazaro2323/clasificador:latest
Después de hacer esto, abre la app en tu navegador en:
http://localhost:8501
Cómo usar la aplicación
Subir una imagen: Simplemente haz clic en el botón para cargar una imagen desde tu computadora.
Clasificación: El modelo de IA te dirá qué objeto cree que está en la imagen (como perro, gato, etc.).
Guardar resultados: Los resultados de la clasificación se guardan automáticamente en la base de datos MySQL para que puedas verlos más tarde.
Ver las predicciones guardadas en MySQL
Si quieres ver qué predicciones se han guardado en la base de datos, sigue estos pasos:

Ingresa al contenedor de MySQL:
docker exec -it mi_proyecto_ml-mysql_db-1 mysql -uroot -proot 
Luego, selecciona la base de datos donde están las predicciones:

USE inferencias_db;
Para ver todas las predicciones almacenadas, solo escribe:
sql

SELECT * FROM inferencias;
Conclusión
¡Y eso es todo! Con estos pasos, ya tienes una aplicación web que puede clasificar imágenes usando IA, y todo está dentro de contenedores Docker para facilitar su ejecución. Ya sea que quieras usarlo en tu máquina o compartirlo, ¡el proceso es fácil y rápido!
