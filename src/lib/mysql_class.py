"""
MYSQL CLASS
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0718
import mysql.connector
from src.lib.config import DB_CONFIG

class MySQLDatabase:
    """
    Class Methods
    """
    def __init__(self,data = None):
        """
        Costruttore
        """
        self.connection = None
        self.config = data
    def read_config(self):
        """
        Lettura da file config
        """
        config = DB_CONFIG
        if config:
            return config
        print("Configurazione non valida: il dizionario è"
                "vuoto o non è stato correttamente inizializzato")
        return None
    def connect(self):
        """
        connessione
        """
        config = self.read_config()
        if config:
            try:
                self.connection = mysql.connector.connect(**config)
            except mysql.connector.Error as err:
                print("Errore durante la connessione al database:", err)

    def disconnect(self):
        """
        disconnessione
        """
        if self.connection:
            self.connection.close()


    def execute_query(self, query, values=None, multi=False):
        """
        Query executor
        """
        cursor = self.connection.cursor()
        try:
            if multi:
                cursor.executemany(query, values)
            else:
                cursor.execute(query, values)
                self.connection.commit()
        except mysql.connector.Error as err:
            print("Errore durante l'esecuzione della query:", err)
        finally:
            cursor.close()

    def select_query(self, query, values=None):
        """
        Query selector
        """
        result = []
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Errore durante l'esecuzione della query di selezione:", err)
        finally:
            cursor.close()
        return []
