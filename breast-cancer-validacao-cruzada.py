#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:19:02 2019

@author: yurifarod
"""
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

#Entrada das bases de teste e avaliação
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

#Definimos um metodo de criacao da RNA para ser usado posteriormente
def criarRede():
    classificador = Sequential()
    classificador.add(Dense(units = 16, activation = 'relu', 
                            kernel_initializer = 'random_uniform', input_dim = 30))
    classificador.add(Dense(units = 16, activation = 'relu', 
                            kernel_initializer = 'random_uniform'))
    classificador.add(Dense(units = 1, activation = 'sigmoid'))
    
    otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
    classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                          metrics = ['binary_accuracy'])
    return classificador

classificador = KerasClassifier(build_fn = criarRede,
                                epochs = 200,
                                batch_size = 10)
resultados = cross_val_score(estimator = classificador,
                             X = previsores, y = classe,
                             cv = 10, scoring = 'accuracy')
media = resultados.mean()
desvio = resultados.std()