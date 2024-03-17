import os
import mysql.connector
from mysql.connector import Error



class MySQLDatabase:
    config_file_path = os.path.join('src', 'lib', 'config.py')
    def __init__(self, config_file_path=config_file_path):
        self.config_file_path = config_file_path
        self.connection = None
