import pytest
from unittest.mock import AsyncMock,patch, ANY
from src.lib.lib import *
from src.start_command import start_command

@pytest.fixture
def update_context_fixture():
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    
    return update_mock, context_mock

@pytest.mark.asyncio
async def test_start_command_with_message(update_context_fixture):
    update_mock, context_mock = update_context_fixture
    # Simula un oggetto Update con un messaggio
    update_mock.message.from_user.first_name = 'Mario Rossi'
    
    result = await start_command(update_mock, context_mock)

    # Aggiungi qui le asserzioni necessarie per verificare il comportamento atteso
    assert result == ConversationHandler.END  