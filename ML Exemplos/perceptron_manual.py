# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:57:21 2022

@author: yfdantas
"""

'''
1 1 = 1
0 1 = 0
1 0 = 0
0 0 = 0
'''

import numpy as np
from statistics import mean


def prediction(X, w, bias):
    #funcao de ativacao
    value =  np.dot(X, w) + bias
    return np.where(value>= 0.0, 1, 0)

def fit(epochs, tx_aprendizado, X, y):
    #Inicializando bias
    #bias = np.random.uniform(-1, 1)
    bias = -0.5
    #Inicializando pesos
    #w = np.random.uniform(-1, 1, (X.shape[1]))
    w = [0.25, 0.9]
    list_erros = []
    
    for i in range(epochs):
        print('Epoch ' +str(i))
        erro = 0
        for x, target in zip(X, y):
            previsto = prediction(x, w, bias)
            f_erro = tx_aprendizado * (target - previsto)
            bias += f_erro
            w += x * f_erro
            print(w, f_erro)
            erro += int(f_erro != 0.0)
            print('Previsto: %d - Valor Real: %d:' %(previsto.tolist(), target))
            #print('Erro: %d ' %(erro))
        list_erros.append(erro)
    return list_erros
    


X = [[1, 1], [0, 1], [1, 0], [0, 0], [1, 1], [0, 1], [1, 0], [0, 0]]
y = [1, 0, 0, 0, 1, 0, 0, 0]

#taxa de aprendizado
eta = 0.1
#iteracoes
epochs = 10

previsao = fit(epochs, eta, np.asarray(X), np.asarray(y))
print('---------------------------------------')
print('Erro Médio %d' %(mean(previsao)))




