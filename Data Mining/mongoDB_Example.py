#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 21:08:04 2021

@author: yurifarod
"""

#Importacao da lib
from pymongo import MongoClient;

conn = MongoClient()

#Conexao com o MongoDB
try:
    conn = MongoClient()
    print("Conexao Bem Sucedida")
except:
    print("Nao foi possivel conectar ao MongoDB")
    
db = conn.local

#Conexao com a base de dados
try:
    db = conn.unyleyadb
    print("Conexao à Base bem Sucedida")
except:
    print("Nao foi possivel conectar à Base de Dados")

#Criacao da Colecao Exercicio 01
collection = db.exercicio_01

#Insercao do primeiro registro que servira de modelo para todos os outros
new_model = {'aluno':'Yuri Faro', 'curso': 'Big Data', 'estado': 'Sergipe',
               'cidade':'Aracaju', 'idade':'30'}

data_insert = collection.insert_one(new_model)

#Insercao de mais um registro
new_register = {'aluno':'Claudio Silva', 'curso': 'Ciencia de Dados', 'estado': 'Sao Paulo',
               'cidade':'Sao Paulo', 'idade':'60'}

collection.insert_one(new_register)

#Insercao de mais um registro
new_register = {'aluno':'Ana Maria', 'curso': 'Business Intelligence', 'estado': 'Amazonas',
               'cidade':'Manaus', 'idade':'87'}

collection.insert_one(new_register)

#Exclusao de um registro, o que possui idade 87
collection.delete_one({'idade':'87'})

#Update de um registro, o que possui idade 30, mudaremos o seu curso
collection.update_one({'idade':'30'}, {'$set':{'curso':'MongoDB'}})

#Comando find para retornar todos os registros
cursor = collection.find()

#Impressao de todos os registros
for register in cursor:
    print(register)

#Vamos apegar a colecao, garantindo o mesmo resultado em toda execucao
collection.drop()