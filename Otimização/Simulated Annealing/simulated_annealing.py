#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:58:26 2020

@author: yurifarod
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
 
bias = -450
d = 100
limite = 50000

#Variveis para o Alg 8
p = 0.02
r = 5

aux = []
f = open("../otimo-f3.txt", "r")
for i in f:
    aux.append(int(i))

custos = []
for k in range(10):
    
    solucao_atual = []
    solucao_aux = []
    for i in range(d):
        number = random.randrange(-100, 100)
        solucao_atual.append(number)
    
    custo_atual = rosenbrock_function(solucao_atual, aux, d, bias)
    
    #Aqui iniciamos o Simulated Annealing
    melhor_sol = []
    melhor_sol = np.copy(solucao_atual)
    melhor_custo = rosenbrock_function(melhor_sol, aux, d, bias)
    
    for i in range(limite):
        temp_calc = float(i/limite)*1.2
        temp_comp = random.randrange(0, 1)
        
        solucao_aux = algorithm_eight(solucao_atual, d, p, r)
        custo_aux = rosenbrock_function(solucao_aux, aux, d, bias)
        
        if(custo_aux < custo_atual or temp_calc < temp_comp):
            solucao_atual = np.copy(solucao_aux)
            custo_atual = custo_aux
        
        if(custo_atual < melhor_custo):
            melhor_sol = np.copy(solucao_atual)
            melhor_custo = custo_atual
        
    print(melhor_custo)
    custos.append(melhor_custo)

print('---------------------')
custos = np.array(custos)
print(np.mean(custos))
print(np.median(custos))
print(statistics.stdev(custos))