"""
Modulo START
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0718
from src.lib.lib import *

## Funzione di gestione del comando /start.
# Messaggio di benvenuto e introduzione ai comandi del bot
async def start_command(update: Update, context: CallbackContext) -> int:
    """
    Modulo START
    """
    text = ("Benvenuto nel bot di prenotazione del ristorante Da Tony&Ale.\n"
            "Usa:\n/prenota per effettuare una prenotazione\n"
            "/le_mie_prenotazioni per visualizzare le tue prenotazioni\n/"
            "menu per visualizzare il menu\n"
            "/eventi per gli eventi settimanali\n"
            "/info per le informazioni sul ristorante.")
    if isinstance(update.message) is isinstance(None):
        user = update.callback_query.from_user
        pre_text = f'Ciao {user.first_name}!\n{text}'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=pre_text)
    else:
        user = update.message.from_user
        await update.message.reply_text(f'Ciao {user.first_name}!\n{text}')
    return ConversationHandler.END
