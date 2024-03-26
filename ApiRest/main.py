from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector
import sys
sys.path.append('../DataBase')  # Agrega la ruta de la carpeta que contiene script1.py
from connection import Connection

host = 'localhost'
#user = input('User: ')
user = 'root'
#password = input('Password: ')
password = 'Ketesi43'
connection = Connection(host,user,password)
cursor, conn = connection.connection_to_database()

app = FastAPI()

# Define el esquema de datos para la inserción
class ItemCreate(BaseModel):
    dbname: str
    table: str
    id: int
    department: Optional[str] = None
    job: Optional[str] = None
    name: Optional[str] = None
    datetime: Optional[str] = None
    department_id: Optional[int] = None
    job_id: Optional[int] = None

# Define una ruta para insertar datos
@app.post("/items/")
def create_items(items :list[ItemCreate]):
    try:
        for item in items:
            if item.table == "departments":
                query = """
                INSERT INTO {dbname}.{table} (id, department) 
                VALUES (%s, %s)
                """
                values = (item.id, item.department)
                cursor.execute(query, values)
            elif item.table == "jobs":
                query = """
                INSERT INTO {dbname}.{table} (id, job) 
                VALUES (%s, %s)
                """
                values = (item.id, item.job)
                cursor.execute(query, values)
            elif item.table == "hired_employees":
                query = """
                INSERT INTO {dbname}.{table} (id, name, datetime, department_id, job_id) 
                VALUES (%s, %s, %s, %s, %s)
                """
                values = (item.id, item.name, item.datetime, item.department_id, item.job_id)
                cursor.execute(query, values)
        conn.commit()
        return {"message": f"{len(items)} items inserted successfully"}
    except mysql.connector.Error as err:
            return {"error": f"Error inserting items: {err}"}