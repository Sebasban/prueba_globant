from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys
sys.path.append('../DataBase')  # Agrega la ruta de la carpeta que contiene script1.py
from connection import Connection
import pandas as pd

app = FastAPI()

# Se establece la conexión a la base de datos
host = 'localhost'
user = 'root'
password = 'Ketesi43'
connection = Connection(host, user, password)
cursor, conn = connection.connection_to_database()

class ItemCreate(BaseModel):
    dbname: Optional[str] = None
    id: Optional[str] = None
    department_id: Optional[str] = None
    datetime: Optional[str] = None
    hired_employees: Optional[str] = None
    job_id: Optional[str] = None
    department: Optional[str] = None
    departments: Optional[str] = None
    jobs: Optional[str] = None
    job: Optional[str] = None

@app.get("/query1/")
def create_items(items: ItemCreate):
    # Consulta SQL con marcadores de posición %s
    query = """
        WITH tbl AS (
            SELECT
                {id},
                {department_id},
                {job_id},
                CONVERT(
                    CONCAT(
                        SUBSTRING({datetime}, 1, 4),
                        SUBSTRING({datetime}, 6, 2)
                    ),
                    UNSIGNED INTEGER
                ) AS ano_mes
            FROM
                {dbname}.{hired_employees}
        ),
        trimestre AS (
            SELECT
                {id},
                {department_id},
                {job_id},
                ano_mes,
                CASE 
                    WHEN ano_mes >= 202101 AND ano_mes <= 202103 THEN 'Q1'
                    WHEN ano_mes >= 202104 AND ano_mes <= 202106 THEN 'Q2'
                    WHEN ano_mes >= 202107 AND ano_mes <= 202109 THEN 'Q3'
                    WHEN ano_mes >= 202110 AND ano_mes <= 202112 THEN 'Q4'
                END AS trimestre
            FROM
                tbl
            WHERE
                ano_mes < 202201
        ),
        departments AS (
            SELECT
                t1.{id},
                t1.{department_id},
                t1.{job_id},
                t1.ano_mes,
                t1.trimestre,
                t2.{department}
            FROM
                trimestre t1
            LEFT JOIN
                {dbname}.{departments} t2 ON t1.{department_id} = t2.id
        ),
        jobs AS (
            SELECT 
                t1.{id},
                t1.{department_id},
                t1.{job_id},
                t1.ano_mes,
                t1.trimestre,
                t1.{department},
                t2.{job}
            FROM 
                departments t1 
            LEFT JOIN 
                {dbname}.{jobs} t2 ON t1.{job_id} = t2.{id}
        )
        SELECT
            {department},
            {job},
            SUM(CASE WHEN trimestre = 'Q1' THEN 1 ELSE 0 END) AS Q1,
            SUM(CASE WHEN trimestre = 'Q2' THEN 1 ELSE 0 END) AS Q2,
            SUM(CASE WHEN trimestre = 'Q3' THEN 1 ELSE 0 END) AS Q3,
            SUM(CASE WHEN trimestre = 'Q4' THEN 1 ELSE 0 END) AS Q4
        FROM
            {jobs} 
        GROUP BY
            {department}, {job}
        ORDER BY 1, 2
    """.format(
        id=items.id,
        department_id=items.department_id,
        job_id=items.job_id,
        datetime=items.datetime,
        dbname=items.dbname,
        hired_employees=items.hired_employees,
        department=items.department,
        departments=items.departments,
        jobs=items.jobs,
        job=items.job
    )
    print(query)

    cursor.execute(query)
    
    # Recuperar los resultados de la consulta
    results = cursor.fetchall()

    # Mostrar los resultados por consola
    for row in results:
        print(row)

    # Devuelve los resultados como respuesta
    return results

@app.get("/query2/")
def create_items_query2(items: ItemCreate):
    # Consulta SQL con marcadores de posición %s
    query = """
        WITH count as (
            SELECT
                COUNT(*) AS cnt
            FROM
                {dbname}.{hired_employees}
            WHERE
                SUBSTRING({datetime}, 1, 4) = '2021'
            GROUP BY
                {department_id}
        ),
        MeanHires AS (
            SELECT
                AVG(cnt) AS mean_hires
            FROM
                count
        ),
        DepartmentHireCounts AS (
            SELECT
                {department_id},
                COUNT(*) AS num_hires
            FROM
                {dbname}.{hired_employees}
            GROUP BY
                {department_id}
        ),
        DepartmentHires AS (
            SELECT
                t2.{id} AS department_id,
                t2.{department},
                t1.num_hires
            FROM
                DepartmentHireCounts t1
                INNER JOIN {dbname}.{departments} t2 ON t1.{department_id} = t2.{id}
        )
        SELECT
            t1.{department_id} AS id,
            t1.{department},
            t1.num_hires AS hired
        FROM
            DepartmentHires t1
            INNER JOIN MeanHires t2 ON t1.num_hires > t2.mean_hires
        ORDER BY
            t1.num_hires DESC
    """.format(
        id=items.id,
        department_id=items.department_id,
        datetime=items.datetime,
        dbname=items.dbname,
        hired_employees=items.hired_employees,
        department=items.department,
        departments=items.departments,
    )
    print(query)

    cursor.execute(query)
    
    # Recuperar los resultados de la consulta
    results = cursor.fetchall()

    # Mostrar los resultados por consola
    for row in results:
        print(row)

    # Devuelve los resultados como respuesta
    return results