# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:25:24 2021

@author: yfdantas
"""

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Data
#Array de Parametros
x = [2, 4, 5, 9, 9, 1, 2, 3, 6, 0, 1] #70

#Array de Custos
y = [1, 2, 3, 3, 5, 6, 7, 8, 1, 9, 0] #70
x = np.array(x)
y = np.array(y)

# Regression
results = sm.OLS(y,x).fit()
regLine_base  = x*results.params[0]




# Gerando Novos Pontos (Parametros)
x_teste = [14, 11, 12]
x_teste = np.array(x_teste)
regLine_gerado  = x_teste*results.params[0]

# PLot
plt.plot(x, y, 'o', label='data')
plt.plot(x, regLine_base, label='base line')
plt.plot(x_teste, regLine_gerado, label='generated line')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend();