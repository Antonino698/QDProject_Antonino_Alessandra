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

    
    def connect(self):
        #try:
            config = self.read_config()
            self.connection = mysql.connector.connect(**config['DB_CONFIG'])
            print("Connessione al database avvenuta con successo.")
        #except Error as e:
        #    print(f"Errore durante la connessione al database: {e}")
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Connessione al database chiusa.")

    def execute_query(self, query, values=None, multi=False):
        cursor = self.connection.cursor()
        #try:
        if multi:
            cursor.executemany(query, values)
        else:
            cursor.execute(query, values)
                
        self.connection.commit()
        print("Query eseguita con successo.")
        #except Error as e:
        #    print(f"Errore durante l'esecuzione della query: {e}")
        #finally:
        cursor.close()
    
    def select_query(self, query, values=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            print("Query eseguita con successo.")
            return result
        #except Error as e:
        #    print(f"Errore durante l'esecuzione della query: {e}")
        finally:
            cursor.close()
