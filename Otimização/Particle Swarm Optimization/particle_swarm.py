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
    def __init__(self, solucao, custo, velocidade):
        self.solucao = solucao
        self.custo = custo
        self.velocidade = velocidade
    
    def getCusto(self):
        return self.custo
    
    def getSol(self):
        return self.solucao
    
    def getVel(self):
        return self.velocidade

#f1 = -450, f2 = 390, f4 = -330, f6 = -140
bias = -140
d = 100
limite = 1000

p = 0.01
r = 5

n_pop = 100

v_max = 0.5
c = 1.494
peso = 0.5

aux = []
f = open("../otimo-f4.txt", "r")
for i in f:
    aux.append(float(i.replace('\n', '')))
aux= np.array(aux)


custos = []
for i in range(10):
    
    solucao = []
    vel = []
    for j in range(n_pop):
        sol = []
        for k in range(d):
            number = random.randrange(-100, 100)
            sol.append(number)
        for k in range(d):
            vel.append(0)
        custo = rastrigin_function(sol, aux, d, bias)
        
        solucao.append(Solucao(sol,custo, vel)) 
        
    solucao.sort(key=operator.attrgetter('custo'))
    actual_Sol = copy(solucao[0])
    global_Sol = copy(solucao[0])
    
    for it in range(limite):
        
        newSol = []
        for j in range(n_pop):
            vel = solucao[j].getVel()
            sol = solucao[j].getSol()
            
            for k in range(d):
                vel[k] = peso * vel[k] + 0.3 * c * (actual_Sol.getSol()[k] - sol[k]) +  0.6 * c * (global_Sol.getSol()[k] - sol[k])
                change = vel[k]
                if vel[k] == 0:
                    change = 1
                vel[k] = 0.5 / change
                
            for k in range(d):
                sol[k] = sol[k] + vel[k]
            
            custo = rastrigin_function(sol, aux, d, bias)
            
            newSol.append(Solucao(sol,custo, vel))
            
        solucao = copy(newSol)
        solucao.sort(key=operator.attrgetter('custo'))
        
        actual_Sol = copy(solucao[0])
        if solucao[0].getCusto() < global_Sol.getCusto():
            global_Sol = copy(solucao[0])
    
    custos.append(global_Sol.getCusto())

print('--------- RESULTADO ------------')
custos = np.array(custos)
print(custos)
media = str(np.mean(custos))
mediana = str(np.median(custos))
desvio = str(statistics.stdev(custos))
print("Média: "+media)
print("Mediana: "+mediana)
print("Desvio Padrão: "+desvio)