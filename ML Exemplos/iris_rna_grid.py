from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Carrega os dados
X, y = load_iris(return_X_y=True)

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define a rede neural
rede = MLPClassifier(max_iter=2000, random_state=42)

# Define os parâmetros que serão testados
parametros = {
    'hidden_layer_sizes': [
        (),       # Zero camadas ocultas
        (10,),    # Uma camada com 10 neurônios
        (20,),    # Uma camada com 20 neurônios
        (10, 10), # Duas camadas com 10 neurônios cada
        (20, 10)  # Duas camadas com 20 e 10 neurônios
    ],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'sgd']
}

# Busca a melhor combinação
busca = GridSearchCV(
    estimator=rede,
    param_grid=parametros,
    cv=5,
    scoring='accuracy'
)

busca.fit(X_treino, y_treino)

# Exibe os melhores resultados
print("Melhores parâmetros:", busca.best_params_)
print("Melhor acurácia na validação:", busca.best_score_)

# Avalia no conjunto de teste
print("Acurácia no teste:", busca.score(X_teste, y_teste))