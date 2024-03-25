"""
Test module add command
"""
#pylint: disable=W0621
import json
from unittest.mock import AsyncMock, patch
import pytest
from telegram.ext import Application
from src import add_commands


@pytest.fixture
def app_fixture():
    """
    fixture
    """
    return Application.builder().token("TOKEN").build()


@pytest.mark.asyncio
async def test_add_commands(app_fixture):
    """
    add command mock
    """
    # Mocking the requests.get function
    with patch("src.add_commands.requests.get") as mock_get:
        # Mocking the response of requests.get
        mock_response = AsyncMock()
        mock_get.return_value = mock_response

        # Executing the function
        await add_commands.add_commands(app_fixture)
        # Assertions
        expected_commands = [
            {"command": "start", "description": "avvia il bot"},
            {"command": "prenota", "description": "prenota un tavolo"},
            {"command": "le_mie_prenotazioni", "description": "visualizza/disdici prenotazione"},
            {"command": "menu", "description": "visualizza il menu"},
            {"command": "eventi", "description": "visualizza gli special nights events"},
            {"command": "info", "description": "visualizza le informazioni del ristorante"}
        ]
        expected_url = (
            "https://api.telegram.org/botTOKEN/setMyCommands?commands="
            + json.dumps(expected_commands)
        )
        mock_get.assert_called_once_with(expected_url, timeout=30)
