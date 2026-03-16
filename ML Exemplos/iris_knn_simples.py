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
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

base = pd.read_csv('datasets/iris.csv')
features = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values


labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)

features_teste, features_treinamento, classe_teste, classe_treinamento = train_test_split(features, classe, test_size=0.25)


classificador = KNeighborsClassifier(n_neighbors=3)
classificador.fit(features_treinamento, classe_treinamento)

previsoes = classificador.predict(features_teste)

acuracia = accuracy_score(previsoes, classe_teste)
print("Acuracia do modelo: %.2f"%acuracia)

matriz = confusion_matrix(previsoes, classe_teste)

print(matriz)
