import os
import pytest
from src.lib.MySQLclass import MySQLDatabase  # Assumi che il modulo contenente la classe sia chiamato 'your_module'


@pytest.fixture
def mysql_db():
    config_file_path = os.path.join('src', 'lib', 'config.py')
    db = MySQLDatabase(config_file_path=config_file_path)
    db.connect()
    yield db
    db.disconnect()

def test_read_config_exists(mysql_db):
    config = mysql_db.read_config()
    assert isinstance(config, dict)
    assert 'DB_CONFIG' in config

def test_read_config_not_exists():
    nonexistent_path = os.path.join('nonexistent', 'config.py')
    with pytest.raises(Exception, match="File di configurazione non trovato."):
        db = MySQLDatabase(config_file_path=nonexistent_path)
        db.read_config()

def test_connect_successful(mysql_db):
    assert mysql_db.connection.is_connected()

def test_execute_query(mysql_db):
    query = "INSERT INTO prenotazioni (id_user, name, phone, reserved_seats, day, time_slot) VALUES (%s, %s, %s, %s, %s, %s)"
    values1 = (1, 'pippo', '1234567890', '6', '2024-01-01', '1')
    mysql_db.execute_query(query, values1)
    #test multi
    values2 = [(2, 'topolino', '1234567890', '6', '2024-01-01', '2'),(3, 'pluto', '1234567890', '6', '2024-01-01', '3')]
    for value in values2:
        mysql_db.execute_query(query, value)
    # Add assertions based on your specific requirements or check the database state

def test_select_query(mysql_db):
    query = "SELECT * FROM prenotazioni WHERE id_user = %s"
    values = (1,)
    result = mysql_db.select_query(query, values)
    assert isinstance(result, list)
    # Add assertions based on your specific requirements or check the retrieved data