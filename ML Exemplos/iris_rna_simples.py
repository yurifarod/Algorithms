#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RNa
@author: yurifarod
"""

import numpy as np
import pandas as pd
from keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

base = pd.read_csv('datasets/iris.csv')
features = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values


labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)
classe = to_categorical(classe)

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(features, classe, test_size=0.25)


'''
Foco aqui! A saida mano, ta errada
'''
from keras.models import Sequential
from keras.layers import Dense

classificador = Sequential()
classificador.add(Dense(units = 4, activation = 'relu', input_dim = 4))
classificador.add(Dense(units = 4, activation = 'relu'))

# Na camada de saida a funcao softmax e necessaria qnd se ha mais de uma classe
# Ha tb uma saida para cada classe
classificador.add(Dense(units = 3, activation = 'softmax'))

# Metrica loss e metrica tb alteradas pelas multiplas opcoes
classificador.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
                      metrics = ['categorical_accuracy'])

#Aqui o treinamento
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10,
                  epochs = 100)

resultado = classificador.evaluate(previsores_teste, classe_teste)
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

classe_teste2 = [np.argmax(t) for t in classe_teste]
previsoes2 = [np.argmax(t) for t in previsoes]

matriz = confusion_matrix(previsoes2, classe_teste2)

print(matriz)