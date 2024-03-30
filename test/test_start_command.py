"""
modulo start command
"""

from test.fixture import ConversationHandler,pytest,AsyncMock
from src.start_command import start_command

@pytest.mark.asyncio
async def test_start_command_with_message():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    # Simula un oggetto Update con un messaggio
    update_mock.message.from_user.first_name = 'Mario Rossi'

    result = await start_command(update_mock, context_mock)

    # Aggiungi qui le asserzioni necessarie per verificare il comportamento atteso
    assert result == ConversationHandler.END

@pytest.mark.asyncio
async def test_start_command_with_callback_query():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    # Simula un oggetto Update con una callback query

    update_mock.message = None
    update_mock.callback_query.from_user.first_name = 'Mario Rossi'

    result = await start_command(update_mock, context_mock)

    # Aggiungi qui le asserzioni necessarie per verificare il comportamento atteso
    assert result == ConversationHandler.END
