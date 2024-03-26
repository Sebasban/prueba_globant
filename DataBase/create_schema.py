import logging
from backup import Backup

class Helper:

    def __init__(self, cursor) -> None:
        self.cursor = cursor

    def __create_database(self, db_name):
        try:
            self.cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
            print(f'Base de datos "{db_name}" creada correctamente')
        except:
            logging.error(f'Error al crear la base de datos: {db_name}')
    
    def __drop_database(self, db_name):
        try:
            self.cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
            print(f'Base de datos "{db_name}" borrada correctamente')
        except:
            logging.error(f'Error al borrar la base de datos: {db_name}')

    def __create_table(self, db_name, table_name, fields):
        try:
            self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {db_name}.{table_name} ({fields})')
            print(f'Tabla "{table_name}" creada correctamente')
        except:
            logging.error(f'Error al crear la tabla: {table_name}')

    def __drop_table(self, db_name, table_name):
        try:
            self.cursor.execute(f'DROP TABLE IF EXISTS {db_name}.{table_name}')
            print(f'Tabla "{table_name}" borrada correctamente')
        except:
            logging.error(f'Error al borrar la tabla: {table_name}')
    
    def __data_insert(self, df, db_name, table_name, fields):
        try:
            df = df.fillna(999999)
            for _, row in df.iterrows():
                    values = tuple(row)
                    self.cursor.execute(f'INSERT INTO {db_name}.{table_name} ({fields}) VALUES {values}')
                    self.cursor.fetchall()
        except:
            logging.error(f'error al insertar datos en la tabla {table_name}')


    def create_db(self, db_name):
        self.__create_database(db_name)

    def drop_db(self, db_name):
        self.__drop_database(db_name)

    def create_table(self, db_name, table_name, fields):
        self.__create_table(db_name, table_name, fields)
    
    def drop_tables(self, db_name, table_name):
        self.__drop_table(db_name, table_name)

    def insert(self, df, db_name, table_name, fields):
        self.__data_insert(df,db_name, table_name, fields)
        backup = Backup(self.cursor)
        backup.generate_backup(db_name, table_name)

