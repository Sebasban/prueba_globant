from conection import Conection

class Struct:

    def __init__(self, cursor) -> None:
        self.cursor = cursor

    def __create_database(self, db_name):
        try:
            self.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
            self.cursor.execute(f'USE {db_name}')
            print(f'Base de datos "{db_name}" creada correctamente')
        except:
            print('Error al crear la base de datos:')
            return db_name

    def __create_table(self, table_name, fields):
        try:
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({fields})')
            print(f'Tabla "{table_name}" creada correctamente')
        except:
            print('Error al crear la tabla:')

    def create_struct(self, db_name, departments_table, jobs_table, employees_table):
        try:
            # Crear la base de datos
            self.__create_database(db_name)

            # Crear tablas
            self.__create_table(departments_table, 'id INT, department VARCHAR(255)')
            self.__create_table(jobs_table, 'id INT, job VARCHAR(255)')
            self.__create_table(employees_table, 'id INT, name VARCHAR(255), datetime VARCHAR(255), department_id INT, job_id INT')

        except:
            print('Error al crear la estructura de la base de datos:')

#pipeline de conexion
host = 'localhost'
user = input('User: ')
password = input('Password: ')
conection = Conection(host,user,password)
cursor = conection.conection_to_database()
struct = Struct(cursor)
struct.create_struct('DBTG', 'departamentos', 'trabajos', 'empleados')

