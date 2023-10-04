#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:46:21 2020

@author: yurifarod
"""

"""
Created on Tue Mar  3 19:07:08 2020

@author: yurifarod
"""

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

base = pd.read_csv('personagem.csv')

X = base.iloc[:, 0:6].values
y = base.iloc[:, 6].values

classe = []

for i in y:
    if i == 'Bart':
        classe.append(0)
    else:
        classe.append(1)

normalizador = MinMaxScaler(feature_range = (0,1))
previsores = normalizador.fit_transform(X)

previsores_teste, previsores_treinamento, classe_teste, classe_treinamento = train_test_split(previsores, classe, test_size=0.25)

classificador = Sequential()
classificador.add(Dense(units = 6, activation = 'relu', input_dim = 6))
classificador.add(Dense(units = 3, activation = 'relu'))

# Na camada de saida a funcao softmax e necessaria qnd se ha mais de uma classe
# Ha tb uma saida para cada classe
classificador.add(Dense(units = 1, activation = 'softmax'))

# Metrica loss e metrica tb alteradas pelas multiplas opcoes
classificador.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])

#Aqui o treinamento
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 1,
                  epochs = 200)

resultado = classificador.evaluate(previsores_teste, classe_teste)
previsoes = classificador.predict(previsores_teste)
previsores = (previsores > 0.5)
matriz = confusion_matrix(previsoes, classe_teste)

