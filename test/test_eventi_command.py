"""
modulo eventi ristorante
"""
import os
from unittest.mock import ANY,AsyncMock
from io import BytesIO
import pytest
from PIL import Image
from src.eventi_command import eventi_command

@pytest.mark.asyncio
async def test_eventi_command():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    # ARRANGE: Prepara lo stato iniziale e ottieni il percorso dell'immagine
    image_path = os.path.join("src", "media", "SpecialNightsEvents.jpeg")

     # ACT: Esegui l'azione, leggi l'immagine dal percorso
    with open(image_path, "rb") as file:
        image_data = file.read()
        image = Image.open(BytesIO(image_data))

        await eventi_command(update_mock, context_mock)

    # ASSERT: Verifica che l'asserzione sia valida
    await context_mock.bot.send_message()

    await context_mock.bot.send_message(text="Ecco il nostri eventi settimanali:")
    assert image_data is not None
    assert image_path.lower().endswith('.jpg') or image_path.lower().endswith('.jpeg')
    assert image is not None
    assert image.size[0] > 0 and image.size[1] > 0
    context_mock.bot.sendPhoto.assert_called_once_with(update_mock.effective_chat.id, photo= ANY)
    assert update_mock.message.reply_text.called
