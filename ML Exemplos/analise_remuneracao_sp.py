#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: yurifarod
"""

#Importacao da lib
import pandas as pd
from pymongo import MongoClient
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

conn = MongoClient()

#Conexao com o MongoDB
try:
    conn = MongoClient()
    print("Conexao Bem Sucedida")
except:
    print("Nao foi possivel conectar ao MongoDB")
    
db = conn.local

#Conexao com a base de dados
try:
    db = conn.unyleyadb
    print("Conexao à Base bem Sucedida")
except:
    print("Nao foi possivel conectar à Base de Dados")

#Buscado a colecao das remuneracoes de SP
collection = db.remuneracaoSP

#Comando find para retornar todos os registros
cursor = collection.find()

dataset = pd.DataFrame(cursor)

dataset = dataset.drop(['FERIAS', 'VANTAGENS', 'LICENCA', 'ABONO', 'REDUTOR', 'TOTAL'], axis=1)

labelenconder = LabelEncoder()

dataset['ORGAO'] = labelenconder.fit_transform(dataset['ORGAO'])
dataset['CARGO'] = labelenconder.fit_transform(dataset['CARGO'])

dataset = dataset.to_numpy()

corpus = []
classe = []
for i in dataset:
    #orgao e salario
    corpus.append( (i[2], i[4]) )
    #cargo
    classe.append(i[3])

corpus_train, corpus_test, classe_train, classe_test = train_test_split(corpus, classe, test_size=0.25)


modelNB = GaussianNB(priors=None, var_smoothing=1e-9)
modelNB.fit(corpus_train, classe_train)

previsoes = modelNB.predict(corpus_test)

acuracia  = accuracy_score(classe_test, previsoes)
matriz = confusion_matrix(classe_test, previsoes)