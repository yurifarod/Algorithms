#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:18:17 2020

@author: yurifarod
"""
import random

#Tweak Simples
def simple_tweak(solucao, d, size_change):
    actual_sol = []
    for i in range(d):
        actual_sol.append(solucao[i])

    index = random.randrange(0, 100)

    for i in range(size_change):
        number = random.randrange(-100, 100)
        actual_sol[index] = number
        index += 1
        if index == 100:
            index = 0

    return actual_sol

def rosenbrock_function(solucao, aux, d, bias):
    custo = 0
    for i in range(d-1):
        number_1 = solucao[i] + aux[i]
        number_2 = solucao[i+1] + aux[i+1]
        custo += (100 * (number_1**2 - number_2)**2 + (number_1 - 1)**2)

    custo = custo + bias
    return custo
