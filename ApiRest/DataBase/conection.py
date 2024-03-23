#importaciones
import mysql.connector
import json
import os
import logging

#conection con el servidor

class conection:

    def __init__(self,host, user, password) -> None:
        self.host = host
        self.user = user.lower()
        self.password = password
    
    def __get_credentials(self) -> str:
        path_json = os.path.join(os.path.dirname(__file__), '..', 'Extra', 'config.json')
        with open(path_json) as file_json:
            credentials = json.load(file_json)
        return credentials['user'], credentials['password']
    
    def __validate(self, user, password):
        if user == self.user and password == self.password:
            return True
        else:
            return False

    def conection_to_database(self):
        user, password = self.__get_credentials()
        try:
            if not self.__validate(user, password):
                logging.error('Wrong Credentials')
                return None
            else:
                conection = mysql.connector.connect(
                    host = self.host,
                    user = user,
                    password = password,
                )
                cursor = conection.cursor()
                logging.info('Successfull conection')
                print('Successfull conection')
                return cursor
        except mysql.connector.Error as e:
            logging.error(f'Database conection failed: {e}')


