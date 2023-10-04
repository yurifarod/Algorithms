#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:51:54 2021

@author: yurifarod

Modelo de codigo utilizado para agrupar entradas dict
"""

def group_by_owners(files):
    result = {}
    for file, owner in files.items():
        result[owner] = result.get(owner, []) + [file]
    return result

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))