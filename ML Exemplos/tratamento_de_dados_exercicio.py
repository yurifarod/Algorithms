import pandas as pd
import numpy as np

dados = {
    "id_funcionario": range(1,31),

    "cargo": [
        "Pedreiro","Servente","Eletricista","Pedreiro","Mestre de Obras",
        "Servente","Encanador","Pedreiro","Eletricista","Servente",
        "Carpinteiro","Pedreiro","Servente","Encanador","Pedreiro",
        "Eletricista","Servente","Carpinteiro","Pedreiro","Servente",
        "Pedreiro","Eletricista","Servente","Encanador","Pedreiro",
        "Servente","Carpinteiro","Pedreiro","Eletricista","Servente"
    ],

    "anos_experiencia": [
        10,2,5,8,np.nan,
        1,7,12,6,3,
        9,11,np.nan,4,15,
        6,2,10,8,1,
        20,5,3,7,9,
        np.nan,13,14,6,2
    ],

    "horas_semanais": [
        44,40,44,50,60,
        38,44,45,np.nan,40,
        44,48,36,44,55,
        42,40,46,44,39,
        60,43,40,np.nan,44,
        35,50,52,41,38
    ],

    "faltas_mes": [
        0,2,1,0,3,
        4,1,0,2,np.nan,
        1,0,3,2,0,
        1,4,0,1,5,
        0,2,3,1,np.nan,
        4,0,1,2,3
    ],

    "setor": [
        "estrutura","estrutura","eletrica","estrutura","gestao",
        "estrutura","hidraulica","estrutura","eletrica","estrutura",
        "madeira","estrutura","estrutura","hidraulica","estrutura",
        "eletrica","estrutura","madeira","estrutura","estrutura",
        "estrutura","eletrica","estrutura","hidraulica","estrutura",
        "estrutura","madeira","estrutura","eletrica","estrutura"
    ],

    "salario": [
        3500,1800,3200,3400,7000,
        1700,3100,3600,3300,1900,
        3000,3700,2000,np.nan,4000,
        3400,1800,3200,3500,1600,
        4500,3300,2100,3100,3800,
        1700,3600,3900,3400,2000
    ],

    "desempenho": [
        "alto","medio","alto","alto","alto",
        "baixo","medio","alto","medio","baixo",
        "alto","alto","medio","medio","alto",
        "alto","baixo","alto","medio","baixo",
        "alto","medio","baixo","medio","alto",
        "baixo","alto","alto","medio","baixo"
    ]
}

df = pd.DataFrame(dados)

print(df.head())
print("\nInformações da base:")
print(df.info())