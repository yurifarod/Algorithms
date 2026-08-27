# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:25:24 2021

@author: yfdantas
"""

import random
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Data
#Array de Parametros
x = [random.randint(1, 100) for _ in range(50)]
#Array de Custos
y = [random.randint(1, 100) for _ in range(50)]
x = np.array(x)
y = np.array(y)

# Regression
results = sm.OLS(y,x).fit()
regLine_base  = x*results.params[0]




# Gerando Novos Pontos (Parametros)
x_teste = [101, 102, 103, 104, 105, 106, 107]
x_teste = np.array(x_teste)
regLine_gerado  = x_teste*results.params[0]

# PLot
plt.plot(x, y, 'o', label='data')
plt.plot(x, regLine_base, label='base line')
plt.plot(x_teste, regLine_gerado, label='generated line')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend();

print(regLine_gerado)