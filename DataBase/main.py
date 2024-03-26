from connection import Connection
from create_schema import Helper
import os
import pandas as pd

#ROUTE OF THE RESOURCES

######################s###################################
currently_path = os.path.dirname(os.path.abspath(__file__))
path_csv = os.path.join(currently_path, '..', 'resources')
###########################################################

#CONECTION

###########################################
host = 'localhost'
user = input('User: ')
password = input('Password: ')
connection = Connection(host,user,password)
cursor, _ = connection.connection_to_database()
helper = Helper(cursor)
##########################################

#DATA MODELING

################################################################################################################################
#helper.create_db('DBTG')
#helper.drop_db('DBTG')
helper.create_table('DBTG', 'departments', 'id INT, department VARCHAR(255)')
helper.create_table('DBTG', 'jobs', 'id INT, job VARCHAR(255)')
helper.create_table('DBTG', 'hired_employees', 'id INT, name VARCHAR(255), datetime VARCHAR(255), department_id INT, job_id INT')
#helper.drop_tables('DBTG','departments')
#helper.drop_tables('DBTG','jobs')
#helper.drop_tables('DBTG','hired_employees')

fields = {
          'departments':'id, department',
          'jobs':'id, job',
          'hired_employees':'id, name, datetime, department_id, job_id'
          }

for tables,values in fields.items():
    df = pd.read_csv(f'{path_csv}/{tables}.csv', sep = ';')
    helper.insert(df, 'DBTG', tables, values)
    connection.upgrade_database()
################################################################################################################################

#Backup restore
############################
#from backup_restore import Restore
#fields = {'departments':'id, department'}
#backup = Restore(cursor)
#backup.restore_table('DBTG', 'departments', 'id INT, department VARCHAR(255)', )
#backup.insert_data('departments', fields)
#connection.upgrade_database()
