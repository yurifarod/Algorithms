#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:05:26 2020

@author: yfdantas
"""

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

base = pd.read_csv('poluicao_china.csv')

base = base.dropna()

base = base.drop('No', axis = 1)
base = base.drop('year', axis = 1)
base = base.drop('month', axis = 1)
base = base.drop('day', axis = 1)
base = base.drop('hour', axis = 1)
base = base.drop('cbwd', axis = 1)

base_treinamento = base.iloc[:, 1:7].values

poluicao = base.iloc[:, 0].values

normalizador = MinMaxScaler(feature_range = (0, 1))
base_treinamento_normalizada = normalizador.fit_transform(base_treinamento)

poluicao = poluicao.reshape(-1, 1)
poluicao_normalizado = normalizador.fit_transform(poluicao)

previsores = []
poluicao_real = []
for i in range(10, 41757):
    previsores.append(base_treinamento_normalizada[i-10:i, 0:6])
    poluicao_real.append(poluicao_normalizado[i, 0])
previsores, poluicao_real = np.array(previsores), np.array(poluicao_real)

regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, input_shape = (previsores.shape[1], 6)))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1, activation = 'linear'))

regressor.compile(optimizer = 'rmsprop', loss = 'mean_squared_error', 
                  metrics = ['mean_absolute_error'])
regressor.fit(previsores, poluicao_real, epochs = 10, batch_size = 64)

previsoes = regressor.predict(previsores)
previsoes = normalizador.inverse_transform(previsoes)

previsoes.mean()
poluicao.mean()

plt.plot(poluicao, color = 'red', label = 'Real')
plt.plot(previsoes, color = 'blue', label = 'Previsto')
plt.legend()
plt.show()
