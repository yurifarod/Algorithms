#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:44:22 2023

@author: yurifarod

Tutorial de como usar a biblioteca deste código:

https://medium.com/@rubyabdullah14/building-a-telegram-bot-with-python-a-step-by-step-guide-5ca305bea6c0
https://www.hashtagtreinamentos.com/bot-de-telegram-com-python

Para Descobrir o seu "chat id" do Telegram, link útil:

https://www.alphr.com/find-chat-id-telegram/

Como pegar o seu id através do uso direto da api do bot:

https://api.telegram.org/botTOKEN_DE_VOCES/getUpdates
    
"""

import telebot


token = 'aqui_vai_sua_token_completa'
id = 'o_id_do_seu_telefone'

bot = telebot.TeleBot(token)

print('Digite o seu nome:')
nome = input()
print('Digite a sua idade:')
idade = input()
print('Digite o seu CPF')
n_cpf = input()


def send_telegram_msg(nome, idade, n_cpf):
    msg_final = ('''
                Confirmação de cadastro,
                Usuário: %s
                Nome: %s
                CPF: %s
                Obrigado por criar o seu cadastro!
                '''%(nome, idade, n_cpf))
    sent_msg = bot.send_message(id, msg_final, parse_mode="Markdown")

send_telegram_msg(nome, idade, n_cpf)
