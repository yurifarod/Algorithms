# -*- coding: utf-8 -*-
"""
Author: Yúri (https://github.com/yurifarod)
        Mariana (https://github.com/marianaliraf)
        
Exemplo didático do funcionamento dos mais usuais algoritmos (modelos) de previsão para séries temporais!
Utiliza-se uma série temporal randômica e oferece uma visão comparática gráfica e em funçaõ do erro (MAPE).

Serão exemplificados o funcionamento base dos algoritmos:
    1. Holt-Winters
    2. ARIMA
    3. SVR
    4. ETS
    5. LSTM (Rede Neural Recorrente)
"""

import os
import random
import numpy as np
import matplotlib.pyplot as plt


def salvar_graficos(nome, previsao, cor, save_path, erro):
    plt.figure(figsize=(8, 4))
    plt.title(f"Previsão com {nome}")
    plt.plot(serie_treino, label='Série Treinamento', color="blue")
    plt.plot([None] * 90 + list(serie_teste), label='Série Real', color="pink")
    plt.plot([None] * 90 + list(previsao), label=f'{nome} (erro: {erro:.2f}%)', color=cor)
    plt.legend(loc='lower left') 
    plt.savefig(save_path)  
    plt.show()
    plt.close() 
    
def calcular_erro(real, previsto):
    real, previsto = np.array(real), np.array(previsto)
    return np.mean(np.abs((real - previsto) / real)) * 100


'''
Diretório para salvar gráfico
'''
output_dir = "./"
os.makedirs(output_dir, exist_ok=True)

'''
Criação da Série 
'''
serie_temporal = [random.randint(10, 100) for _ in range(100)]
serie_treino = serie_temporal[:90]
serie_teste = serie_temporal[90:]
intervalo = 10

'''
Exemplo de previsão com Holt-Winters e plotagem de gráfico
'''
from statsmodels.tsa.api import Holt

model_hw = Holt(serie_treino, exponential=False, damped=False)
model_fit_hw = model_hw.fit(smoothing_level=0.5, smoothing_slope=0.3, optimized=False, damping_slope=0.1)
previsto_hw = model_fit_hw.predict(start=len(serie_teste), end=len(serie_teste) + intervalo - 1)

erro_hw = calcular_erro(serie_teste, previsto_hw)

salvar_graficos("Holt-Winters", previsto_hw, "green", os.path.join(output_dir, "previsao_holt_winters.png"), erro_hw)

'''
Exemplo de previsão com ARIMA e plotagem de gráfico
'''
import pmdarima as pm

model_arima = pm.auto_arima(
    serie_treino, start_p=1, start_q=1, test='adf',
    max_p=3, max_q=3, m=1, d=None, seasonal=False,
    trace=True, error_action='ignore', suppress_warnings=True, stepwise=True
)
previsto_arima = model_arima.predict(n_periods=intervalo)

erro_arima = calcular_erro(serie_teste, previsto_arima)

salvar_graficos("Modelo Autoregressivo", previsto_arima, "red", os.path.join(output_dir, "previsao_arima.png"), erro_arima)

'''
Exemplo de previsão com SVR e plotagem de gráfico
'''
from sklearn.svm import SVR

svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
x_train = np.arange(len(serie_treino)).reshape(-1, 1)
svr.fit(x_train, serie_treino)
x_forecast = np.arange(len(serie_treino), len(serie_treino) + intervalo).reshape(-1, 1)
previsto_svr = svr.predict(x_forecast)

erro_svr = calcular_erro(serie_teste, previsto_svr)

salvar_graficos("SVR", previsto_svr, "orange", os.path.join(output_dir, "previsao_svr.png"), erro_svr)

'''
Exemplo de previsão com ETS e plotagem de gráfico
'''
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

model_ets = ETSModel(serie_treino, error='add', trend='add', seasonal=None)
model_fit_ets = model_ets.fit()
previsto_ets = model_fit_ets.forecast(intervalo)

erro_ets = calcular_erro(serie_teste, previsto_ets)

salvar_graficos("ETS", previsto_ets, "purple", os.path.join(output_dir, "previsao_ets.png"), erro_ets)


'''
Exemplo de previsão com RNR (LSTM) e plotagem de gráfico
'''
from keras.models import Sequential
from keras.layers import Dense, LSTM
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

serie_array = np.array(serie_treino).reshape(-1, 1)
generator = TimeseriesGenerator(serie_array, serie_array, length=1, batch_size=1)


model_lstm = Sequential([
    LSTM(2, activation='relu', input_shape=(1, 1)),
    Dense(1)
])
model_lstm.compile(optimizer='adam', loss='mse')


model_lstm.fit(generator, epochs=5, verbose=0)

previsto_lstm = []
input_seq = serie_array[-1].reshape(1, 1, 1)
for _ in range(intervalo):
    pred = model_lstm.predict(input_seq, verbose=0)
    previsto_lstm.append(pred[0][0])
    input_seq = np.array(pred).reshape(1, 1, 1)
    


erro_lstm = calcular_erro(serie_teste, previsto_lstm)

salvar_graficos("LSTM", previsto_lstm, "cyan", os.path.join(output_dir, "previsao_lstm.png"), erro_lstm)

'''
Plotando Gráfico com todas as previsões
'''
plt.figure(figsize=(10, 6))
plt.title("Comparativo de Previsões")
plt.plot(serie_treino, label='Série Treinamento', color="blue")
plt.plot([None] * 90 + list(serie_teste), label='Série Real', color="pink")
plt.plot([None] * 90 + list(previsto_hw), label=f'Holt-Winters (erro: {erro_hw:.2f}%)', color="green")
plt.plot([None] * 90 + list(previsto_arima), label=f'Modelo Autoregressivo (erro: {erro_arima:.2f}%)', color="red")
plt.plot([None] * 90 + list(previsto_svr), label=f'SVR (erro: {erro_svr:.2f}%)', color="orange")
plt.plot([None] * 90 + list(previsto_ets), label=f'ETS (erro: {erro_ets:.2f}%)', color="purple")
plt.plot([None] * 90 + list(previsto_lstm), label=f'LSTM (erro: {erro_lstm:.2f}%)', color="cyan")
plt.legend(loc='lower left')  
plt.savefig(os.path.join(output_dir, "comparativo_previsoes_com_erro.png"))
plt.show()





