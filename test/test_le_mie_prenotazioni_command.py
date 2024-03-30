"""
modulo le mie prenotazioni command
"""

from unittest.mock import AsyncMock
import pytest
from src.le_mie_prenotazioni_command import datetime



@pytest.mark.asyncio
async def test_le_mie_prenotazioni_command():
    """
    fixture
    """
    context_mock = AsyncMock()
    db_mock = AsyncMock()

    # Crea un mock della connessione al database
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
    for item in prenotazioni_di_prova:
        context_mock.user_data["id_prenotazione"]=item['id']
        context_mock.user_data["id_user"]=item['id_user']
        context_mock.user_data["name"]=item['name']
        context_mock.user_data["phone"]=item['phone']
        context_mock.user_data["reserved_seats"]=item['reserved_seats']
        context_mock.user_data["date"]=item['day']
        context_mock.user_data["time_slot"] =  item['tms']
        context_mock.user_data["time_slot_id"] = item['time_slot']
        prenotazioni_message = (
            f'ID_PRENOTAZIONE: {item['id']}\n'
            f'Nome: {item['name']}\n'
            f'Telefono: {item['phone']}\n'
            f'Posti prenotati: {item['reserved_seats']}\n'
            f'Giorno: {datetime.strptime(
                str(item['day'])
                , "%Y-%m-%d").strftime("%d-%m-%Y")}\n'
            f'Ora: {item['time_slot']}\n\n'
        )
        lista_prenotazioni.append(prenotazioni_message)

    await context_mock.bot.send_message()
    expected_text =("In questa sezione potrai visualizzare e/o "
                    "cancellare le tue prenotazioni.\nEcco l'elenco "
                    "delle prenotazioni effettuate:\n")
    await context_mock.bot.send_message(text=expected_text)
