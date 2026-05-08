import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV

base = pd.read_csv('iris.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

labelencoder = LabelEncoder()
classe = labelencoder.fit_transform(classe)
classe_dummy = np_utils.to_categorical(classe)

def criar_rede(optimizer, kernel_initializer, activation, neurons):
    classificador = Sequential()
    classificador.add(Dense(units = neurons,
                            kernel_initializer = kernel_initializer, 
                            activation = activation, input_dim = 4))
    
    classificador.add(Dense(units = neurons, activation = activation))
    
    classificador.add(Dense(units = 3, activation = 'softmax'))
    
    classificador.compile(optimizer = optimizer, loss = 'sparse_categorical_crossentropy',
                          metrics = ['accuracy'])
    return classificador

classificador = KerasClassifier(build_fn = criar_rede)
parametros = {'batch_size': [8, 10],
              'epochs': [150, 100],
              'optimizer': ['sgd', 'adamax'],
              'kernel_initializer': ['random_uniform', 'normal'],
              'activation': ['tanh', 'sigmoid'],
              'neurons': [16, 8]}

grid_search = GridSearchCV(estimator = classificador,
                           param_grid = parametros,
                           cv = 5)
grid_search = grid_search.fit(previsores, classe)
melhores_parametros = grid_search.best_params_
melhor_precisao = grid_search.best_score_