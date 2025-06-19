# -*- coding: utf-8 -*-
"""
Created on Wed May 28 10:40:03 2025

@author: yfdantas
"""
import os
import subprocess
from fuzzywuzzy import fuzz

def rename_files(folder, list_files):
	for file in list_files:
		new_file_name = file.replace('.txt', '.c')
		os.rename(folder + file, folder + new_file_name)
		file = new_file_name
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
        text = open(folder + file).read()
        text = text_processing(text)
        files.append(text)
    return files
            
def list_levshtein_similar_files(files):
    remove_files = []

    for i in range(0, len(files)):
        for j in range(0, len(files)):
            if i != j:
                lev_value = fuzz.ratio(files[i],files[j])
                if (lev_value > 85) and (j not in remove_files):
                   remove_files.append(j)
    return remove_files

folder = '/home/directory/'

list_files = collect_exercise_files(folder)

files = rename_files(folder, list_files)

files= collect_text_files(list_files)

'''
Primeira correcao, similaridade de codigos
'''
remove_files = list_levshtein_similar_files(files)

'''
Segunda correcao, compilacao de codigos
'''
for i in range(0, len(files)):
    command = 'gcc '+ '"' + folder + list_files[i] + '"'
    #returned_value = subprocess.call("cd "+ folder, shell=True)
    try:
        returned_value = subprocess.run(command, capture_output=True, check=True, shell=True).stdout 
    except:
        if(i not in remove_files):
            remove_files.append(i)

print('########################')
print('Arquivos para correcao ')
print('########################')
for i in range(len(list_files)):
    if i not in remove_files:
        print(list_files[i])
