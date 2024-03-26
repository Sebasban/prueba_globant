import pandas as pd 
import os 
import fastavro
from create_schema import Helper

class Restore(Helper):

    def __init__(self, cursor) -> None:
        super().__init__(cursor)

    def restore_table(self, dbname, table_name, fields): 
        self.create_table(dbname, table_name, fields)

    def insert_data(self, table_name, fields):
        with open(f'backups/{table_name}.avro', 'rb') as f:
            avro_reader = fastavro.reader(f)
            data = [record for record in avro_reader]
        df = pd.DataFrame(data)
        df = df.fillna(999999)
        for tables,values in fields.items():
            self.insert(df, 'DBTG', tables, values)