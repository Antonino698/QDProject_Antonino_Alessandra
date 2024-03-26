""""
add commands test module
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0621
# pylint: disable=W0718
import json
from unittest.mock import AsyncMock, patch
import pytest
from src import add_commands

@pytest.fixture
def update_context_fixture():
    """"
    fixture
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    return update_mock, context_mock

@pytest.mark.asyncio
async def test_add_commands(update_context_fixture):
    """"
    metodo
    """
    update_mock, context_mock = update_context_fixture


    # Mocking the response of the requests.get function
    with patch("src.add_commands.requests.get") as mock_get:
        mock_get.return_value = AsyncMock()

        # Executing the function
        await add_commands.add_commands(update_mock)

        # Assertions
        await context_mock.bot.send_message()
        expected_commands = [
            {"command": "start", "description": "avvia il bot"},
            {"command": "prenota", "description": "prenota un tavolo"},
            {"command": "le_mie_prenotazioni", "description": "visualizza/disdici prenotazione"},
            {"command": "menu", "description": "visualizza il menu"},
            {"command": "eventi", "description": "visualizza gli special nights events"},
            {"command": "info", "description": "visualizza le informazioni del ristorante"}
        ]
        await context_mock.bot.send_message(text=expected_commands)

        await context_mock.bot.send_message()
        expected_url = (
            f"https://api.telegram.org/botTOKEN/setMyCommands?commands={
                json.dumps(expected_commands)
                }")
        await context_mock.bot.send_message(text=expected_url)

        await context_mock.bot.send_message()
        expected_obj = [
            ("start", "avvia il bot"),
            ("prenota", "prenota un tavolo"),
            ("le_mie_prenotazioni", "visualizza/disdici prenotazione"),
            ("menu", "visualizza il menu"),
            ("eventi", "visualizza gli special nights events"),
            ("info", "visualizza le informazioni del ristorante")
        ]
        await context_mock.bot.send_message(text=expected_obj)
