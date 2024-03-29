"""
LIB GENERIC
Inserito il disable per W0611 perchè
in questo file sono riportate la maggior
parte dei moduli
"""
#pylint: disable=W0611
import os
from logging import Logger
from datetime import datetime, timedelta
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application,Updater, CommandHandler, MessageHandler
from telegram.ext import filters, ConversationHandler
from telegram.ext import CallbackContext, CallbackQueryHandler, ContextTypes
from src.lib.mysql_class import MySQLDatabase
db = MySQLDatabase()
# Definizione degli stati
NAME, PHONE, RESERVED_SEATS, DAY, TIME_SLOT, CONFIRMATION, BUTTON_HANDLER = range(7)
