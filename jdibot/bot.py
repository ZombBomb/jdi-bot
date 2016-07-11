# -*- coding: utf-8 -*-
import config
import telebot
import time
import random as rand
import threading
from time import sleep
from SQLighter import SQLighter
from telebot import types

#@bot.message_handler(commands=['doit'])
def doit(message):	
	if len(message.text.split()) > 1:
		msg = message.text.split()[1]
		db_worker = SQLighter(config.database_name)
		db_worker.insert_single(message.chat.id, msg)
		db_worker.close()


class Bot:

	def __init__(self, token):
		self.bot = telebot.TeleBot(token)

	def updates(self):
		messages = self.bot.get_updates()
		for message in messages:
			doit(message.message)

	def activity(self):
		db_worker = SQLighter(config.database_name)
		rows = db_worker.count_rows()
		rand_val = rand.randint(1, rows)
		msg = db_worker.select_single(rand_val)
		self.bot.send_message(msg[2], msg[1])
		db_worker.close()