# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:40:36 2026

@author: yfdantas
"""

import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.metrics import confusion_matrix, accuracy_score

base = pd.read_csv('datasets/iris.csv')
features = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values


labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)

previsores_teste, previsores_treinamento, classe_teste, classe_treinamento = train_test_split(features, classe, test_size=0.25)


classificador = SVC(kernel='linear')
classificador.fit(previsores_treinamento, classe_treinamento)


previsoes = classificador.predict(previsores_teste)

acuracia = accuracy_score(previsoes, classe_teste)
print("Acuracia do modelo: %.2f"%acuracia)

matriz = confusion_matrix(previsoes, classe_teste)
print(matriz)
