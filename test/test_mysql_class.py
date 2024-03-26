"""
mysql test class
"""
# pylint: disable=R0801
import unittest
from unittest.mock import MagicMock
from src.lib.mysql_class import MySQLDatabase
class TestMySQLDatabase(unittest.TestCase):
    """
    mysql test class metodi
    """
    def setUp(self):
        """
        setup mock
        """
        self.mock_connect = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_cursor.fetchall.return_value = [{'id': 1, 'name': 'Test'}]
        self.mock_connection = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.mock_connect.return_value = self.mock_connection

    def mock_mysql_connector(self, monkeypatch):
        """
        mock connector
        """
        monkeypatch.setattr('mysql.connector.connect', self.mock_connect)

    def test_connect(self):
        """
        mock connect
        """
        with unittest.mock.patch('mysql.connector.connect', self.mock_connect):
            db = MySQLDatabase(
                {'host': 'localhost',
                 'user': 'root',
                 'password': 'password',
                 'database': 'test_db'}
                 )
            db.connect()
            self.assertTrue(self.mock_connect.called)

    def test_select_query(self):
        """
        metodo
        """
        with unittest.mock.patch('mysql.connector.connect', self.mock_connect):
            db = MySQLDatabase(
                {'host': 'localhost',
                 'user': 'root',
                 'password': 'password',
                 'database': 'test_db'}
                 )
            db.connect()
            result = db.select_query("SELECT * FROM test_table")
            self.assertEqual(result, [{'id': 1, 'name': 'Test'}])

    def test_execute_query(self):
        """
        metodo
        """
        db = MySQLDatabase()
        db.connection = self.mock_connection

        query = "INSERT INTO test_table (name) VALUES (%s)"
        values = ("Test",)

        db.execute_query(query, values)

        self.mock_cursor.execute.assert_called_once_with(query, values)
        self.mock_connection.commit.assert_called_once()
