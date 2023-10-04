#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:39:10 2019

@author: yurifarod
"""

import numpy as np
from keras.models import model_from_json

arquivo = open('classificador_iris.json', 'r')
estrutura_rede = arquivo.read()
arquivo.close()

classificador = model_from_json(estrutura_rede)
classificador.load_weights('classificador_iris.h5')

novo = np.array([[4.9, 3.0, 1.4, 0.2]])
previsao = classificador.predict(novo)
previsao = (previsao > 0.5)
print(previsao)