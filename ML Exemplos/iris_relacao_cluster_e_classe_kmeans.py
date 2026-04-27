#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:01:16 2023
Naive Bayes
@author: yurifarod
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

base = pd.read_csv('datasets/iris.csv')

features = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)


kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(features)

kmeans_cluster = kmeans.labels_

df = pd.DataFrame({'Classe': classe, 'Cluster': kmeans.labels_})

# Heatmap
plt.figure(figsize = (7,7))
sns.heatmap(df.corr("spearman"), annot = True, cmap = "YlGnBu")
plt.title("Mapa de Correlação das Variáveis Numéricas\n", fontsize = 15)
plt.show()

X = df['Classe']
Y = df['Cluster']

# Tabela de contingência (frequência)
tabela = pd.crosstab(X, Y)

# Convertendo para porcentagem por linha (P(Y | X))
tabela_pct = tabela.div(tabela.sum(axis=1), axis=0)

# Plotando heatmap
sns.heatmap(tabela_pct, annot=True, cmap="Blues", fmt=".2f")

plt.title("Probabilidade da Classe dado o Cluster")
plt.xlabel("Cluster")
plt.ylabel("Classe")

plt.show()