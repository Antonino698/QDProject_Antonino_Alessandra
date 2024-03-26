from unittest.mock import AsyncMock

class MockAsyncMySQLDatabase:
    """
    Mock della classe MySQLDatabase per i test con AsyncMock
    """
    def __init__(self):
        """
        Inizializza il mock
        """
        self.connection = AsyncMock()

    async def read_config(self):
        """
        Simula il metodo read_config
        """
        return {'host': 'localhost', 'user': 'testuser', 'password': 'testpassword', 'database': 'testdb'}

    async def connect(self):
        """
        Simula il metodo connect
        """
        config = await self.read_config()
        self.connection = AsyncMock()  # Simula la connessione al database

    async def disconnect(self):
        """
        Simula il metodo disconnect
        """
        if self.connection:
            await self.connection.close()

    async def execute_query(self, query, values=None, multi=False):
        """
        Simula il metodo execute_query
        """
        cursor = await self.connection.cursor()
        if multi:
            await cursor.executemany(query, values)
        else:
            await cursor.execute(query, values)
            await self.connection.commit()
        await cursor.close()

    async def select_query(self, query, values=None):
        """
        Simula il metodo select_query
        """
        cursor = await self.connection.cursor(dictionary=True)
        try:
            await cursor.execute(query, values)
            result = await cursor.fetchall()
            return result
        finally:
            await cursor.close()
