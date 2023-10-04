#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:07:08 2020

@author: yurifarod
"""

from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
from pylab import pcolor, colorbar, plot
import pandas as pd
import numpy as np

base = pd.read_csv('original.csv')

X = base.iloc[:, 0:6].values
y = base.iloc[:, 6].values

classe = []

for i in y:
    if i == 'Bart':
        classe.append(0)
    else:
        classe.append(1)

normalizador = MinMaxScaler(feature_range = (0,1))
X = normalizador.fit_transform(X)

som = MiniSom(x = 17, y = 17, input_len = 6, random_seed = 0)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)

pcolor(som.distance_map().T)
colorbar()

markers = ['o', 's']
colors = ['r', 'g']

for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5, w[1] + 0.5, markers[classe[i]],
         markerfacecolor = 'None', markersize = 10,
         markeredgecolor = colors[classe[i]], markeredgewidth = 2)
    
mapeamento = som.win_map(X)
outliers = np.concatenate((mapeamento[(16,8)], mapeamento[(0,11)]), axis = 0)
outliers = normalizador.inverse_transform(outliers)