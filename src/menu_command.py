"""
Menu
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0718
from typing import Any
from telegram import Update
from telegram.ext import CallbackContext
from src.lib.lib import *

async def menu_command(update: Update, context: CallbackContext,
                       bot: Any = None) -> None:
    """
    Menu
    """
    # Implementa la logica per visualizzare il menu
    await update.message.reply_text("Ecco il nostro menu:")
    image_path = os.path.join("src", "media", "Menu.jpg")

    # Invia la foto utilizzando il bot
    with open(image_path, 'rb') as photo_file:
        await context.bot.sendPhoto(update.effective_chat.id,
                                    photo=photo_file)
