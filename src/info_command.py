"""
View restaurant info
"""

from src.lib.lib import Update, ContextTypes

# Funzione di gestione del comando /info
# Mostra le informazioni generali del ristorante, quali:
# numero, orari e mappa(utilizzando google maps)
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    View restaurant info
    """
    context.user_data['stat'] = ""
    phone_number = "+391234567890"
    map_url = "https://www.google.com/maps?q=Latitudine,Longitudine"
    orari = (
        "Lun: Chiuso\n"
        "Mar: 19:30-02:00 (Special Nights Events)\n"
        "Mer: 19:30-24:00\n"
        "Gio: 19:30-02:00 (Special Nights Events)\n"
        "Ven: 19:30-24:00\n"
        "Sab: 19:30-02:00 (Special Nights Events)\n"
        "Dom: 19:30-02:00"
    )

    await update.message.reply_text(
        f"Orari di apertura:\n{orari}\n"
        f"Per chiamarci, clicca qui: tel:{phone_number}\n"
        f"Ci troviamo in Via del Ristorante, 12345, Città, clicca qui per raggiungerci: {map_url}"
    )
