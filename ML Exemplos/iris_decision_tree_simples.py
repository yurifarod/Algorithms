# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:40:36 2026

@author: yfdantas
"""

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

iris = load_iris()
features = iris.data
classe = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)

previsores_teste, previsores_treinamento, classe_teste, classe_treinamento = train_test_split(features, classe, test_size=0.25)


classificador = clf = DecisionTreeClassifier(criterion='gini')
classificador.fit(previsores_treinamento, classe_treinamento)


previsoes = classificador.predict(previsores_teste)

acuracia = accuracy_score(previsoes, classe_teste)
print("Acuracia do modelo: %.2f"%acuracia)

matriz = confusion_matrix(previsoes, classe_teste)
print(matriz)

plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()
