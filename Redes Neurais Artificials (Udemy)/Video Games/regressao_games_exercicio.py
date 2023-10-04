import pandas as pd
from keras.layers import Dense, Input
from keras.models import Model
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

base = pd.read_csv('games.csv')
base = base.drop('Other_Sales', axis = 1)
base = base.drop('Global_Sales', axis = 1)
base = base.drop('Developer', axis = 1)

base = base.dropna(axis = 0)
base['global_sales'] = base['NA_Sales'] + base['EU_Sales'] + base['JP_Sales']
base = base.loc[base['global_sales'] > 1]

base = base.drop('NA_Sales', axis = 1)
base = base.drop('EU_Sales', axis = 1)
base = base.drop('JP_Sales', axis = 1)

base['Name'].value_counts()
nome_jogos = base.Name
base = base.drop('Name', axis = 1)


previsores = base.iloc[:, [0,1,2,3,4,5,6,7,8]].values
venda = base.iloc[:, 9].values

labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])
previsores[:, 2] = labelencoder.fit_transform(previsores[:, 2])
previsores[:, 3] = labelencoder.fit_transform(previsores[:, 3])
previsores[:, 8] = labelencoder.fit_transform(previsores[:, 8])

# s 1 0
# r 0 1
onehotencoder = OneHotEncoder(categorical_features = [0,2,3,8])
previsores = onehotencoder.fit_transform(previsores).toarray()

camada_entrada = Input(shape=(94,))
camada_oculta1 = Dense(units = 32, activation = 'sigmoid')(camada_entrada)
camada_oculta2 = Dense(units = 32, activation = 'sigmoid')(camada_oculta1)
camada_saida = Dense(units = 1, activation = 'linear')(camada_oculta2)

regressor = Model(inputs = camada_entrada,
                  outputs = [camada_saida])
regressor.compile(optimizer = 'adam',
                  loss = 'mse')
regressor.fit(previsores, [venda],
              epochs = 5000, batch_size = 100)
previsao_na, previsao_eu, previsao_jp = regressor.predict(previsores)