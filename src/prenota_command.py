from src.lib.lib import *




# Funzione chiamata quando il giorno viene inviato
async def prenota_day(update: Update, context: CallbackContext) -> int:
    
    #Mostra i pulsanti per selezionare una data nel formato "giorno, mese, anno"
    current_date = datetime.now()
    keyboard = []
    giorni = []
    for i in range(7):
        date = current_date + timedelta(days=i)
        formatted_date = italian_day[date.strftime('%A')] + ', ' + date.strftime('%d') + ' ' + italian_month[date.strftime('%B')] + ' ' + date.strftime('%Y')
        date_in_iso = date.strftime('%Y-%m-%d')  # Converti la data nel formato "anno-mese-giorno"
        giorni.append(date_in_iso)
        date_in_iso1 = datetime.strptime(date_in_iso, '%Y-%m-%d').strftime('%d-%m-%Y')
        date_again = f"manageDate@{date_in_iso}"
        keyboard.append([InlineKeyboardButton(formatted_date, callback_data=date_again)])

    reply_markup = InlineKeyboardMarkup(keyboard)
    #reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text("Per quale giorno desideri prenotare?\nSeleziona una data:", reply_markup=reply_markup)
    return BUTTON_HANDLER

async def prenota_time_slot(update: Update, context: CallbackContext) -> int:
    print(context.user_data)
    reserved_seats = context.user_data["reserved_seats"]
    reserved_data  = context.user_data["date"]
    try:
        db.connect()
        new_day = ("SELECT *,s2.id as id_time_slot FROM seats_occupation s1 JOIN max_seats_time_slot s2 on s1.time_slot = s2.id WHERE s1.day = %s and s1.free_seats >= %s")
        res = db.select_query(new_day, (reserved_data,reserved_seats))
        available_time_slots = [ f'{item["time_slot"]}#{item["id_time_slot"]}' for item in res ]
    finally:
        db.disconnect()

    if ( len(available_time_slots) == 0 ) :
        text = f"Non ci sono slot disponibili per {reserved_data}.\nRispondi con qualsiasi carattere per selezionare un'altra data."
        await update.message.reply_text(text)
        return DAY

    #Simulazione di fasce orarie disponibili 
    keyboard = [[InlineKeyboardButton(slot.split('#')[0], callback_data=f"manageTime@{slot}")] for slot in available_time_slots]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Perfetto! A che ora preferisci?\nScegli una fascia oraria:', reply_markup=reply_markup)
    return BUTTON_HANDLER