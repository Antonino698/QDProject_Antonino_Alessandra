"""
Menu
"""
import os
from typing import Any
from telegram import Update
from telegram.ext import CallbackContext

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

    return bot
