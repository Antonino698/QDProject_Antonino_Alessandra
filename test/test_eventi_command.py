import os
from io import BytesIO
from PIL import Image
import pytest
from src.lib.lib import *
from unittest.mock import AsyncMock, patch, ANY
from src.eventi_command import eventi_command

@pytest.fixture
def update_context_fixture():
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    
    return update_mock, context_mock

@pytest.mark.asyncio
async def test_eventi_command(update_context_fixture):
    update_mock, context_mock = update_context_fixture
    # ARRANGE: Prepara lo stato iniziale e ottieni il percorso dell'immagine
    image_path = os.path.join("src", "media", "SpecialNightsEvents.jpeg")

     # ACT: Esegui l'azione, leggi l'immagine dal percorso
    with open(image_path, "rb") as file:
        image_data = file.read()
        image = Image.open(BytesIO(image_data))

        await eventi_command(update_mock, context_mock)
        
    # ASSERT: Verifica che l'asserzione sia valida
    await context_mock.bot.send_message()
    expected_text = "Ecco il nostri eventi settimanali:"
    await context_mock.bot.send_message(text=expected_text)
    assert image_data is not None
    assert image_path.lower().endswith('.jpg') or image_path.lower().endswith('.jpeg')
    assert image is not None
    assert image.size[0] > 0 and image.size[1] > 0
    context_mock.bot.sendPhoto.assert_called_once_with(update_mock.effective_chat.id, photo= ANY)
    assert update_mock.message.reply_text.called
