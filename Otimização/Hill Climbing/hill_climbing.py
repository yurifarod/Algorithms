# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 07:54:05 2020
@author: yfdantas
"""

import random
import statistics
import math
import numpy as np

#Funcao de custo
def sphere_function(solucao, aux, d, bias):
    custo = 0
    for i in range(d):
        number = solucao[i] + aux[i]
        custo += number*number
    custo = custo + bias
    return custo

#Se isso tiver certo eu cegue!
def rosenbrock_function(solucao, aux, d, bias):
    custo = 0
    solucao = solucao - aux + 1
    custo = np.sum(100.0*(solucao[1:]-solucao[:-1]**2.0)**2.0 + (1-solucao[:-1])**2.0) + bias
    return custo

def rastrigin_function(X, aux, d, bias):
    A = 10
    X = X + aux
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X]) + bias

def ackley_function(X, aux, d, bias):
    y = X - aux
    part1 = -0.2*np.sqrt((1/d)*np.sum(y**2))
    part2 = (1/d)*(np.sum(np.cos(2*np.pi*y)))
    return -20*np.exp(part1) -np.exp(part2) + 20 + np.exp(1) + bias

#Tweak do Livro
def algorithm_eight(solucao, d, p, r):
    actual_sol = []
    for i in range(d):
        actual_sol.append(solucao[i])
        
    for i in range(d):
        prob = random.randrange(0, 1)
        if(prob < p):
            valor = actual_sol[i] + random.randrange(-1 * r, r)
            while (valor > 100 or valor < -100):
                valor = actual_sol[i] + random.randrange(-1 * r, r)
            actual_sol[i] = valor
            
    return actual_sol

#f1 = -450, f2 = 390, f4 = -330 e f6 = -140    
bias = -330
d = 100
limite = 50000

#Variveis para o Alg 8
p = 0.01
r = 5

aux = []
f = open("../otimo-f4.txt", "r")
for i in f:
    aux.append(float(i.replace('\n', '')))

aux= np.array(aux)

custos = []
for k in range(10):
    solucao = []
    for i in range(d):
        number = random.randrange(-100, 100)
        solucao.append(number)
        
    #Aqui iniciamos o Hill Climbing
    melhor_custo = rastrigin_function(solucao, aux, d, bias)
    
    melhor_sol = []
    melhor_sol = np.copy(solucao)
        
    for i in range(limite):
        solucao = algorithm_eight(melhor_sol, d, p, r)
        custo_atual = rastrigin_function(solucao, aux, d, bias)
        
        if(custo_atual < melhor_custo):
            melhor_custo = custo_atual
            melhor_sol = np.copy(solucao)
    
    custos.append(melhor_custo)

print('--------- RESULTADO ------------')
custos = np.array(custos)
print(custos)
media = str(np.mean(custos))
mediana = str(np.median(custos))
desvio = str(statistics.stdev(custos))
print("Média: "+media)
print("Mediana: "+mediana)
print("Desvio Padrão: "+desvio)