# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:50:13 2020

Algoritmo para validação de CNPJ. Faz uso da regra encontrada em: http://www.macoratti.net/alg_cnpj.htm

@author: yfdantas
"""

cnpj = '11222333000181'

raiz_cnpj = cnpj[0:12]
digito_ver = cnpj[12:14]

ver = int(raiz_cnpj[0])*5
ver += int(raiz_cnpj[1])*4
ver += int(raiz_cnpj[2])*3
ver += int(raiz_cnpj[3])*2
ver += int(raiz_cnpj[4])*9
ver += int(raiz_cnpj[5])*8
ver += int(raiz_cnpj[6])*7
ver += int(raiz_cnpj[7])*6
ver += int(raiz_cnpj[8])*5
ver += int(raiz_cnpj[9])*4
ver += int(raiz_cnpj[10])*3
ver += int(raiz_cnpj[11])*2

ver_resto = ver % 11

digito_1 = 0;

if ver_resto < 2:
    digito_1 = 0
else:
    digito_1 = 11-ver_resto

ver = int(raiz_cnpj[0])*6
ver += int(raiz_cnpj[1])*5
ver += int(raiz_cnpj[2])*4
ver += int(raiz_cnpj[3])*3
ver += int(raiz_cnpj[4])*2
ver += int(raiz_cnpj[5])*9
ver += int(raiz_cnpj[6])*8
ver += int(raiz_cnpj[7])*7
ver += int(raiz_cnpj[8])*6
ver += int(raiz_cnpj[9])*5
ver += int(raiz_cnpj[10])*4
ver += int(raiz_cnpj[11])*3
ver += digito_1 * 2

ver_resto = ver % 11

digito_2 = 0;

if ver_resto < 2:
    digito_2 = 0
else:
    digito_2 = 11-ver_resto
    
digito_calc = str(digito_1) + str(digito_2)

if digito_calc == digito_ver:
    print('CNPJ Válido: '+cnpj)
else:
    print('CNPJ Inválido: '+cnpj)