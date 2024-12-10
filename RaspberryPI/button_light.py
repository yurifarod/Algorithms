from gpiozero import LED, Button

#criacao dos objetos conectados ao LED e ao botao, respectivamente
led = LED(17)
botao = Button(27)

while True:

    #quando o botao estiver pressionado
    botao.when_pressed = led.on #acende o LED

    #quando o botao estiver solto
    botao.when_released = led.off #apaga o LED