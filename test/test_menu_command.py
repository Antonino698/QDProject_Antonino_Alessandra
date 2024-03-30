"""
TEST Menu Command
"""

from test.fixture import pytest,os,Image,BytesIO,ANY,AsyncMock
from src.menu_command import menu_command

@pytest.mark.asyncio
async def test_menu_command():
    """
    Menu Command Mock
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    # ARRANGE: Prepara lo stato iniziale e ottieni il percorso dell'immagine
    image_path = os.path.join("src", "media", "Menu.jpg")

     # ACT: Esegui l'azione, leggi l'immagine dal percorso
    with open(image_path, "rb") as file:
        image_data = file.read()
        image = Image.open(BytesIO(image_data))

        await menu_command(update_mock, context_mock)

    # ASSERT: Verifica che l'asserzione sia valida
    await context_mock.bot.send_message()
    expected_text = "Ecco il nostro menu:"
    await context_mock.bot.send_message(text=expected_text)
    assert image_data is not None
    assert image is not None
    assert image.size[0] > 0 and image.size[1] > 0
    context_mock.bot.sendPhoto.assert_called_once_with(update_mock.effective_chat.id, photo= ANY)
    assert update_mock.message.reply_text.called
