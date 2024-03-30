"""
modulo le mie prenotazioni command
"""

from test.fixture import AsyncMock
from unittest.mock import patch
import pytest
from src.info_command import info_command

@pytest.mark.asyncio
async def test_info_command():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    # Mocking user information
    phone_number = "+391234567890"
    map_url = "https://www.google.com/maps?q=Latitudine,Longitudine"
    orari = ("Lun1: Chiuso\n"
             "Mar1: 19:30-02:00 (Special Nights Events)\n"
             "Mer1: 19:30-24:00\n"
             "Gio1: 19:30-02:00 (Special Nights Events)\n"
             "Ven1: 19:30-24:00\n"
             "Sab1: 19:30-02:00 (Special Nights Events)\n"
             "Dom1: 19:30-02:00")
    info= AsyncMock(phone=phone_number, map=map_url, orari=orari)

    # Act
    # Patching attributes
    with patch.object(update_mock, "message", AsyncMock(risto_info=info)):
        # Run the info_command function
        await info_command(update_mock, context_mock)

    # Assert
    await context_mock.bot.send_message()
    expected_text = (f"Orari di apertura:\n{orari}\n"
                     "Per chiamarci, clicca qui: tel:{phone_number}\n"
                     "Ci troviamo in Via del Ristorante, 12345, Città,"
                     "clicca qui per raggiungerci: {map_url}")
    await context_mock.bot.send_message(text=expected_text)

    return True
