#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:42:03 2020

@author: yurifarod
"""

from rbm import RBM
import numpy as np

rbm = RBM(num_visible = 6, num_hidden = 3)

base = np.array([[0,1,1,1,0,1],
                 [1,1,0,1,1,1],
                 [0,1,0,1,0,1],
                 [0,1,1,1,0,1],
                 [1,1,0,1,0,1],
                 [1,1,0,1,1,1]])

filmes = ["Freddy x Jason", "O Ultimato Bourne", "Star Trek",
          "Exterminador do Futuro", "Norbit", "Star Wars"]

rbm.train(base, max_epochs=5000)
rbm.weights

leonardo = np.array([[0,1,0,1,0,0]])

rbm.run_visible(leonardo)

camada_escondida = np.array([[1,0,1]])
recomendacao = rbm.run_hidden(camada_escondida)

for i in range(len(leonardo[0])):
    if leonardo[0,i] == 0 and recomendacao[0,i] == 1:
        print(filmes[i])