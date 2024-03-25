"""
LIB GENERIC
"""
# pylint: disable=R0914
# pylint: disable=E1120
# pylint: disable=W0401
# pylint: disable=W0611
# pylint: disable=W0612
# pylint: disable=W0613
# pylint: disable=W0614
# pylint: disable=W0718
import os
from logging import Logger
from datetime import datetime, timedelta
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application,Updater, CommandHandler, MessageHandler
from telegram.ext import filters, ConversationHandler
from telegram.ext import CallbackContext, CallbackQueryHandler, ContextTypes

from src.lib.mysql_class import *
db = MySQLDatabase()
# Definizione degli stati
NAME, PHONE, RESERVED_SEATS, DAY, TIME_SLOT, CONFIRMATION, BUTTON_HANDLER = range(7)
