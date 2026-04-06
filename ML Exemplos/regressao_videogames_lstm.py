import pandas as pd
import numpy as np
from keras.layers import Dense, Input
from keras.models import Model

# =========================
# DATA LOADING & CLEANING
# =========================
base = pd.read_csv('datasets/games.csv')

base = base.drop(['Other_Sales', 'Developer'], axis=1)
base = base.drop(['NA_Sales', 'EU_Sales', 'JP_Sales'], axis=1)

base = base.dropna(axis=0)
base = base.loc[base['Global_Sales'] > 1]

nome_jogos = base['Name']
base = base.drop('Name', axis=1)

# =========================
# FEATURES & TARGET
# =========================
X = base.drop('Global_Sales', axis=1)
y = base['Global_Sales'].values

# =========================
# ENCODING (MODERN WAY)
# =========================
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# categorical column indices (based on X)
categorical_cols = [0, 2, 3, 8]

ct = ColumnTransformer(
    transformers=[
        ("encoder", OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'
)

X = ct.fit_transform(X)

# Convert to dense if needed (Keras usually prefers dense)
X = X.toarray() if hasattr(X, "toarray") else X

# =========================
# MODEL
# =========================
input_dim = X.shape[1]

camada_entrada = Input(shape=(input_dim,))
camada_oculta1 = Dense(units=50, activation='sigmoid')(camada_entrada)
camada_oculta2 = Dense(units=50, activation='sigmoid')(camada_oculta1)
camada_saida = Dense(units=1, activation='linear')(camada_oculta2)

regressor = Model(inputs=camada_entrada, outputs=camada_saida)

regressor.compile(optimizer='adam', loss='mean_squared_error')

regressor.fit(X, y, epochs=100, batch_size=100)

previsoes = regressor.predict(X)

print(previsoes)