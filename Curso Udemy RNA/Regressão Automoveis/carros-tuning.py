import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import GridSearchCV

base = pd.read_csv('autos.csv', encoding = 'ISO-8859-1')
base = base.drop('dateCrawled', axis = 1)
base = base.drop('dateCreated', axis = 1)
base = base.drop('nrOfPictures', axis = 1)
base = base.drop('postalCode', axis = 1)
base = base.drop('lastSeen', axis = 1)
base = base.drop('name', axis = 1)
base = base.drop('seller', axis = 1)
base = base.drop('offerType', axis = 1)

base = base[base.price > 10]
base = base[base.price < 350000]

values = {'vehicleType': 'limousine', 'gearbox': 'manuell', 'model': 'golf', 'fuelType': 'benzin', 'notRepairedDamage': 'nein'}
base = base.fillna(value=values)

previsores = base.iloc[:, 1:13].values
preco_real = base.iloc[:, 0].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_previsores = LabelEncoder()
previsores[:, 0] = labelencoder_previsores.fit_transform(previsores[:, 0])
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 10] = labelencoder_previsores.fit_transform(previsores[:, 10])

onehotencoder = OneHotEncoder(categorical_features = [0,1,3,5,8,9,10])
previsores = onehotencoder.fit_transform(previsores).toarray()

def criar_rede(loss):
    regressor = Sequential()
    regressor.add(Dense(units = 158, activation = 'relu', kernel_initializer = 'random_uniform', input_dim = 316))
    regressor.add(Dense(units = 158, activation = 'relu', kernel_initializer = 'random_uniform'))
    regressor.add(Dense(units = 1, activation = 'linear'))
    regressor.compile(loss=loss, optimizer='adam', metrics=['mean_absolute_error'])
    return regressor

# Não é necessário alterar o parâmetro metrics pois ele é usado somente para 
# mostrar o resultado e de fato ele não é utilizado no treinamento da rede neural

regressor = KerasRegressor(build_fn = criar_rede, epochs = 100, batch_size = 300)
parametros = {'loss': ['mean_squared_error', 'mean_absolute_error',
                       'mean_absolute_percentage_error', 'mean_squared_logarithmic_error',
                       'squared_hinge']}
grid_search = GridSearchCV(estimator = regressor,
                           param_grid = parametros,                           
                           cv = 10)
grid_search = grid_search.fit(previsores, preco_real)
melhores_parametros = grid_search.best_params_