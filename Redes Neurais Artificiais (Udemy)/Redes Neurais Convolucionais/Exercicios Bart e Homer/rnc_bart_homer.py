#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:18:39 2020

@author: yurifarod
"""

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator

classificador = Sequential()
classificador.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
classificador.add(MaxPooling2D(pool_size = (2, 2)))

classificador.add(Conv2D(32, (3, 3), activation = 'relu'))
classificador.add(MaxPooling2D(pool_size = (2, 2)))

classificador.add(Flatten())

classificador.add(Dense(units = 4, activation = 'relu'))
classificador.add(Dense(units = 4, activation = 'relu'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))
classificador.compile(optimizer = 'adamax', loss = 'binary_crossentropy', metrics = ['accuracy'])

gerador_treinamento = ImageDataGenerator(rescale = 1./255, rotation_range=7, 
                                         horizontal_flip = True, shear_range=0.2,
                                         height_shift_range=0.07, zoom_range=0.2)
gerador_teste = ImageDataGenerator(rescale = 1./255)

base_treinamento = gerador_treinamento.flow_from_directory('dataset_personagens/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 10,
                                                 class_mode = 'binary')
base_teste = gerador_teste.flow_from_directory('dataset_personagens/test_set',
                                            target_size = (64, 64),
                                            batch_size = 10,
                                            class_mode = 'binary')

classificador.fit_generator(base_treinamento, steps_per_epoch = 12, epochs = 4)