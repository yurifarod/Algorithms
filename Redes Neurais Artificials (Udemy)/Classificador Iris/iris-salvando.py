#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:32:55 2019

@author: yurifarod
"""

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder

base = pd.read_csv('iris.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)
classe_dummy = np_utils.to_categorical(classe)

classificador = Sequential()
classificador.add(Dense(units = 8,
                        kernel_initializer = 'normal', 
                        activation = 'tanh', input_dim = 4))
    
classificador.add(Dense(units = 8, activation = 'tanh'))
    
classificador.add(Dense(units = 3, activation = 'softmax'))
    
classificador.compile(optimizer = 'sgd', loss = 'sparse_categorical_crossentropy',
                      metrics = ['accuracy'])
classificador.fit(previsores, classe, batch_size = 10, epochs = 150)

classificador_json = classificador.to_json()
with open('classificador_iris.json', 'w') as json_file:
    json_file.write(classificador_json)
classificador.save_weights('classificador_iris.h5')