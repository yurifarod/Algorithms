#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:58:26 2020

@author: yurifarod
"""

import math
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

def rastrigin_function(X, aux, d, bias):
    A = 10
    X = X + aux
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X]) + bias

#Tweak do Livro
def algorithm_eight(solucao, d, p, r):
    actual_sol = []
    retorno_lista = []
    
    for i in range(d):
        actual_sol.append(solucao[i])
        
    for i in range(d):
        prob = random.randrange(0, 1)
        if(prob < p):
            retorno_lista.append(i)
            valor = actual_sol[i] + random.randrange(-1 * r, r)
            while (valor > 100 or valor < -100):
                valor = actual_sol[i] + random.randrange(-1 * r, r)
            actual_sol[i] = valor
            
    return actual_sol, retorno_lista

#f1 = -450, f2 = 390 e f3 = -330
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
    
    solucao_atual = []
    solucao_aux = []
    for i in range(d):
        number = random.randrange(-100, 100)
        solucao_atual.append(number)
    
    custo_atual = rastrigin_function(solucao_atual, aux, d, bias)
    
    #Aqui iniciamos a Busca Tabu
    t_lista = 20
    lista_tabu = []
    lista_aux = []
    melhor_sol = []
    melhor_sol = np.copy(solucao_atual)
    melhor_custo = custo_atual
    for i in range(limite):
        
        solucao_aux, retorno_lista = algorithm_eight(solucao_atual, d, p, r)
        custo_aux = rastrigin_function(solucao_aux, aux, d, bias)
        
        listado = False
        
        while(listado and custo_aux > melhor_custo):
            for compare in lista_tabu:
                if np.allclose(compare, retorno_lista):
                    listado = True
                else:
                    listado = False
            
            if listado:
                solucao_aux, retorno_lista = algorithm_eight(solucao_atual, d, p, r)
                custo_aux = rastrigin_function(solucao_aux, aux, d, bias)
        
        
        if len(lista_tabu) <= t_lista:
            lista_tabu.append(np.copy(retorno_lista))
        else:
            lista_aux = np.copy(lista_tabu)
            lista_tabu[0] = np.copy(retorno_lista)
            for z in range(t_lista, 0, -1):
                lista_tabu[z] = np.copy(retorno_lista[z-1])
        
        if(not(listado) and custo_aux < melhor_custo):
            solucao_atual = np.copy(solucao_aux)
            custo_atual = custo_aux
        
        if(custo_atual < melhor_custo):
            melhor_sol = np.copy(solucao_atual)
            melhor_custo = custo_atual
    
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