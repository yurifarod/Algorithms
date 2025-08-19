# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 20:56:46 2025

@author: yfdantas
"""

from collections import defaultdict

# ------------------------
# 1) Entrada como string
# ------------------------
texto = "Hadoop é rápido. Hadoop é escalável e Hadoop é confiável. hadoop é top!"

# ------------------------
# 2) Fase Map
# ------------------------
def mapper(texto):
    retorno = []
    # Normaliza o texto: minúsculas e remove pontuações simples
    for palavra in texto.lower().replace(".", "").split():
        retorno.append((palavra, 1))
    return retorno

# ------------------------
# 3) Shuffle (agrupamento por chave)
# ------------------------
def shuffle(mapped_values):
    #Gera um tipo dict para associar a chave (texto) ao valor!
    grupos = defaultdict(list)
    for chave, valor in mapped_values:
        grupos[chave].append(valor)
    return grupos

# ------------------------
# 4) Fase Reduce
# ------------------------
def reducer(grupos):
    retorno = []
    for chave, valores in grupos.items():
        retorno.append((chave, sum(valores)))
    return retorno

# ------------------------
# 5) Execução MapReduce
# ------------------------
# Map
mapped = list(mapper(texto))

# Shuffle
grouped = shuffle(mapped)

# Reduce
reduced = list(reducer(grouped))

# ------------------------
# 6) Resultado final
# ------------------------
print("Resultado do MapReduce (contagem de palavras):")
for palavra, contagem in reduced:
    print('%s: %d'%(palavra, contagem))
