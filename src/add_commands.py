"""Add commands handler"""
from telegram import BotCommand
from telegram.ext import Application

import requests,json

from typing import Final
from src.lib.config import *
TOKEN: Final = BOT_CONFIG['__TOKEN']


cmd = [
        {"command":"start","description":"avvia il bot"},
        {"command":"prenota","description":"prenota un tavolo"},
        {"command":"le_mie_prenotazioni","description":"visualizza/disdici prenotazione"},
        {"command":"menu","description":"visualizza il menu"},
        {"command":"eventi","description":"visualizza gli special nights events"},
        {"command":"info","description":"visualizza le informazioni del ristorante"}
    ]
url = "https://api.telegram.org/bot"+TOKEN+"/setMyCommands?commands="+str(json.dumps(cmd))
req = requests.get(url)

