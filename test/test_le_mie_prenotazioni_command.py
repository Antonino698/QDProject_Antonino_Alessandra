import asyncio
import pytest
from src.lib.lib import *
from unittest.mock import AsyncMock, patch, ANY, MagicMock
from src.le_mie_prenotazioni_command import *
from src.lib.mysql_class import MySQLDatabase

from src.start_command import * #MBARE NON LO USI gemini
@pytest.fixture
def update_context_fixture():
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    query_mock = AsyncMock()
    bot_mock = AsyncMock()
    db_mock = AsyncMock()
    return update_mock, context_mock, query_mock, bot_mock, db_mock

@pytest.mark.asyncio
async def test_le_mie_prenotazioni_command(update_context_fixture):
    update_mock, context_mock, query_mock, bot_mock, db_mock = update_context_fixture
    
    # Crea un mock della connessione al database
    db_mock = AsyncMock()
    #user_id=123
    prenotazioni_di_prova=[
    {
        "id": 1,
        "id_user": 123,
        "name": "Mario Rossi",
        "phone": "123456789",
        "reserved_seats": 2,
        "day": "2024-02-22",
        "tms": "20:00",
        "time_slot": 1
    },
    {
        "id": 2,
        "id_user": 123,
        "name": "Mario Rossi",
        "phone": "123456789",
        "reserved_seats": 5,
        "day": "2024-02-23",
        "tms": "21:00",
        "time_slot": 2
    },
    {
        "id": 3,
        "id_user": 123,
        "name": "Mario Rossi",
        "phone": "123456789",
        "reserved_seats": 8,
        "day": "2024-02-24",
        "tms": "22:00",
        "time_slot": 3
    }
]
    db_mock.select_query.return_value = prenotazioni_di_prova
    context_mock.user_data = {}
    lista_prenotazioni = []
    for i, item in enumerate(prenotazioni_di_prova):
        context_mock.user_data["id_prenotazione"]=prenotazioni_di_prova[i]['id']
        context_mock.user_data["id_user"]=prenotazioni_di_prova[i]['id_user']
        context_mock.user_data["name"]=prenotazioni_di_prova[i]['name']
        context_mock.user_data["phone"]=prenotazioni_di_prova[i]['phone']
        context_mock.user_data["reserved_seats"]=prenotazioni_di_prova[i]['reserved_seats']
        context_mock.user_data["date"]=prenotazioni_di_prova[i]['day']
        context_mock.user_data["time_slot"] =  prenotazioni_di_prova[i]['tms']
        context_mock.user_data["time_slot_id"] = prenotazioni_di_prova[i]['time_slot']
        date_in_iso1 = datetime.strptime(str(context_mock.user_data["date"]), '%Y-%m-%d').strftime('%d-%m-%Y')
        prenotazioni_message = (
            f'ID_PRENOTAZIONE: {prenotazioni_di_prova[i]['id']}\n'
            f'Nome: {prenotazioni_di_prova[i]['name']}\n'
            f'Telefono: {prenotazioni_di_prova[i]['phone']}\n'
            f'Posti prenotati: {prenotazioni_di_prova[i]['reserved_seats']}\n'
            f'Giorno: {datetime.strptime(str(prenotazioni_di_prova[i]['day']), "%Y-%m-%d").strftime("%d-%m-%Y")}\n'
            f'Ora: {prenotazioni_di_prova[i]['time_slot']}\n\n'
        )
        lista_prenotazioni.append(prenotazioni_message)

    await context_mock.bot.send_message()
    expected_text ="In questa sezione potrai visualizzare e/o cancellare le tue prenotazioni.\nEcco l'elenco delle prenotazioni effettuate:\n"
    await context_mock.bot.send_message(text=expected_text)

    

    #
    
    #db_mock.execute_query.return_value = None

    # Crea un mock del bot Telegram
    

    # Chiama la funzione le_mie_prenotazioni_command con i mock delle dipendenze
    
    

    # Chiama la funzione le_mie_prenotazioni_command con i mock delle dipendenze
    """    query_mock.data = "deleteSinglePren" #deleteAllByUser
    update_mock.callback_query = query_mock
    update_mock.effective_chat.id = 123
    context_mock.bot = bot_mock
    context_mock.user_data = prenotazioni_di_prova
    
  
    
    # Verifica che la funzione abbia inviato il messaggio corretto
    await context_mock.bot.send_message()
    expected_text ="In questa sezione potrai visualizzare e/o cancellare le tue prenotazioni.\nEcco l'elenco delle prenotazioni effettuate:\n"
    await context_mock.bot.send_message(text=expected_text) """
    

    # Verifica che la funzione abbia inviato il messaggio corretto per ogni prenotazione
    """    bot_mock.send_message.assert_any_call(
        chat_id=update_mock.effective_chat.id,
        text=(
            f'ID_PRENOTAZIONE: {context_mock.user_data[0]["id"]}\n'
            f'Nome: {context_mock.user_data[0]["name"]}\n'
            f'Telefono: {context_mock.user_data[0]["phone"]}\n'
            f'Posti prenotati: {context_mock.user_data[0]["reserved_seats"]}\n'
            f'Giorno: {datetime.strptime(str(context_mock.user_data[0]["day"]), "%Y-%m-%d").strftime("%d-%m-%Y")}\n'
            f'Ora: {context_mock.user_data[0]["time_slot"]}\n\n'
        )
    )"""

 

    """
    bot_mock.send_message.assert_any_call(
        chat_id=update_mock.effective_chat.id,
        text=(
            f'ID_PRENOTAZIONE: {context_mock.user_data[1]["id"]}\n'
            f'Nome: {context_mock.user_data[1]["name"]}\n'
            f'Telefono: {context_mock.user_data[1]["phone"]}\n'
            f'Posti prenotati: {context_mock.user_data[1]["reserved_seats"]}\n'
            f'Giorno: {datetime.strptime(str(context_mock.user_data[1]["day"]), "%Y-%m-%d").strftime("%d-%m-%Y")}\n'
            f'Ora: {context_mock.user_data[1]["time_slot"]}\n\n'
        )
    )

    # Verifica che la funzione abbia inviato la tastiera corretta
    bot_mock.send_message.assert_called_with(
        chat_id=update_mock.effective_chat.id,
        text="Bene, queste sono le tue prenotazioni!\nCosa vuoi fare adesso?",
        reply_markup=AsyncMock()
    )"""
