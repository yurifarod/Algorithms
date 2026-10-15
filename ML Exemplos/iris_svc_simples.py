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

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(features, classe, test_size=0.25)

kernel = ['rbf', 'linear', 'sigmoid']
c_list = [1, 2, 2.5]

best_acc = 0
best_matriz = []
parametros = []
for k in kernel: 
	for c in c_list:
		classificador = SVC(kernel=k, C=c)
		classificador.fit(previsores_treinamento, classe_treinamento)


		previsoes = classificador.predict(previsores_teste)

		acuracia = accuracy_score(previsoes, classe_teste)
		matriz = confusion_matrix(previsoes, classe_teste)
		if acuracia > best_acc:
			best_acc = acuracia
			best_matriz = matriz
			parametros = [k, c]

print(best_acc)
print(best_matriz)
print(parametros)
