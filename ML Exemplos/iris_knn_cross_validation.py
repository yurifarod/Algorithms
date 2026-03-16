#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:01:16 2023
Naive Bayes
@author: yurifarod
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score

base = pd.read_csv('datasets/iris.csv')
features = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values


labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)

classificador = KNeighborsClassifier(n_neighbors=3)

resultados = cross_val_score(estimator = classificador,
                             X = features, y = classe,
                             cv = 10, scoring = 'accuracy')

'''
Resultados
'''
media = resultados.mean()
print("Media: "+ str(media))
desvio = resultados.std()
print("Desvio: "+desvio)