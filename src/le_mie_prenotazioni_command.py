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
        pren_query= "SELECT t1.*,t2.time_slot as tms FROM prenotazioni t1 join max_seats_time_slot t2 on t1.time_slot = t2.id  WHERE t1.id_user= %s"
        res = db.select_query(pren_query, (user_id,))
        keyboard = []
        lista_prenotazioni = []
        for i, item in enumerate(res):
            context.user_data["id_prenotazione"]=res[i]['id']
            context.user_data["id_user"]=res[i]['id_user']
            context.user_data["name"]=res[i]['name']
            context.user_data["phone"]=res[i]['phone']
            context.user_data["reserved_seats"]=res[i]['reserved_seats']
            context.user_data["date"]=res[i]['day']
            context.user_data["time_slot"] =  res[i]['tms']
            context.user_data["time_slot_id"] = res[i]['time_slot']
            date_in_iso1 = datetime.strptime(str(context.user_data["date"]), '%Y-%m-%d').strftime('%d-%m-%Y')
            prenotazioni_message = (
                    f'ID_PRENOTAZIONE: {context.user_data["id_prenotazione"]}\n'
                    f'Nome: {context.user_data["name"]}\n'
                    f'Telefono: {context.user_data["phone"]}\n'
                    f'Posti prenotati: {context.user_data["reserved_seats"]}\n'
                    f'Giorno: {date_in_iso1}\n'
                    f'Ora: {context.user_data["time_slot"]}\n\n'
                ) 
            lista_prenotazioni.append(prenotazioni_message)

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
    finally:
        # Chiudi la connessione al database
        db.disconnect()


async def edit_booking(update, context):
    query= update.callback_query
    id_user = query.message.chat_id
    data = query.data
        
    # Assume che il campo 'data' abbia la forma 'valore1:valore2'
    parts = data.split('@')
    
    if len(parts) == 2:
        valore1 = parts[0]
        valore2 = parts[1]

        # gestisce la risposta in base al 'valore1'
        if valore1 == 'deleteSinglePren':
            print('deleteSinglePren')

#aggiungere parti del db mancanti