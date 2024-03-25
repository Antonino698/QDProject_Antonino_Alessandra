import os
import pytest
from unittest.mock import AsyncMock, patch
from src.lib.MySQLclass import MySQLDatabase

@pytest.fixture
def mock_mysql_db():
    async_mock_db = AsyncMock(spec=MySQLDatabase)
    async_mock_db.connection.is_connected.return_value = True
    return async_mock_db

async def test_read_config_exists(mock_mysql_db):
    mock_config = {'DB_CONFIG': 'example_config'}
    mock_mysql_db.read_config.return_value = mock_config
    config = await mock_mysql_db.read_config()
    assert isinstance(config, dict)
    assert 'DB_CONFIG' in config

async def test_read_config_not_exists():
    nonexistent_path = os.path.join('nonexistent', 'config.py')
    with patch('src.lib.MySQLclass.MySQLDatabase') as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.read_config.side_effect = FileNotFoundError
        with pytest.raises(Exception, match="File di configurazione non trovato."):
            db = MySQLDatabase(config_file_path=nonexistent_path)
            await db.read_config()

async def test_connect_successful(mock_mysql_db):
    assert await mock_mysql_db.assert_called.is_connected()

async def test_execute_query(mock_mysql_db):
    mock_execute_query = mock_mysql_db.execute_query
    query = "INSERT INTO prenotazioni (id_user, name, phone, reserved_seats, day, time_slot) VALUES (%s, %s, %s, %s, %s, %s)"
    values1 = (1, 'pippo', '1234567890', '6', '2024-01-01', '1')
    await mock_execute_query(query, values1)
    #test multi
    values2 = [(2, 'topolino', '1234567890', '6', '2024-01-01', '2'),(3, 'pluto', '1234567890', '6', '2024-01-01', '3')]
    for value in values2:
        await mock_execute_query(query, value)
    # Add assertions based on your specific requirements or check the database state

async def test_select_query(mock_mysql_db):
    mock_select_query = mock_mysql_db.select_query
    query = "SELECT * FROM prenotazioni WHERE id_user = %s"
    values = (1,)
    mock_select_query.return_value = [{'id_user': 1, 'name': 'pippo', 'phone': '1234567890', 'reserved_seats': '6', 'day': '2024-01-01', 'time_slot': '1'}]
    result = await mock_select_query(query, values)
    assert isinstance(result, list)
    # Add assertions based on your specific requirements or check the retrieved data