#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:20:05 2019

@author: yurifarod
"""
import pandas as pd
import tensorflow
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import confusion_matrix, accuracy_score

#Entrada das bases de teste e avaliação
previsores = pd.read_csv('entradas-breast.csv')
classe = pd.read_csv('saidas-breast.csv')

#Define o que é teste e o que é avaliação
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25)

#Cria rede neural
entrada = 30
saida = 1
tRedeInterna = (int)((entrada + saida)/2)

classificador = Sequential()

#camada entrada e oculta
classificador.add(Dense(units = tRedeInterna,
                        activation = 'relu',
                        kernel_initializer = 'random_uniform',
                        input_dim = entrada))

#mais uma oculta
classificador.add(Dense(units = tRedeInterna,
                        activation = 'relu',
                        kernel_initializer = 'random_uniform'))

#camada de saida
classificador.add(Dense(units = saida, activation = 'sigmoid'))

#o metodo Adam é um otimizador da descida do gradiente
#Documentação pode ser encontrada em keras.io
#Na versao inicial optimizer = 'adam', agora fizemos um otimizador

otimizador = tensorflow.keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy',
                      metrics = ['binary_accuracy'])

#Aqui treinamos a Rede
classificador.fit(previsores_treinamento,
                  classe_treinamento,
                  batch_size = 10,
                  epochs = 100)

#Aqui fazemos a previsão
previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)

#Agora vamos medir a acurácia da rede
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)

resultado = classificador.evaluate(previsores_teste, classe_teste)

#Podemos atestar que nessa RNA a adição de mais uma camada foi prejudicial

#outro codigo tem impressao dos valores dos pesos para cada camada implementada
