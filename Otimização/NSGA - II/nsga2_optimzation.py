# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:54:05 2020
@author: yfdantas
"""

import random
import math
import numpy as np
from copy import copy
import matplotlib.pyplot as plt

#Funcao de custo
def dtlz1_function(x, n_var, n_obj):
  f = []
  k = n_var - n_obj + 1

  g = 0
  i = n_var - k
  while (i < n_var):
    g = g + ((x[i] - 0.5) * (x[i] - 0.5) - (math.cos(20 * math.pi * (x[i] - 0.5))))
    i = i + 1
  
  g = 100 * (k + g)
  i = 0
  while (i < n_obj):
    v = (1.0 + g) * 0.5;
    f.append(v)
    i = i + 1

  i = 0
  j = 0
  while (i < n_obj):
    while (j < n_obj):
      f[i] = f[i] * x[j]
      j = j + 1
    if (i != 0):
      aux = n_obj - (i + 1)
      f[i] = f[i] * (1 - x[aux])
    i = i + 1

  return f

def dtlz2_function(x, n_var, n_obj):
  f = []
  k = n_var - n_obj + 1

  g = 0
  i = n_var - k
  while (i < n_var):
    g = g + ((x[i] - 0.5) * (x[i] - 0.5))
    i = i + 1
  
  i = 0
  while (i < n_obj):
    v = 1 + g;
    f.append(v)
    i = i + 1

  i = 0
  j = 0
  while (i < n_obj):
    while (j < n_obj):
      f[i] = f[i] * (math.cos(x[j] * 0.5 * math.pi));
      j = j + 1
    if (i != 0):
      aux = n_obj - (i + 1)
      f[i] = f[i] * (math.sin(x[aux] * 0.5 * math.pi))
    i = i + 1
  return f

#Algoritmo de Dominancia de Soluções 
def dominancia_simples(sol_1, sol_2):
  domina = False
  tuplas = zip(sol_1, sol_2)
  
  for tupla_1, tupla_2 in tuplas:
    if tupla_1 < tupla_2:
        domina = True
    
    return domina 

def fronteira_pareto_simples(solucao):
    nova_lista = []
    for sol in solucao:
      nova_lista.append(sol)
      
      for sol_aux in nova_lista:
        if sol_aux != sol:
          if dominancia_simples(sol_aux.custo, sol.custo):
            nova_lista.remove(sol)
            break
          elif dominancia_simples(sol.custo, sol_aux.custo):
            nova_lista.remove(sol_aux)
    return nova_lista[0]

#Tweak proposto
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

#Crossover proposto
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
    
limite = 1000
n_pop = 30
n_var = 12
n_obj = 3
n_elite = 10
v_mut = 5
v_prob = 10

solucao_1 = []
for j in range(n_pop):
    sol = []
    for k in range(n_var):
        number = random.randrange(-100, 100)
        sol.append(number)
    
    custo_f1 = []
    custo_f1 = dtlz2_function(sol, n_var, n_obj)
    #custo_f1 = dtlz1_function(sol, n_var, n_obj)
    
    solucao_1.append(Solucao(sol, custo_f1))    

for it in range(limite):
    
    pos_front = []
    for i in range(len(solucao_1)):
        oper_front = fronteira_pareto_simples(solucao_1)
        pos_front.append(oper_front)

    selecionado = []
    for j in range(n_elite):
        selecionado.append(copy(pos_front[j]))
        
    for j in range(n_pop-n_elite):
        pai = random.randrange(0, n_elite)
        mae = random.randrange(0, n_elite)
        children = algorithm_24(selecionado[pai].getSol(), selecionado[mae].getSol(), n_var)
        new_sol = algorithm_eight(children, n_var, v_prob, v_mut)
        #new_custo = dtlz1_function(new_sol, n_var, n_obj)
        new_custo = dtlz2_function(new_sol, n_var, n_obj)
        selecionado.append(Solucao(new_sol, new_custo))
    solucao_1 = copy(selecionado)

#Impressao dos Resultados
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
impressor = []
for i in solucao_1:
    if i.custo not in impressor:
        impressor.append(i.custo)
        ax.scatter3D(i.custo[0], i.custo[1], i.custo[2], color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))

# Creating figure

 
# Creating plot
ax.scatter3D(1, 2, 3, color = "green")
plt.title("Fronteira de Pareto Obtida")
 
# show plot
plt.show()