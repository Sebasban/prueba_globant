import requests

def challenge_2_1():

    url = 'http://localhost:8000/query1/'

    data = {
        "dbname": "DBTG",
        "id": "id",
        "department_id": "department_id",
        "datetime": "datetime",
        "hired_employees": "hired_employees",
        "job_id": "job_id",
        "department": "department",
        "departments": "departments",
        "jobs": "jobs",
        "job": "job"
    }

    # Cambia la solicitud a una GET y envía los datos como parámetros de consulta
    response = requests.get(url, json=data)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error al realizar la solicitud:", response.status_code)

def challenge_2_2():
    url = 'http://localhost:8000/query2/'

    data = {
        "dbname": "DBTG",
        "id": "id",
        "department_id": "department_id",
        "datetime": "datetime",
        "hired_employees": "hired_employees",
        "job_id": "job_id",
        "department": "department",
        "departments": "departments",
        "jobs": "jobs",
        "job": "job"
    }

    # Cambia la solicitud a una GET y envía los datos como parámetros de consulta
    response = requests.get(url, json=data)

    if response.status_code == 200:
        print(response.json())
    else:
        print("Error al realizar la solicitud:", response.status_code)

challenge_2_1()