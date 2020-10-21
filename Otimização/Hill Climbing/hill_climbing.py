# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 07:54:05 2020
@author: yfdantas
"""

import random
import statistics
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

#Tweak do Livro
def algorithm_eight(solucao, d, p, r):
    actual_sol = []
    for i in range(d):
        actual_sol.append(solucao[i])
        
    for i in range(d):
        prob = random.randrange(0, 1)
        if(prob < p):
            teto = actual_sol[i] + r
            if teto > 100:
                teto = 100
            piso = actual_sol[i] - r
            if piso < -100:
                piso= -100
            actual_sol[i] = random.randrange( piso, teto)
                
    return actual_sol
    
bias = 390
d = 100
limite = 50000

#Variveis para o Alg 8
p = 0.2
r = 5

aux = []
f = open("../otimo-f3.txt", "r")
for i in f:
    aux.append(int(i))

custos = []
for k in range(10):
    solucao = []
    for i in range(d):
        number = random.randrange(-100, 100)
        solucao.append(number)
        
    #Aqui iniciamos o Hill Climbing
    melhor_custo = rosenbrock_function(solucao, aux, d, bias)
    
    melhor_sol = []
    melhor_sol = np.copy(solucao)
        
    for i in range(limite):
        solucao = algorithm_eight(melhor_sol, d, p, r)
        custo_atual = rosenbrock_function(solucao, aux, d, bias)
        
        if(custo_atual < melhor_custo):
            melhor_custo = custo_atual
            melhor_sol = np.copy(solucao)
    
    print(melhor_custo)
    custos.append(melhor_custo)

print('---------------------')
custos = np.array(custos)
print(np.mean(custos))
print(np.median(custos))
print(statistics.stdev(custos))