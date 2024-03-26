import fastavro.schema
from fastavro import writer
from connection import Connection

class Backup:

    avro_schema_department = {
        "type": "record",
        "name": "NombreTabla",
        "fields": [
            {"name": "id", "type": ["null", "int"]},
            {"name": "department", "type": ["null", "string"]}
        ]
    }

    avro_schema_jobs = {
        "type": "record",
        "name": "NombreTabla",
        "fields": [
            {"name": "id", "type": ["null", "int"]},
            {"name": "job", "type": ["null", "string"]}
        ]
    }

    avro_schema_employee = {
        "type": "record",
        "name": "NombreTabla",
        "fields": [
            {"name": "id", "type": ["null", "int"]},
            {"name": "name", "type": ["null", "string"]},
            {"name": "datetime", "type": ["null", "string"]},
            {"name": "department_id", "type": ["null", "int"]},
            {"name": "job_id", "type": ["null", "int"]}
        ]
    }

    def __init__(self, cursor):
        self.cursor = cursor

    def generate_backup(self, dbname, table_name):
        try:
            # Consultar la tabla MySQL
            self.cursor.execute(f"SELECT * FROM {dbname}.{table_name}")
            rows = self.cursor.fetchall()
            # Crear una lista de diccionarios para almacenar los datos
            data = []

            if table_name == 'departments':
                for row in rows:
                    data.append({"id": row[0], "department": row[1]})
                with open(f"backups/{table_name}.avro", "wb") as out:
                    writer(out, fastavro.schema.parse_schema(self.avro_schema_department), data)
                    print(out)
            elif table_name == 'jobs':
                for row in rows:
                    data.append({"id": row[0], "job": row[1]})
                with open(f"backups/{table_name}.avro", "wb") as out:
                    writer(out, fastavro.schema.parse_schema(self.avro_schema_jobs), data)
                    print(out)
            elif table_name == 'hired_employees':
                for row in rows:
                    data.append({"id": row[0], "name": row[1], 'datetime': row[2], 'department_id': row[3], 'job_id': row[4]})
                with open(f"backups/{table_name}.avro", "wb") as out:
                    writer(out, fastavro.schema.parse_schema(self.avro_schema_employee), data)
                    print(out)
        except Exception as e:
            print(f"Error al generar el respaldo para la tabla {table_name}: {e}")
