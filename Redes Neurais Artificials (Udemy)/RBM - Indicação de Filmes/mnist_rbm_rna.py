#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:27:50 2020

@author: yurifarod
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.neural_network import BernoulliRBM
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

# Carregamento dos dados
digits = datasets.load_digits()
previsores = np.asarray(digits.data, 'float32')
classe = digits.target

# Normalizacao na escala entre 0 e 1
normalizador = MinMaxScaler(feature_range = (0,1))
previsores = normalizador.fit_transform(previsores)

# Divisao da base entre treinamento e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.2, random_state=0)

# Criacao e configuracao da Restricted Boltzmann Machine
rbm = BernoulliRBM(random_state=0)
rbm.n_iter = 25
rbm.n_components = 50

# Criacao e configuracao da rede neural usando o scikit-learn
# O parametro hidden_layer_sizes cria as camadas escondidas, sendo que cada numero
# 37 representa uma camada. Neste exemplo temos duas camadas escondidas com 37 
# neuronios cada uma - usada a formula (entradas + sai­das) / 2 = (64 + 10) / 2 = 37
# No scikit-learn nao e necessario configurar a camada de sai­da, pois ele 
# faz automaticamente. Definimos o max_iter com no maximo 1000 epocas, porem,
# quando a loos function nao melhora depois de um certo numero de rodadas ele
# para a execucao. O parametro verbosa mostra as mensagens na tela
mlp_rbm = MLPClassifier(hidden_layer_sizes = (37, 37),
                        activation = 'relu', 
                        solver = 'adam',
                        batch_size = 50,
                        max_iter = 1000,
                        verbose = 1)

# Criacao do pipeline para executarmos o rbm e logo apos o mlp
classificador_rbm = Pipeline(steps=[('rbm', rbm), ('mlp', mlp_rbm)])
classificador_rbm.fit(previsores_treinamento, classe_treinamento)

# Previsoes usando rbm + mlp
previsoes_rbm = classificador_rbm.predict(previsores_teste)
precisao_rbm = metrics.accuracy_score(previsoes_rbm, classe_teste)

# Criacao da rede neural simples sem aplicaÃ§Ã£o de rbm
mlp_simples = MLPClassifier(hidden_layer_sizes = (37, 37),
                        activation = 'relu', 
                        solver = 'adam',
                        batch_size = 50,
                        max_iter = 1000,
                        verbose = 1)
mlp_simples.fit(previsores_treinamento, classe_treinamento)
previsoes_mlp = mlp_simples.predict(previsores_teste)
precisao_mlp = metrics.accuracy_score(previsoes_mlp, classe_teste)

print('Previsao com RBM: '+str(precisao_rbm))
print('Previsao sem RBM: '+str(precisao_mlp))