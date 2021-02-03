# -*- coding: utf-8 -*-

import random
import statistics
import numpy as np
from copy import copy


infinito = 999999
n_it = 500000

def calcula_custo(solucao, matriz, size):
    custo = 0
    for i in range(size-2):
        custo += matriz[solucao[i]][solucao[i+1]]
    custo += matriz[solucao[0]][solucao[size-1]]
    return custo


def simple_combinatory_tweak(solucao, size):
    change_size = random.randrange(3, int((size/5)))
    
    for i in range(change_size):
        n1 = random.randrange(0, size-1)
        n2 = random.randrange(0, size-1)
        aux = solucao[n1]
        solucao[n1] = solucao[n2]
        solucao[n2] = aux
    
    return solucao

size = 280
coordenadas = []
f = open("entradas/a280.tsp", "r")
for i in f:
    entrada = i.split(" ")
    lat = float(entrada[1])
    log = float(entrada[2])
    coordenadas.append([lat, log])
    
coordenadas = np.array(coordenadas)

matriz = []
for i in range(size):
    line = []
    for j in range(size):
        
        dist = np.linalg.norm(coordenadas[i] - coordenadas[j])
        if i == j:
            dist = infinito
        line.append(dist)
    matriz.append(line)

#O que muda aqui e que ele vai montar essa solucao de maneira guloso, apenas
custos = []

for teste in range(10): 
    solucao = []
    city = random.randrange(0, size)
    
    solucao.append(city)
    t = 1
    
    while t < size:
        valor = infinito
        entra = size+1
        for i in range(size):
            if (matriz[city][i] < valor) and not (i in solucao):
                valor = matriz[city][i]
                entra = i
        solucao.append(entra)
        city = entra
        t += 1
    
    custo = calcula_custo(solucao, matriz, size)
    
    for i in range(n_it):
        nova_solucao = simple_combinatory_tweak(solucao, size)
        novo_custo = calcula_custo(solucao, matriz, size)
        if novo_custo < custo:
            solucao = copy(nova_solucao)
            custo = novo_custo
    custos.append(custo)

print('--------- RESULTADO ------------')
custos = np.array(custos)
print(custos)
media = str(np.mean(custos))
mediana = str(np.median(custos))
desvio = str(statistics.stdev(custos))
print("Média: "+media)
print("Mediana: "+mediana)
print("Desvio Padrão: "+desvio)