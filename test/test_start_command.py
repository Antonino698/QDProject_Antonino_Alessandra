"""
modulo start command
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0621
# pylint: disable=W0718
# pylint: disable=R0801
from unittest.mock import AsyncMock,patch, ANY
import pytest
from src.lib.lib import *
from src.start_command import start_command

@pytest.fixture
def update_context_fixture():
    """
    fixture
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    return update_mock, context_mock

@pytest.mark.asyncio
async def test_start_command_with_message(update_context_fixture):
    """
    metodo
    """
    update_mock, context_mock = update_context_fixture
    # Simula un oggetto Update con un messaggio
    update_mock.message.from_user.first_name = 'Mario Rossi'

    result = await start_command(update_mock, context_mock)

    # Aggiungi qui le asserzioni necessarie per verificare il comportamento atteso
    assert result == ConversationHandler.END

@pytest.mark.asyncio
async def test_start_command_with_callback_query(update_context_fixture):
    """
    metodo
    """
    update_mock, context_mock = update_context_fixture
    # Simula un oggetto Update con una callback query

    update_mock.message = None
    update_mock.callback_query.from_user.first_name = 'Mario Rossi'

    result = await start_command(update_mock, context_mock)

    # Aggiungi qui le asserzioni necessarie per verificare il comportamento atteso
    assert result == ConversationHandler.END
