#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:46:28 2020

@author: yurifarod
"""

import numpy as np
from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers import Input, Dense
from keras.utils import np_utils

(previsores_treinamento, classe_treinamento), (previsores_teste, classe_teste) = mnist.load_data()
previsores_treinamento = previsores_treinamento.astype('float32') / 255
previsores_teste = previsores_teste.astype('float32') / 255
classe_dummy_treinamento = np_utils.to_categorical(classe_treinamento)
classe_dummy_teste = np_utils.to_categorical(classe_teste)


previsores_treinamento = previsores_treinamento.reshape((len(previsores_treinamento), np.prod(previsores_treinamento.shape[1:])))
previsores_teste = previsores_teste.reshape((len(previsores_teste), np.prod(previsores_teste.shape[1:])))

# 784 - 32 - 784
autoencoder = Sequential()
autoencoder.add(Dense(units = 32, activation = 'relu', input_dim = 784))
autoencoder.add(Dense(units = 784, activation = 'sigmoid'))
autoencoder.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                    metrics = ['accuracy'])
autoencoder.fit(previsores_treinamento, previsores_treinamento,
                epochs = 50, batch_size = 256,
                validation_data = (previsores_teste, previsores_teste))

dimensao_original = Input(shape=(784,))
camada_encoder = autoencoder.layers[0]
encoder = Model(dimensao_original, camada_encoder(dimensao_original))

previsores_treinamento_codificados = encoder.predict(previsores_treinamento)
previsores_teste_codificados = encoder.predict(previsores_teste)

# sem reducao de dimensionalidade
c1 = Sequential()
c1.add(Dense(units = 397, activation = 'relu', input_dim = 784))
c1.add(Dense(units = 397, activation = 'relu'))
c1.add(Dense(units = 10, activation = 'softmax'))
c1.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
           metrics = ['accuracy'])
c1.fit(previsores_treinamento, classe_dummy_treinamento, batch_size = 256,
       epochs = 100, validation_data=(previsores_teste, classe_dummy_teste))

# com reducao de dimensionalidade
c2 = Sequential()
c2.add(Dense(units = 21, activation = 'relu', input_dim = 32))
c2.add(Dense(units = 21, activation = 'relu'))
c2.add(Dense(units = 10, activation = 'softmax'))
c2.compile(optimizer = 'adam', loss = 'categorical_crossentropy',
           metrics = ['accuracy'])
c2.fit(previsores_treinamento_codificados, classe_dummy_treinamento, batch_size = 256,
       epochs = 100, validation_data=(previsores_teste_codificados, classe_dummy_teste))