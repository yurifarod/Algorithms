# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 09:46:18 2025

@author: yfdantas

Para demonstrar que metricas distintas podem eleger previsoes distintas como a 'melhor'
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
    data = np.random.randint(50, size=n)
    return data

def generate_trend_forecast(data):
    value = 20
    ind = int(len(data)/2)
    trend = []
    for i in range(ind):
        trend.append(data[i] + value)
    for i in range(ind, len(data)):
        trend.append(data[i] - (value*2))
    return trend

def generate_mae_forecast(data):
    value = 35
    mae = []
    for i in range(len(data)):
        if (i % 2 == 0):
            mae.append(data[i] + value)
        else:
            mae.append(data[i] - value)
    return mae

def generate_mape_forecast(data):
    avg = np.mean(data)
    mape = []
    for i in range(len(data)):
        if data[i] > avg:
            avg += np.random.randint(data[i] - avg)
        else:
            avg -= np.random.randint(avg - data[i])
        mape.append(avg)
    return mape
    

def plot_data(data, color, label):
    plt.plot(data, marker='o', color=color, label=label)
    

plt.figure(figsize=(10, 6))
serie_real = generate_data(30)
plot_data(serie_real, 'blue', 'Serie "real"')
forecast_trend = generate_trend_forecast(serie_real)
plot_data(forecast_trend, 'lightcoral', 'Trend')
forecast_mape = generate_mape_forecast(serie_real)
plot_data(forecast_mape, 'lightgreen', 'MAPE')
forecast_mae = generate_mae_forecast(serie_real)
plot_data(forecast_mae, 'lightgray', 'CFE')
plt.legend()
plt.show()
