from src.lib.lib import *



# Dizionario di traduzione dei giorni della settimana in italiano
italian_day = {
    'Monday': 'Lunedì',
    'Tuesday': 'Martedì',
    'Wednesday': 'Mercoledì',
    'Thursday': 'Giovedì',
    'Friday': 'Venerdì',
    'Saturday': 'Sabato',
    'Sunday': 'Domenica'
}

# Dizionario di traduzione dei mesi in italiano
italian_month = {
    'January': 'Gennaio',
    'February': 'Febbraio',
    'March': 'Marzo',
    'April': 'Aprile',
    'May': 'Maggio',
    'June': 'Giugno',
    'July': 'Luglio',
    'August': 'Agosto',
    'September': 'Settembre',
    'October': 'Ottobre',
    'November': 'Novembre',
    'December': 'Dicembre'
}

## Funzioni di gestione del comando /prenota
# Permettono di prenotare un tavolo attraverso una procedura di domande-risposte ottenute in input dall'utente.
#le informazioni richieste sono rispettivamente: 
#   -nome prenotazione
#   -numero di telefono
#   -posti da prenotare
#   -giorno
#   -fascia oraria
#si conclude con il recap delle informazioni ottenute e con la possibilità di confermare o annullare la prenotazione prima di essere memorizzata nel sistema(db) 
async def prenota_start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Per effettuare la prenotazione mi servono alcune informazioni. Inserisci il nome per la prenotazione:')
    return NAME

# Funzione chiamata quando il nome viene inviato
async def prenota_name(update: Update, context: CallbackContext) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text(f'Grazie, {context.user_data["name"]}! Qual è il tuo numero di telefono?')
    return PHONE

# Funzione chiamata quando il numero di telefono viene inviato
async def prenota_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['phone'] = update.message.text
    await update.message.reply_text('Ottimo! Quanti posti desideri prenotare? Inserisci un numero compreso tra 1 e 10.')
    
    return RESERVED_SEATS

# Funzione chiamata quando il numero di posti viene inviato
async def prenota_reserved_seats(update: Update, context: CallbackContext) -> int:
    #context.user_data['reserved_seats'] = update.message.text
    user_input = update.message.text
    if not user_input.isdigit():
        await update.message.reply_text('Per favore, inserisci un numero non un carattere PAGLIACCIO.')
        return
    reserved_seats = int(user_input)
    #1 <= reserved_seats <= 10
    if reserved_seats < 1 or reserved_seats > 10: 
        await update.message.reply_text('Per favore, inserisci un numero valido di posti (da 1 a 10).')
        return
    
    context.user_data['reserved_seats'] = reserved_seats
    await update.message.reply_text(f'Bene! Il numero di posti selezionati è {context.user_data["reserved_seats"]}. Rispondi con un qualsiasi carattere per continuare...')
    return DAY