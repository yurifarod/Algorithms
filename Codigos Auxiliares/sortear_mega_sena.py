# -*- coding: utf-8 -*-
"""
Spyder Editor

yurifarod
"""

import random
from datetime import datetime

numero_de_jogos = 6

def sortear_sena(n):
    random.seed((datetime.now().timestamp() * n) % 667)
    
    jogo = []
    for i in range(6):
        numero = random.randrange(1, 60)
        while numero in jogo:
            numero = random.randrange(1, 60)
        jogo.append(numero)
    
    jogo.sort()
    
    return jogo

for i in range(numero_de_jogos):
    print(sortear_sena(i))