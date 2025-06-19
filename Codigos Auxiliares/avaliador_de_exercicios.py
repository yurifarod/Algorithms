# -*- coding: utf-8 -*-
"""
Created on Wed May 28 10:40:03 2025

@author: yfdantas
"""
import os
import subprocess
from fuzzywuzzy import fuzz

def rename_files(folder, list_files):
	for i in range(len(list_files)):
		new_file_name = list_files[i].replace('.txt', '.c')
		os.rename(folder + list_files[i], folder + new_file_name)
		list_files[i] = new_file_name
	return list_files

def text_processing(text):
    text = ' '.join(text.splitlines())
    text = text.replace(' ', '')
    return text

def collect_exercise_files(directory):
    list_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            list_files.append(file)
    return list_files

def collect_text_files(list_files):
    files = []
    for file in list_files:
        try:
            text = open(folder + file).read()
            text = text_processing(text)
            files.append(text)
        except:
            print('Erro de leitra em: ', file)
            files.append('Erro')
    return files
            
def list_levshtein_similar_files(files, fator_similaridade):
    remove_files = []

    for i in range(0, len(files)):
        for j in range(0, len(files)):
            if i != j:
                lev_value = fuzz.ratio(files[i],files[j])
                if (lev_value > fator_similaridade) and (j not in remove_files):
                   remove_files.append(j)
                if (list_files[i] == 'base_de_correcao.c') and (lev_value < 5):
                   remove_files.append(j)
                    
    return remove_files

'''
95 - Exercicio simples
85 - Exercicio mediano
75 - Exercicio complexo

Aquivo com similaridade menor que 5 do arquivo base, provavelmente enviou qlqr coisa
O arquivo base pode ser uma resolucao correta para o problema
'''
fator_similaridade = 90

folder = '/home/folder/'

list_files = collect_exercise_files(folder)

list_files = rename_files(folder, list_files)

files= collect_text_files(list_files)

'''
Primeira correcao, similaridade de codigos
'''
remove_files = list_levshtein_similar_files(files, fator_similaridade)

'''
Segunda correcao, compilacao de codigos
'''
for i in range(0, len(files)):
    command = 'gcc '+ '"' + folder + list_files[i] + '"'
    try:
        returned_value = subprocess.run(command, capture_output=True, check=True, shell=True).stdout 
    except:
        if(i not in remove_files):
            remove_files.append(i)

print('########################')
print('Arquivos para correcao ')
print('########################')

correcao_lista = []
for i in range(len(list_files)):
    if i not in remove_files:
        correcao_lista.append(list_files[i])

correcao_lista.sort()
for arquivo in correcao_lista:
    print(arquivo)