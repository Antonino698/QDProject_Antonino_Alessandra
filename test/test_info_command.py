"""
modulo le mie prenotazioni command
"""
# pylint: disable=R0914
# pylint: disable=W0104
# pylint: disable=W0401
# pylint: disable=W0401
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0621
# pylint: disable=W0718
# pylint: disable=R0801
from test.fixture import *
from src.info_command import info_command
@pytest.mark.asyncio
async def test_info_command(update_context_fixture):
    """
    metodo
    """
    update_mock, context_mock = update_context_fixture

    # Mocking user information
    phone_number = "+391234567890"
    map_url = "https://www.google.com/maps?q=Latitudine,Longitudine"
    orari = ("Lun: Chiuso\n"
             "Mar: 19:30-02:00 (Special Nights Events)\n"
             "Mer: 19:30-24:00\n"
             "Gio: 19:30-02:00 (Special Nights Events)\n"
             "Ven: 19:30-24:00\n"
             "Sab: 19:30-02:00 (Special Nights Events)\n"
             "Dom: 19:30-02:00")
    info= AsyncMock(phone=phone_number, map=map_url, orari=orari)

    # Act
    # Patching attributes
    with patch.object(update_mock, "message", AsyncMock(risto_info=info)):
        # Run the info_command function
        result = await info_command(update_mock, context_mock)

    # Assert
    await context_mock.bot.send_message()
    expected_text = (f"Orari di apertura:\n{orari}\n"
                     "Per chiamarci, clicca qui: tel:{phone_number}\n"
                     "Ci troviamo in Via del Ristorante, 12345, Città,"
                     "clicca qui per raggiungerci: {map_url}")
    await context_mock.bot.send_message(text=expected_text)

    result == ConversationHandler.END
