"""
modulo prenota command
"""

from unittest.mock import AsyncMock, ANY
import pytest
#from unittest import mock
from src.lib.lib import NAME,PHONE,RESERVED_SEATS,DAY,BUTTON_HANDLER,CONFIRMATION
from src.prenota_command import (
    prenota_start,
    prenota_name,
    prenota_phone,
    prenota_reserved_seats,
    prenota_day,
    confirmation,
    button_click,
)


@pytest.mark.asyncio
async def test_prenota_start():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    result = await prenota_start(update_mock, context_mock)
    assert result == NAME  # Make sure to import NAME from your actual code

@pytest.mark.asyncio
async def test_prenota_name():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    # Setting up context.user_data with a name
    name_value = "Paperino"
    update_mock.message.text = name_value
    context_mock.user_data = {}
    context_mock.message.reply_text.return_value = AsyncMock()

    # Calling the function
    result = await prenota_name(update_mock, context_mock)

    # Assertions
    await context_mock.bot.send_message()
    assert context_mock.user_data['name'] == name_value
    expected_text = f'Grazie, {name_value}! Qual è il tuo numero di telefono?'
    await context_mock.bot.send_message(text=expected_text)
    assert result == PHONE  # Assuming PHONE is the next step

@pytest.mark.asyncio
async def test_prenota_phone():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    # Setting up context.user_data with a name
    phone_value = "1234455678"
    update_mock.message.text = phone_value
    context_mock.user_data = {}
    context_mock.message.reply_text.return_value = AsyncMock()

    # Calling the function
    result = await prenota_phone(update_mock, context_mock)

    # Assertions
    await context_mock.bot.send_message()
    assert context_mock.user_data['phone'] == phone_value
    expected_text = ("Ottimo! Quanti posti desideri prenotare?"
    "Inserisci un numero compreso tra 1 e 10.")
    await context_mock.bot.send_message(text=expected_text)
    assert result == RESERVED_SEATS  # Assuming RESERVED_SEATS is the next step

@pytest.mark.asyncio
async def test_prenota_reserved_seats_valid_input():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    seats_value = "5"
    update_mock.message.text = seats_value
    context_mock.user_data = {}
    context_mock.message.reply_text.return_value = AsyncMock()


    #update_mock.message.text = "5"

    result = await prenota_reserved_seats(update_mock, context_mock)

    await context_mock.bot.send_message()
    assert context_mock.user_data['reserved_seats'] == int(seats_value)
    expected_text = (f'Bene! Il numero di posti selezionati è {seats_value}.'
                     'Rispondi con un qualsiasi carattere per continuare...')
    await context_mock.bot.send_message(text=expected_text)
    assert result == DAY  # Assuming DAY is the next step


@pytest.mark.asyncio
async def test_prenota_reserved_seats_invalid_input():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    seats_value = "invalid_input"
    update_mock.message.text = seats_value
    context_mock.user_data = {}
    context_mock.message.reply_text.return_value = AsyncMock()

    result = await prenota_reserved_seats(update_mock, context_mock)

    assert result is None
    assert context_mock.user_data.get('reserved_seats') is None
    await context_mock.bot.send_message()
    expected_text ="Per favore, inserisci un numero non un carattere PAGLIACCIO."
    await context_mock.bot.send_message(text=expected_text)

@pytest.mark.asyncio
async def test_prenota_reserved_seats_out_of_range():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    seats_value ="15"
    update_mock.message.text = seats_value
    context_mock.user_data = {}
    context_mock.message.reply_text.return_value = AsyncMock()

    result = await prenota_reserved_seats(update_mock, context_mock)

    assert result is None
    assert context_mock.user_data.get('reserved_seats') is None
    await context_mock.bot.send_message()
    expected_text ="Per favore, inserisci un numero valido di posti (da 1 a 10)."
    await context_mock.bot.send_message(text=expected_text)

@pytest.mark.asyncio
async def test_prenota_day():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    # Chiamata alla funzione prenota_day
    result = await prenota_day(update_mock, context_mock)

    # Verifica che la risposta contenga il testo corretto
    update_mock.message.reply_text.assert_called_once_with(
        "Per quale giorno desideri prenotare?\nSeleziona una data:",
        reply_markup=ANY # Verifica che sia presente una InlineKeyboardMarkup
    )
    # Estrai il reply_markup inviato come argomento alla reply_text
    reply_markup = update_mock.message.reply_text.call_args[1]['reply_markup']

    # Verifica che reply_markup contenga i pulsanti corretti
    assert len(reply_markup.inline_keyboard) == 7  # Verifica che ci siano 7 pulsanti
    for button_row in reply_markup.inline_keyboard:
        for button in button_row:
            assert button.callback_data.startswith("manageDate@")
    assert result == BUTTON_HANDLER  # Assuming BUTTON_HANDLER is the next step
# @pytest.mark.asyncio
# async def test_prenota_time_slot(update_context_fixture):
#     """
#     metodo
#     """
#     update_mock, context_mock, query_mock, bot_mock, db_mock = update_context_fixture

#     context_mock.user_data = {"reserved_seats": 5, "date": "2024-01-20"}

#     res_mock = [
#         {"time_slot": "20:00", "id_time_slot": 1},
#         {"time_slot": "21:00", "id_time_slot": 2},
#         {"time_slot": "22:00", "id_time_slot": 3}
#     ]
#     query_mock.return_value = res_mock

#     # Call the function
#     result = prenota_time_slot(update_mock, context_mock)
#     res = await result
#     if res == 3:
#         assert  res == DAY


@pytest.mark.asyncio
async def test_confirmation(mocker):
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()

    # Configuriamo il dizionario user_data con dati di esempio
    context_mock.user_data = {
        "name": "Mario Rossi",
        "phone": "123456789",
        "reserved_seats": 2,
        "date": "2023-01-01",
        "time_slot": "15:00",
    }

    async def reply_text_mock(*args, **kwargs):
        """
        metodo
        """

        print(args,kwargs)
        assert 'Conferma' in kwargs['reply_markup'].inline_keyboard[0][0].text
        assert 'Annulla' in kwargs['reply_markup'].inline_keyboard[0][1].text
        return AsyncMock()

    mocker.patch.object(update_mock.message, 'reply_text', side_effect=reply_text_mock)

    # Chiamiamo la funzione di conferma
    result = await confirmation(update_mock, context_mock)

    # Verifichiamo che la funzione restituisca il valore corretto (BUTTON_HANDLER)
    assert result == BUTTON_HANDLER

    # Verifichiamo che il metodo di risposta del messaggio sia stato chiamato correttamente
    update_mock.message.reply_text.assert_called_once()

    await context_mock.bot.send_message()
    # Possiamo anche verificare che il messaggio contenga le informazioni di prenotazione
    expected_text = (
        'Questi sono i dettagli della tua prenotazione:\n'
        'Nome: Mario Rossi\n'
        'Telefono: 123456789\n'
        'Posti prenotati: 2\n'
        'Giorno: 2023-01-01\n'
        'Ora: 20:00\n\n'
        'Confermi la prenotazione?'
    )
    await context_mock.bot.send_message(text=expected_text, reply_markup= ANY)

# @pytest.mark.asyncio
# async def test_button_click_date(update_context_fixture):
#     """
#     metodo
#     """
#     update_mock, context_mock, query_mock, bot_mock, db_mock = update_context_fixture
#     query_mock.data = "manageDate@2023-01-01"
#     update_mock.callback_query = query_mock
#     update_mock.effective_chat.id = 123
#     context_mock.bot = bot_mock
#     context_mock.user_data = {}

#     db_mock.select_query.return_value = [{'n_row': 3}]

#     result = await button_click(update_mock, context_mock)

#     bot_mock.delete_message.assert_called_with(
#         chat_id=query_mock.message.chat_id,
#         message_id=query_mock.message.message_id)
#     bot_mock.send_message.assert_called_once_with(
#         chat_id=update_mock.effective_chat.id,
#         text=("D'accordo! La data selezionata è 01-01-2023 ."
#               "Rispondi con un qualsiasi carattere per continuare..."))
#     assert result == TIME_SLOT

@pytest.mark.asyncio
async def test_button_click_time():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    query_mock = AsyncMock()
    bot_mock = AsyncMock()

    query_mock.data = "manageTime@20:00#1"
    update_mock.callback_query = query_mock
    context_mock.bot = bot_mock
    context_mock.user_data = {}

    result = await button_click(update_mock, context_mock)

    bot_mock.delete_message.assert_called_with(
        chat_id=query_mock.message.chat_id,
        message_id=query_mock.message.message_id)
    bot_mock.send_message.assert_called_once_with(
        chat_id=update_mock.effective_chat.id,
        text=("Perfetto! Ci vediamo alle 20:00!"
              "Rispondi con un qualsiasi carattere per continuare..."))

    assert result == CONFIRMATION


@pytest.mark.asyncio
async def test_button_click_pren():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    query_mock = AsyncMock()
    bot_mock = AsyncMock()

    query_mock.data = "confirmPren"
    update_mock.callback_query = query_mock
    update_mock.effective_chat.id = 123
    context_mock.bot = bot_mock
    context_mock.user_data = {
        'name': 'Mario Rossi',
        'phone': '123456789',
        'reserved_seats': 2,
        'date': '2023-01-01',
        'id_time_slot': 1
    }

    result = await button_click(update_mock, context_mock)

    await context_mock.bot.send_message()
    expected_text =("Tutto pronto! Ti aspettiamo.\n\n"
    "E ADESSO?!\nHai dato un'occhiata ai nostri eventi? Clicca qui -->"
    "/eventi e preparati a divertirti con noi!")
    await context_mock.bot.send_message(text=expected_text)
    assert result == 6

@pytest.mark.asyncio
async def test_button_click_decline():
    """
    metodo
    """
    update_mock = AsyncMock()
    context_mock = AsyncMock()
    query_mock = AsyncMock()
    bot_mock = AsyncMock()

    query_mock.data = "declinePren"
    update_mock.callback_query = query_mock
    context_mock.bot = bot_mock

    result = await button_click(update_mock, context_mock)

    await context_mock.bot.send_message()
    expected_text =("Oh no, hai annullato la procedura di prenotazione :"
        "'(\n\nQualcosa è andato storto?\nContattaci pure atttraverso i "
        "nostri contatti che troverai qui --> /info\n"
        "Saremo felici di accoglierti presto, magari in uno dei nostri /eventi ;)")
    await context_mock.bot.send_message(text=expected_text)

    assert result == 6
