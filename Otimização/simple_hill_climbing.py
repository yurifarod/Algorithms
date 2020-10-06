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

#Tweak Simples
def simple_tweak(solucao, d, size_change):
    actual_sol = []
    for i in range(d):
        actual_sol.append(solucao[i])
    
    index = random.randrange(0, 100)
    
    for i in range(size_change):
        number = random.randrange(-100, 100)
        actual_sol[index] = number 
        index += 1
        if index == 100:
            index = 0
    
    return actual_sol

#Tweak do Livro
def algorithm_eight(solucao, d, p, r):
    actual_sol = []
    for i in range(d):
        actual_sol.append(solucao[i])
        
    for i in range(d):
        prob = random.randrange(0, 1)
        if(prob < p):
            number = random.randrange((-1 * r), r)
            actual_sol[i] -= number
    return actual_sol
    
bias = -450
d = 100
limite = 50000

#Variavel para o Algo Simples
size_change = 1

#Variveis para o Alg 8
p = 0.02
r = 10

aux = []
f = open("otimo-f1.txt", "r")
for i in f:
    aux.append(int(i))

custos = []
for k in range(10):
    solucao = []
    for i in range(d):
        number = random.randrange(-100, 100)
        solucao.append(number)
        
    #Aqui iniciamos o Hill Climbing
    melhor_custo = sphere_function(solucao, aux, d, bias)
    
    melhor_sol = []
    for i in range(d):
        melhor_sol.append(solucao[i])
        
    for i in range(limite):
        solucao = simple_tweak(melhor_sol, d, size_change)
        #solucao = algorithm_eight(melhor_sol, d, p, r)
        custo_atual = sphere_function(solucao, aux, d, bias)
        
        if(custo_atual < melhor_custo):
            melhor_custo = custo_atual
            for i in range(d):
                melhor_sol[i] = solucao[i]
        
    custos.append(melhor_custo)

custos = np.array(custos)
print(np.mean(custos))
print(np.median(custos))
print(statistics.stdev(custos))