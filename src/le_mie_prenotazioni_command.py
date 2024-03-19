from src.lib.lib import *
from src.start_command import *

async def le_mie_prenotazioni_command(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_id=user.id
    # Connessione al database
    try:
        db.connect()
        messaggio = (
        "In questa sezione potrai visualizzare e/o cancellare le tue prenotazioni.\n"
        "Ecco l'elenco delle prenotazioni effettuate:\n"
        )
        await context.bot.send_message(chat_id=update.message.chat_id, text=messaggio)

        #da inserire la query

        keyboard = [[InlineKeyboardButton(f'Elimina prenotazione: {prenotazione["id"]}', callback_data=f'deleteSinglePren@{prenotazione["id"]}')] for prenotazione in res]

        delete_all_b = InlineKeyboardButton("Elimina tutte le prenotazioni", callback_data=f"deleteAllByUser@{user_id}")
        back_b = InlineKeyboardButton("Torna a /start", callback_data=f"reset@-1")
        keyboard.append([delete_all_b])
        keyboard.append([back_b])
        reply_markup = InlineKeyboardMarkup(keyboard)

        for prenotazioni_message in lista_prenotazioni:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=prenotazioni_message)

        msg = "Bene, queste sono le tue prenotazioni!\nCosa vuoi fare adesso?"
        await update.message.reply_text(msg, reply_markup=reply_markup)
        return BUTTON_HANDLER