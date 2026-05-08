#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:19:02 2019

@author: yurifarod
"""
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

#Entrada das bases de teste e avaliação
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

#Definimos um metodo de criacao da RNA para ser usado posteriormente
def criarRede():
    classificador = Sequential()
    classificador.add(Dense(units = 8, activation = 'relu', 
                            kernel_initializer = 'normal', input_dim = 30))
    
    #add droupout para evitar overfiting
    classificador.add(Dropout(0.2))
    classificador.add(Dense(units = 8, activation = 'relu', 
                            kernel_initializer = 'normal'))
    classificador.add(Dense(units = 1, activation = 'sigmoid'))
    
    
    classificador.add(Dropout(0.2))
    
    #otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
    classificador.compile(optimizer = 'adamax', loss = 'binary_crossentropy',
                          metrics = ['binary_accuracy'])
    return classificador

classificador = KerasClassifier(build_fn = criarRede,
                                epochs = 100,
                                batch_size = 5)
resultados = cross_val_score(estimator = classificador,
                             X = previsores, y = classe,
                             cv = 10, scoring = 'accuracy')
media = resultados.mean()
desvio = resultados.std()