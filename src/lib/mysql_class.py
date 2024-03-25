"""
Classe DB MySQL
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
    Classe DB MySQL
    """
    def __init__(self):
        """
        Classe DB MySQL
        """
        self.connection = None

    def read_config(self):
        """
        Metodo
        """
        try:
            config = DB_CONFIG
            if not config:
                raise ValueError("Configurazione non valida: il dizionario "
                                 "è vuoto o non è stato correttamente inizializzato")
            return config
        except ValueError as exc:
            raise ValueError(f"Errore nella configurazione: {format(exc)}") from exc

    def connect(self):
        """
        Metodo
        """
        config = self.read_config()
        self.connection = mysql.connector.connect(**config)
        print("Connessione al database avvenuta con successo.")

    def disconnect(self):
        """
        Metodo
        """
        if self.connection:
            self.connection.close()
            print("Connessione al database chiusa.")

    def execute_query(self, query, values=None, multi=False):
        """
        Metodo
        """
        cursor = self.connection.cursor()
        if multi:
            cursor.executemany(query, values)
        else:
            cursor.execute(query, values)
            self.connection.commit()
        cursor.close()

    def select_query(self, query, values=None):
        """
        Metodo
        """
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            print("Query eseguita con successo.")
            return result
        finally:
            cursor.close()
