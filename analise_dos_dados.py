#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:22:39 2021

@author: yurifarod
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv('KaggleV2-May-2016.csv')

#Tamanho do nosso dataset
df.shape

#Os primeiros 5 registros
df.head(5)

#Os ultimos 5 registros
df.tail(5)

#As colunas presentes
df.columns

#Informacoes sobre o nosso dataset em geral
df.info()

#A descricao da lib sobre o nosso dataset
df.describe()

#Contagem dos valores da coluna Alcoolismo
df['Alcoholism'].value_counts()

#criando uma figure, axes
fig, ax = plt.subplots()

#criando o gráfico de barras 
sns.barplot(x=df.index, y=df['No-show'], ax=ax, data=df)

#otimizar espaço da figure
fig.tight_layout();


sns.set(color_codes=True)
cor=df.corr()
cor
sns.heatmap(cor,annot=True)


labelencoder_df = LabelEncoder()
df['Neighbourhood'] = labelencoder_df.fit_transform(df['Neighbourhood'])
df['Gender'] = labelencoder_df.fit_transform(df['Gender'])
df['No-show'] = labelencoder_df.fit_transform(df['No-show'])

atributos = ['Gender','Age','Neighbourhood','Scholarship','Hipertension','Diabetes',
             'Alcoholism','Handcap','SMS_received']

atributos_prev= ['No-show']

X = df[atributos].values

y = df[atributos_prev].values

split_test_size = 0.20

X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, y, test_size = split_test_size)

modelNB = GaussianNB(priors=None, var_smoothing=1e-9)
modelNB.fit(X_treino, Y_treino)

previsoes = modelNB.predict(X_teste)

acuracia  = accuracy_score(Y_teste, previsoes)
matriz = confusion_matrix(Y_teste, previsoes)