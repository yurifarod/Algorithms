# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:17:43 2023

@author: yfdantas
"""

text = 'Texto grande de teste para ver aqui como fazer esse Texto virar um Texto de uma parada aqui!'

def codificar(text): 
    first_list = text.split()
    
    second_list = []
    for term in first_list:
        j = 0
        if term not in second_list:
            second_list.append(term)
    
    first_matrix = []
    j = 0
    for term in second_list:
        first_matrix.append([j])
        index = second_list.index(term)
        j += 1
        
        for i in range(len(first_list)):
            if term == first_list[i]:
                first_matrix[index].append(i)
                
    #Se der tempo preenche com -1 o espaco vazio
    return first_matrix, second_list

encode, dicionario = codificar(text)