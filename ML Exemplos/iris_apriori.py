# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:20:12 2026

@author: yfdantas

Transformar valores numéricos em categorias.

Exemplo:

petal length
1.4
5.1

vira:

petal length
pequena
grande
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

'''
Transformando valores numéricos
em categorias:
baixo, médio, alto
'''
for coluna in df.columns:

    df[coluna] = pd.qcut(
        df[coluna],
        q=3,
        labels=[
            f"{coluna}_baixo",
            f"{coluna}_medio",
            f"{coluna}_alto"
        ]
    )

print("\n=== Dados categorizados ===")
print(df.head())


df_encoded = pd.get_dummies(df)

print("\n=== Dados binários ===")
print(df_encoded.head())


frequent_itemsets = apriori(
    df_encoded,
    min_support=0.3,
    use_colnames=True
)

print("\n=== Itemsets frequentes ===")
print(frequent_itemsets)

rules = association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.7
)

print("\n=== Regras encontradas ===")

print(
    rules[
        [
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]
    ]
)