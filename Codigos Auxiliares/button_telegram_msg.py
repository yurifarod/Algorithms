import telebot
from time import sleep
from gpiozero import LED, Button

def send_telegram_msg(bot, id_phone, led, controller):
	if(controller == 1):
		msg_final = "O botao foi pressionado!"
		bot.send_message(id_phone, msg_final, parse_mode="Markdown")
		led.on()
		sleep(5)
	else:
		led.off()

token = 'token_do_seu_bot'
id_phone = 'id_do_seu_celular'

led = LED(17)
botao = Button(27)

while True:
	if botao.is_pressed:
		send_telegram_msg(bot, id_phone, led, controller=1)
	else:
		send_telegram_msg(bot, id_phone, led, controller=2)