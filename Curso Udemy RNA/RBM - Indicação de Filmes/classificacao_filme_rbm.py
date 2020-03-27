#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:33:57 2020

@author: yurifarod
"""

from rbm import RBM
import numpy as np

rbm = RBM(num_visible = 6, num_hidden = 2)

base = np.array([[1,1,1,0,0,0],
                 [1,0,1,0,0,0],
                 [1,1,1,0,0,0],
                 [0,0,1,1,1,1],
                 [0,0,1,1,0,1],
                 [0,0,1,1,0,1]])

filmes = ["A bruxa", "Invocacao do mal", "O chamado",
          "Se beber nao case", "Gente grande", "American pie"]

rbm.train(base, max_epochs=5000)
rbm.weights

usuario1 = np.array([[1,1,0,1,0,0]])
usuario2 = np.array([[0,0,0,1,1,0]])

rbm.run_visible(usuario1)
rbm.run_visible(usuario2)

camada_escondida = np.array([[1,0]])
recomendacao = rbm.run_hidden(camada_escondida)

for i in range(len(usuario1[0])):
    #print(usuario1[0,i])
    if usuario2[0,i] == 0 and recomendacao[0,i] == 1:
        print(filmes[i])