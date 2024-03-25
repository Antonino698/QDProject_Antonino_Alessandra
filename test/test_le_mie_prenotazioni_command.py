"""
modulo le mie prenotazioni command
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0621
# pylint: disable=W0718
import asyncio
from unittest.mock import AsyncMock, patch, ANY, MagicMock
import pytest
from src.lib.lib import *
from src.le_mie_prenotazioni_command import *
from src.lib.mysql_class import MySQLDatabase

from src.start_command import *
@pytest.fixture
def update_context_fixture():
    """
    fixture
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    query_mock = AsyncMock()
    bot_mock = AsyncMock()
    db_mock = AsyncMock()
    return update_mock, context_mock, query_mock, bot_mock, db_mock

@pytest.mark.asyncio
async def test_le_mie_prenotazioni_command(update_context_fixture):
    """
    fixture
    """
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
        date_in_iso1 = datetime.strptime(
            str(context_mock.user_data["date"]), '%Y-%m-%d').strftime('%d-%m-%Y')
        prenotazioni_message = (
            f'ID_PRENOTAZIONE: {prenotazioni_di_prova[i]['id']}\n'
            f'Nome: {prenotazioni_di_prova[i]['name']}\n'
            f'Telefono: {prenotazioni_di_prova[i]['phone']}\n'
            f'Posti prenotati: {prenotazioni_di_prova[i]['reserved_seats']}\n'
            f'Giorno: {datetime.strptime(
                str(prenotazioni_di_prova[i]['day'])
                , "%Y-%m-%d").strftime("%d-%m-%Y")}\n'
            f'Ora: {prenotazioni_di_prova[i]['time_slot']}\n\n'
        )
        lista_prenotazioni.append(prenotazioni_message)

    await context_mock.bot.send_message()
    expected_text =("In questa sezione potrai visualizzare e/o "
                    "cancellare le tue prenotazioni.\nEcco l'elenco "
                    "delle prenotazioni effettuate:\n")
    await context_mock.bot.send_message(text=expected_text)
