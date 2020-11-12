# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 07:54:05 2020
@author: yfdantas
"""

import random
import statistics
import operator
import math
import numpy as np
from copy import copy

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

def algorithm_24(vetorA, vetorB, d):
    e = random.randrange(0, d)
    f = random.randrange(e, d)
    
    vetor_aux = []
    for i in range(d):
        if i <= e:
            vetor_aux.append(vetorA[i])
        if i > e and i <= f:
            vetor_aux.append(vetorB[i])
        if i > f:
            vetor_aux.append(vetorA[i])
    return vetor_aux
    
class Solucao:
    def __init__(self, solucao, custo):
        self.solucao = solucao
        self.custo = custo
    
    def getCusto(self):
        return self.custo
    
    def getSol(self):
        return self.solucao

#f1 = -450, f2 = 390 e f3 = -330
bias = -330
d = 100
limite = 1000

p = 0.01
r = 5

n_pop = 100
n_elite = 10

aux = []
f = open("../otimo-f4.txt", "r")
for i in f:
    aux.append(float(i.replace('\n', '')))
aux= np.array(aux)


custos = []
for i in range(10):
    
    solucao = []
    for j in range(n_pop):
        sol = []
        for k in range(d):
            number = random.randrange(-100, 100)
            sol.append(number)
        custo = rastrigin_function(sol, aux, d, bias)
        
        solucao.append(Solucao(sol,custo)) 
    
    for it in range(limite):
    
        selecionado = []
        for j in range(n_elite):
            selecionado.append(copy(solucao[j]))
        
        for j in range(n_pop-n_elite):
            pai = random.randrange(0, n_elite)
            mae = random.randrange(0, n_elite)
            
            children = algorithm_24(selecionado[pai].getSol(), selecionado[mae].getSol(), d)
            new_sol = algorithm_eight(children, d, p, r)
            new_custo = rastrigin_function(new_sol, aux, d, bias)
            selecionado.append(Solucao(new_sol, new_custo))
        
        selecionado.sort(key=operator.attrgetter('custo'))
        
        solucao = copy(selecionado)
        melhor_sol = selecionado[0]
        
        if  melhor_sol.getCusto() < 1000:
            break
    
    custos.append(melhor_sol.getCusto())

print('--------- RESULTADO ------------')
custos = np.array(custos)
print(custos)
media = str(np.mean(custos))
mediana = str(np.median(custos))
desvio = str(statistics.stdev(custos))
print("Média: "+media)
print("Mediana: "+mediana)
print("Desvio Padrão: "+desvio)