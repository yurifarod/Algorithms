#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from time import sleep
from gpiozero import LED, Button

def send_telegram_msg(bot, id_phone, led, iterator):
    
    if(iterator == 1):
        msg_final = "O botao foi pressionado!"
        bot.send_message(id_phone, msg_final, parse_mode="Markdown")
        led.on()
        sleep(5)
    else:
        led.off()
    

token = '6100016451:AAFbUCma9j3wmJhDmQvolWNJn0bT1gyiV44'
id_phone = '886758070'
bot = telebot.TeleBot(token)
   
led = LED(17)
botao = Button(27)

while True:
    if botao.is_pressed:
        send_telegram_msg(bot, id_phone, led, iterator=1)
    else:
        send_telegram_msg(bot, id_phone, led, iterator=2)