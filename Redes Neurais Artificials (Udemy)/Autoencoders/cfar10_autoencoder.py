#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:41:55 2020

@author: yurifarod
"""

import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import cifar10
from keras.models import Model, Sequential
from keras.layers import Input, Dense

(previsores_treinamento, _), (previsores_teste, _) = cifar10.load_data()
previsores_treinamento = previsores_treinamento.astype('float32') / 255
previsores_teste = previsores_teste.astype('float32') / 255

previsores_treinamento = previsores_treinamento.reshape((len(previsores_treinamento), np.prod(previsores_treinamento.shape[1:])))
previsores_teste = previsores_teste.reshape((len(previsores_teste), np.prod(previsores_teste.shape[1:])))

autoencoder = Sequential()

# Estrutura do encoder: 3072 - 1536 - 768 - 1536 - 3072
autoencoder.add(Dense(units = 1536, activation = 'relu', input_dim = 3072))
autoencoder.add(Dense(units = 768, activation='relu'))

#768 - 1536 - 3072
autoencoder.add(Dense(units = 1536, activation='relu'))
autoencoder.add(Dense(units = 3072, activation='sigmoid'))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy', metrics = ['accuracy'])
autoencoder.fit(previsores_treinamento, previsores_treinamento,
                epochs=200, batch_size=256, validation_data=(previsores_teste, previsores_teste))

dimensao_original = Input(shape=(3072,))
camada_encoder1 = autoencoder.layers[0]
camada_encoder2 = autoencoder.layers[1]
encoder = Model(dimensao_original, camada_encoder2(camada_encoder1(dimensao_original)))

imagens_codificadas = encoder.predict(previsores_teste)
imagens_decodificadas = autoencoder.predict(previsores_teste)

numero_imagens = 4
imagens_teste = np.random.randint(previsores_teste.shape[0], size=numero_imagens)
plt.figure(figsize=(18, 18))
for i, indice_imagem in enumerate(imagens_teste):
    eixo = plt.subplot(10, 10, i + 1)
    plt.imshow(previsores_teste[indice_imagem].reshape(32, 32, 3))
    plt.xticks(())
    plt.yticks(())
    
    eixo = plt.subplot(10, 10, numero_imagens + i + 1)
    plt.imshow(imagens_codificadas[indice_imagem].reshape(16, 16, 3))
    plt.xticks(())
    plt.yticks(())

    eixo = plt.subplot(10, 10, 2 * numero_imagens + i + 1)
    plt.imshow(imagens_decodificadas[indice_imagem].reshape(32, 32, 3))
    plt.xticks(())
    plt.yticks(())
plt.show()