import requests

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

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)