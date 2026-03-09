import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# -------------------------------
# 1. Criando um dataframe fictício
# -------------------------------

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor"],
    "idade": [15, 16, 15, 17, np.nan, 16, 18, 17, 15],
    "horas_estudo": [2, 4, np.nan, 5, 3, 4, 6, 2, 3],
    "faltas": [5, 2, 3, np.nan, 4, 1, 0, 6, 2],
    "media": [3.5, 7.0, 4.5, 8.0, 6.5, np.nan, 9.0, 3.8, 5.2]
}

df = pd.DataFrame(dados)

# -------------------------------
# 2. Criando o TARGET (situação)
# -------------------------------

def classificar(media):
    if media < 4:
        return "reprovado"
    elif media < 6:
        return "recuperacao"
    else:
        return "aprovado"

df["situacao"] = df["media"].apply(lambda x: classificar(x) if pd.notnull(x) else np.nan)

print("DataFrame original:")
print(df)

# -------------------------------
# 3. Tratamento de Missing Values
# -------------------------------

colunas_numericas = ["idade", "horas_estudo", "faltas", "media"]

for col in colunas_numericas:
    media = df[col].mean()
    df[col].fillna(media, inplace=True)

# atualizar situacao após preenchimento da média
df["situacao"] = df["media"].apply(classificar)

print("\nApós tratamento de missing values:")
print(df)

# -------------------------------
# 4. Normalização Min-Max
# -------------------------------

scaler = MinMaxScaler()

df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])

print("\nApós normalização Min-Max:")
print(df)

# -------------------------------
# 5. One-Hot Encoding do TARGET
# -------------------------------

target_encoded = pd.get_dummies(df["situacao"], prefix="situacao")

df_final = pd.concat([df.drop(["situacao", "nome"], axis=1), target_encoded], axis=1)

print("\nDataFrame final preparado para ML:")
print(df_final)