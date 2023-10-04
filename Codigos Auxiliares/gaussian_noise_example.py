# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 08:44:57 2022

@author: yfdantas
"""

import numpy as np

#Cada elemento possui duas features
populacao = [[1, 2], [3, 4], [5, 0], [2, 6], [9, 1], [4, 7], [3, 6], [8, 2], [1, 9], [5, 2]]

first_feature = []
second_feature = []
for i in populacao:
    first_feature.append(i[0])
    second_feature.append(i[1])
    
media_first = np.mean(first_feature)
media_second = np.mean(second_feature)

std_first = np.std(first_feature)
std_second = np.std(second_feature)

ff = np.random.normal(media_first, std_first, 1)[0]
sf = np.random.normal(media_second, std_second, 1)[0]

novo_elemento = [ff, sf]