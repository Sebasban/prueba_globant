# Gestión de Base de Datos
Este proyecto consiste en un script de Python diseñado para facilitar la gestión de una base de datos relacional. El script proporciona funcionalidades para la conexión a la base de datos, modelado de datos y restauración de respaldo.

## Funcionalidades
Conexión a la Base de Datos: El script permite establecer una conexión a una base de datos MySQL utilizando credenciales proporcionadas por el usuario.

## Modelado de Datos: 
Se incluye la capacidad de crear y modificar la estructura de la base de datos mediante la creación, modificación y eliminación de tablas.

Carga de Datos desde Archivos CSV: También se ofrece la funcionalidad de cargar datos desde archivos CSV a la base de datos para poblar las tablas.

Restauración de Respaldo: El script incluye una función para restaurar respaldos de tablas específicas en la base de datos.

## Estructura del Proyecto
connection.py: Contiene la clase Connection que maneja la conexión a la base de datos.

create_schema.py: Contiene la clase Helper que proporciona métodos para el modelado de datos, como la creación y eliminación de tablas.

backup_restore.py: Contiene la clase Restore que se encarga de la restauración de respaldos de tablas en la base de datos.

resources: Directorio que almacena archivos CSV utilizados para cargar datos en la base de datos.

main.py: El archivo principal que ejecuta el script principal.

## Uso
Clona este repositorio en tu máquina local.

Asegúrate de tener instalado Python 3 y las dependencias necesarias, las cuales se pueden instalar mediante pip con el comando:
pip install -r requirements.txt

Ejecuta el script main.py para iniciar la gestión de la base de datos.

# API de Gestión de Base de Datos
Este proyecto consiste en una API desarrollada con FastAPI que facilita la inserción de datos en una base de datos MySQL. La API permite insertar datos en diferentes tablas de la base de datos de manera flexible.

## Funcionalidades
Inserción de Datos: La API permite insertar datos en tablas específicas de la base de datos utilizando solicitudes HTTP POST.
Estructura del Proyecto
main.py: Contiene la definición de la API utilizando FastAPI, así como las rutas y lógica necesarias para la inserción de datos en la base de datos.

connection.py: Contiene la clase Connection que maneja la conexión a la base de datos MySQL.

Uso
Clona este repositorio en tu máquina local.

Asegúrate de tener instalado Python 3 y las dependencias necesarias, las cuales se pueden instalar mediante pip con el comando:

Copy code
pip install -r requirements.txt
Ejecuta el script main.py para iniciar el servidor de la API.

Utiliza herramientas como cURL, Postman o tu navegador web para enviar solicitudes HTTP POST a la API con los datos que deseas insertar en la base de datos.

También puedes utilizar el script de solicitud request.py para enviar solicitudes HTTP POST a la API desde tu código Python.

Rutas de la API
Insertar Datos
URL: /items/
Método HTTP: POST
Descripción: Permite insertar datos en tablas específicas de la base de datos. Los datos se envían en el cuerpo de la solicitud en formato JSON.
Uso del Script de Solicitud
Puedes utilizar el siguiente script de Python para enviar solicitudes HTTP POST a la API y realizar inserciones en la base de datos:

python
Copy code
from requests import requests

url = "http://localhost:8000/items/"  # Suponiendo que la aplicación esté en ejecución en localhost en el puerto 8000

data = [
    {"dbname": "DBTG","table": "departments","id": 32,"department": "insercion3"},
    {"dbname": "DBTG","table": "departments","id": 32,"department": "insercion3"},
    {"dbname": "DBTG","table": "departments","id": 32,"department": "insercion3"},
    {"dbname": "DBTG","table": "jobs","id": 32,"job": "insercion2"},
    {"dbname": "DBTG","table": "jobs","id": 32,"job": "insercion2"},
    {"dbname": "DBTG","table": "jobs","id": 32,"job": "insercion2"},
    {"dbname": "DBTG","table": "hired_employees","id": 32,"name": "insercion2","datetime":"3:pm","department_id":45,"job_id":1},
    {"dbname": "DBTG","table": "hired_employees","id": 32,"name": "insercion2","datetime":"3:pm","department_id":45,"job_id":1},
    {"dbname": "DBTG","table": "hired_employees","id": 32,"name": "insercion2","datetime":"3:pm","department_id":45,"job_id":1},
]

response = requests.post(url,json=data)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Imprimir el contenido de la respuesta
    print(response.json())
else:
    print("Error:", response.status_code)
Asegúrate de ejecutar este script desde un entorno donde tengas instalado Python y el paquete requests.

# Notas
Asegúrate de tener los permisos adecuados para realizar operaciones de inserción en la base de datos.

Antes de ejecutar la API en un entorno de producción, asegúrate de entender las consecuencias de las operaciones que realizará, especialmente aquellas relacionadas con la modificación de datos en la base de datos.

Este proyecto está diseñado para ser utilizado con bases de datos MySQL. Asegúrate de tener acceso a una instancia de MySQL para probar la API.

