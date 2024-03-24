from conection import conection

host = 'localhost'
user = input('User: ')
password = input('Password: ')
conection = conection(host,user,password)
cursor = conection.conection_to_database()
print(cursor)