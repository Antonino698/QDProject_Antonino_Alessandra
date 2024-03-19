import pytest
from unittest.mock import AsyncMock,patch, ANY
from src.lib.lib import *
from src.info_command import info_command

@pytest.fixture
def update_context_fixture():
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    
    return update_mock, context_mock

@pytest.mark.asyncio
async def test_info_command(update_context_fixture):
    update_mock, context_mock = update_context_fixture

    # Mocking user information
    phone_number = "+391234567890"
    map_url = "https://www.google.com/maps?q=Latitudine,Longitudine"
    orari = "Lun: Chiuso\nMar: 19:30-02:00 (Special Nights Events)\nMer: 19:30-24:00\nGio: 19:30-02:00 (Special Nights Events)\nVen: 19:30-24:00\nSab: 19:30-02:00 (Special Nights Events)\nDom: 19:30-02:00"
    info= AsyncMock(phone=phone_number, map=map_url, orari=orari) 

    # Act
    # Patching attributes
    with patch.object(update_mock, "message", AsyncMock(risto_info=info)):
        # Run the info_command function
        result = await info_command(update_mock, context_mock)

    # Assert
    await context_mock.bot.send_message()
    expected_text = f'Orari di apertura:\n{orari}\nPer chiamarci, clicca qui: tel:{phone_number}\nCi troviamo in Via del Ristorante, 12345, Città, clicca qui per raggiungerci: {map_url}'
    await context_mock.bot.send_message(text=expected_text)

    result == ConversationHandler.END  
