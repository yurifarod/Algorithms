#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:08:27 2023

@author: yurifarod
"""

import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from statsmodels.stats.stattools import jarque_bera

#Libs com os modelos de previsao
import statsmodels.api as sm
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

#Ignorar as Warnings do Codigo
import warnings
warnings.filterwarnings("ignore")

def previsao_ets(desp_serie, intervalo, parametros):

    error = parametros[0]
    trend = parametros[1]
    seasonal = parametros[2]
    initialization = parametros[3]
    seasonal_periods = parametros[4]

    arr_real =[]
    inter_real = []

    for i in range(intervalo):
        max_size = max(desp_serie.index)
        arr_real.append(desp_serie[max_size])
        inter_real.append(max_size)
        desp_serie = desp_serie.drop(max_size)

    model = ETSModel(desp_serie, error=error, trend=trend, seasonal=seasonal,
                     initialization_method=initialization, seasonal_periods=seasonal_periods)
    model_fit = model.fit(disp=0)

    start = len(desp_serie)
    end = len(desp_serie)+intervalo-1

    previsto = model_fit.predict(start = start, end = end)
    serie_real = Series(arr_real, inter_real)
    #Invertendo a serie
    serie_real = serie_real.iloc[::-1]

    size = len(previsto)
    erro = []

    for i in range(size):
        parc_erro = (previsto[i] - serie_real[i])/serie_real[i]
        erro.append(abs(parc_erro))

    erro_medio = np.mean(erro)
    return abs(erro_medio), previsto, model_fit

def previsao_arima(desp_serie, intervalo, parametros):

    measurement_error = parametros[0]
    time_varying_regression = parametros[1]
    enforce_stationarity = parametros[2]
    mle_regression = False
    concentrate_scale = parametros[3]
    cov_type = parametros[4]
    method = parametros[5]
    p = parametros[6]
    d = parametros[7]
    q = parametros[8]
    trend_offset = parametros[9]
    #prefixados
    order = (p,d,q)
    #Removendo a sazonalidade!
    seasonal_order = (0,0,0,0)
    arr_exog = None

    arr_real =[]
    inter_real = []
    for i in range(intervalo):
        max_size = max(desp_serie.index)
        arr_real.append(desp_serie[max_size])
        inter_real.append(max_size)
        desp_serie = desp_serie.drop(max_size)

    model = sm.tsa.statespace.SARIMAX(desp_serie,
                                      exog=arr_exog,
                                      order=order,
                                      seasonal_order=seasonal_order,
                                      mle_regression=mle_regression,
                                      hamilton_representation=False,
                                      simple_differencing=False,
                                      measurement_error=measurement_error,
                                      time_varying_regression=time_varying_regression,
                                      enforce_stationarity=enforce_stationarity,
                                      enforce_invertibility=False,
                                      concentrate_scale=concentrate_scale,
                                      initialization='approximate_diffuse',
                                      trend_offset=trend_offset)
    model_fit = model.fit(disp=0,
                          cov_type=cov_type,
                          method=method)

    start = len(desp_serie)
    end = len(desp_serie)+intervalo-1

    previsto = model_fit.predict(start = start, end = end)
    serie_real = Series(arr_real, inter_real)
    #Invertendo a serie
    serie_real = serie_real.iloc[::-1]

    size = len(previsto)
    erro = []

    for i in range(size):
        parc_erro = (previsto[i] - serie_real[i])/serie_real[i]
        erro.append(abs(parc_erro))

    erro_medio = np.mean(erro)
    return abs(erro_medio), previsto, model_fit

class_file = './dataset/yahoo_stock.csv'
df = pd.read_csv(class_file, index_col=False, sep=',')
df.drop('High', inplace=True, axis=1)
df.drop('Low', inplace=True, axis=1)
df.drop('Open', inplace=True, axis=1)
df.drop('Volume', inplace=True, axis=1)
df.drop('Adj Close', inplace=True, axis=1)

df.index = pd.to_datetime(df.Date, format="%Y-%m-%d")
df.drop("Date", inplace=True, axis=1)

serie_original = df.iloc[:,0]
serie_size = len(serie_original)
intervalo = 15
'''
Aqui iniciamos os testes com a serie afim de tirar os parametros adequados!

Primeiro faremos o Augmented Dickey-Fuller test
Depois faremos o teste de diferenciação para descobrir o momento de estacionariedade da série
Após isso faremos a autocorrelação parcial para achar o de autoregressão
Por último faremos o teste de correlação para encontrar o número de erros de previsão defasados na equação de previsão.
'''
from statsmodels.tsa.stattools import adfuller

result_test_adfuller = adfuller(serie_original)
print('ADF Statistic: %f' % result_test_adfuller[0])
print('p-value: %f' % result_test_adfuller[1])

if result_test_adfuller[1] > 0.05:
    print('Serie não estacionária!')

print('Critical Values:')

for key, value in result_test_adfuller[4].items():
  print('\t%s: %.3f' % (key, value))
  
# Original Series
fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(serie_original); ax1.set_title('Original Series'); ax1.axes.xaxis.set_visible(False)
# 1st Differencing
ax2.plot(serie_original.diff()); ax2.set_title('1st Order Differencing'); ax2.axes.xaxis.set_visible(False)
# 2nd Differencing
ax3.plot(serie_original.diff().diff()); ax3.set_title('2nd Order Differencing')
plt.show()

from statsmodels.graphics.tsaplots import plot_acf
fig, (ax1, ax2, ax3) = plt.subplots(3)
plot_acf(serie_original, ax=ax1)
plot_acf(serie_original.diff().dropna(), ax=ax2)
plot_acf(serie_original.diff().diff().dropna(), ax=ax3)

print('A serie parece eter menos ruidos na primeira diferenciação! Manteremos D = 1')

from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(serie_original.diff().dropna())

print('A serie tem pico de autocorrelação em P = 1')

plot_acf(serie_original.diff().dropna())

print('A serie tem picos fora de faixa em Q = 18')



'''
Aqui iniciamos a previsao utilizando o modelo ETS
'''
v_erro = ['add', 'mul']
v_trend = ['add', 'mul']
v_seasonal = ['add', 'mul']
v_init = ['estimated', 'heuristic']
v_period = [18]

best_vlerro = 99
best_para = []
best_prev = []
modelo = ''
for erro in v_erro:
    for trend in v_trend:
        for seasonal in v_seasonal:
            for init in v_init:
                for period in v_period:
                    parametros = [erro, trend, seasonal, init, period]
                    vlerro, serie_prevista, modelo = previsao_ets(serie_original, intervalo, parametros)
                    
                    if vlerro < best_vlerro:
                        best_vlerro = vlerro
                        best_param = parametros
                        best_prev = serie_prevista

#Para uso no intervalo de confiança
x = best_prev.index
y = best_prev.values

plt.figure(figsize=(16,8))
serie_original[serie_size-2*intervalo:serie_size].plot(label=None)
best_prev.plot(label='ETS Model')
plt.fill_between(x, y*0.95, y+(y*0.05), color='g', alpha=.1)
plt.fill_between(x, y*0.8, y+(y*0.2), color='r', alpha=.1)
plt.title('MAPE Encontrado na Previsão: '+str(round(best_vlerro*100, 2))+'%')
plt.show()

print('============ Melhores Parametros ============')

print(best_param)

print('============ Analise de Ruido ============')
print(' '*254)
teste_ruido = jarque_bera(modelo.resid)
print('Estatística Jarque-Bera :', teste_ruido[0])
print('P-valor :', teste_ruido[1])
print('Assimetria :', teste_ruido[2])
print('Curtose :',teste_ruido[3])



'''
Aqui iniciamos a previsao utilizando o modelo ARIMA (sarima zerado na sazonalidade)
'''
v_measurement_error = [True, False]
v_time_varying_regression = [True, False]
v_enforce_stationarity = [True, False]
v_concentrate_scale = [True, False]
v_cov_type = ['approx']
v_method = ['bfgs', 'cg']
v_p = [1]
v_d = [1]
v_q = [18]
v_trend = [1]

best_vlerro = 99
best_para = []
best_prev = []
modelo = ''
for measurement_error in v_measurement_error:
    for time_varying in v_time_varying_regression:
        for enforce in v_enforce_stationarity:
            for concentrate in v_concentrate_scale:
                for conv_type in v_cov_type:
                    for method in v_method:
                        for p in v_p:
                            for d in v_d:
                                for q in v_q:
                                    for trend in v_trend:
                                        parametros = [measurement_error, time_varying, enforce, concentrate, conv_type, method, p, d, q, trend]
                                        vlerro, serie_prevista, modelo = previsao_arima(serie_original, intervalo, parametros)
                                        
                                        if vlerro < best_vlerro:
                                            best_vlerro = vlerro
                                            best_param = parametros
                                            best_prev = serie_prevista
                    
                    

#Para uso no intervalo de confiança
x = best_prev.index
y = best_prev.values

plt.figure(figsize=(16,8))
serie_original[serie_size-2*intervalo:serie_size].plot(label=None)
best_prev.plot(label='ARIMA Model')
plt.fill_between(x, y*0.95, y+(y*0.05), color='g', alpha=.1)
plt.fill_between(x, y*0.8, y+(y*0.2), color='r', alpha=.1)
plt.title('MAPE Encontrado na Previsão: '+str(round(best_vlerro*100, 2))+'%')
plt.show()

print('============ Melhores Parametros ============')

print(best_param)

print('============ Analise de Ruido ============')
print(' '*254)
teste_ruido = jarque_bera(modelo.resid)
print('Estatística Jarque-Bera :', teste_ruido[0])
print('P-valor :', teste_ruido[1])
print('Assimetria :', teste_ruido[2])
print('Curtose :',teste_ruido[3])
