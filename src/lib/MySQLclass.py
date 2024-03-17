import os
import mysql.connector
from mysql.connector import Error



class MySQLDatabase:
    config_file_path = os.path.join('src', 'lib', 'config.py')
    def __init__(self, config_file_path=config_file_path):
        self.config_file_path = config_file_path
        self.connection = None

    def read_config(self):
        try:
            # Importa il modulo come un modulo Python
            config = {}
            with open(self.config_file_path, 'r') as file:
                exec(file.read(), config)
            return config
        except FileNotFoundError:
            raise Exception("File di configurazione non trovato.")
