# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:00:24 2026

@author: yfdantas
"""
import time
import requests

response = requests.get('https://api.telegram.org/botTOKEN_DE_VOCES/getUpdates')
data_old = response.json()
last_message_id = len(data_old['result']) - 1
data_old = data_old['result'][last_message_id]['message']['text']

while True:
	time.sleep(3)
	response = requests.get('https://api.telegram.org/botTOKEN_DE_VOCES/getUpdates')
	data = response.json()
	last_message_id = len(data['result']) - 1
	data = data['result'][last_message_id]['message']['text']

	if data_old == data:
		print("Mensagem segue igual!")
	else:
		message = data.split(';')
		data_old = data
		print(message)