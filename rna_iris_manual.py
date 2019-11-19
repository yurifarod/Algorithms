# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:28:42 2019

@author: yfdantas
"""

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def initialize_parameters(n_x, n_h1, n_h2,n_h3, n_y):
    W1 = np.random.randn(n_h1, n_x)
    b1 = np.zeros((n_h1, 1))
    W2 = np.random.randn(n_h2, n_h1)
    b2 = np.zeros((n_h2, 1))
    W3 = np.random.randn(n_h3, n_h2)
    b3 = np.zeros((n_h3, 1))
    W4 = np.random.randn(n_y, n_h3)
    b4 = np.zeros((n_y, 1))
    
    parameters = {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2,
        "W3": W3,
        "b3": b3,
        "W4": W4,
        "b4": b4
    }
    return parameters

def forward_prop(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    W3 = parameters["W3"]
    b3 = parameters["b3"]

    W4 = parameters["W4"]
    b4 = parameters["b4"]

    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = np.tanh(Z2)
    Z3 = np.dot(W3, A2) + b3
    A3 = np.tanh(Z3)
    Z4 = np.dot(W4, A3) + b4
    A4 = sigmoid(Z4)

    cache = {
        "A1": A1,
        "A2": A2,
        "A3": A3,
        "A4": A4
        
    }
    return A4, cache

def calculate_cost(A2, Y):

    cost = -np.sum(np.multiply(Y, np.log(A2)) +  np.multiply(1-Y, np.log(1-A2)))/m

    cost = np.squeeze(cost)

    return cost

def backward_prop(X, Y, cache, parameters):
    A1 = cache["A1"]
    A2 = cache["A2"]
    A3 = cache["A3"]
    A4 = cache["A4"]
    
    W2 = parameters["W2"]
    W3 = parameters["W3"]
    W4 = parameters["W4"]
    
    
    dZ4 = A4 - Y
    dW4 = np.dot(dZ4, A3.T)/m
    db4 = np.sum(dZ4, axis=1, keepdims=True)/m
    
    dZ3 = np.multiply(np.dot(W4.T, dZ4), 1-np.power(A3, 2))
    dW3 = np.dot(dZ3, A2.T)/m
    db3 = np.sum(dZ3, axis=1, keepdims=True)/m
    
    dZ2 = np.multiply(np.dot(W3.T, dZ3), 1-np.power(A2, 2))
    dW2 = np.dot(dZ2, A1.T)/m
    db2 = np.sum(dZ2, axis=1, keepdims=True)/m
    
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1-np.power(A1, 2))
    dW1 = np.dot(dZ1, X.T)/m
    db1 = np.sum(dZ1, axis=1, keepdims=True)/m

    grads = {
        "dW1": dW1,
        "db1": db1,
        "dW2": dW2,
        "db2": db2,
        "dW3": dW3,
        "db3": db3,
        "dW4": dW4,
        "db4": db4
    }

    return grads

def update_parameters(parameters, grads, learning_rate):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    
    W3 = parameters["W3"]
    b3 = parameters["b3"]
    
    W4 = parameters["W4"]
    b4 = parameters["b4"]
    
    dW1 = grads["dW1"]
    db1 = grads["db1"]
    
    dW2 = grads["dW2"]
    db2 = grads["db2"]
    
    dW3 = grads["dW3"]
    db3 = grads["db3"]
    
    dW4 = grads["dW4"]
    db4 = grads["db4"]

    W1 = W1 - learning_rate*dW1
    b1 = b1 - learning_rate*db1
    
    W2 = W2 - learning_rate*dW2
    b2 = b2 - learning_rate*db2
    
    W3 = W3 - learning_rate*dW3
    b3 = b3 - learning_rate*db3
    
    W4 = W4 - learning_rate*dW4
    b4 = b4 - learning_rate*db4
    
    new_parameters = {
        "W1": W1,
        "W2": W2,
        "W3": W3,
        "W4": W4,
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "b4": b4
    }

    return new_parameters


def model(X, Y, n_x, n_h1,n_h2,n_h3, n_y, num_of_iters, learning_rate):
    parameters = initialize_parameters(n_x, n_h1, n_h2,n_h3, n_y)

    for i in range(0, num_of_iters+1):
        a3, cache = forward_prop(X, parameters)

        cost = calculate_cost(a3, Y)

        grads = backward_prop(X, Y, cache, parameters)

        parameters = update_parameters(parameters, grads, learning_rate)

        if(i%100 == 0):
            print('Cost after iteration# {:d}: {:f}'.format(i, cost))

    return parameters

def predict(X, parameters,tam):
    a2, cache = forward_prop(X, parameters)
    yhat = a2
    yhat = np.squeeze(yhat)
    yhat = yhat.T
    pred = [[0 for _ in range(tam)] for _ in range(len(yhat))]
    for i in range(len(yhat)):
        for j in range(len(yhat[i])):
            if(yhat[i][j] >= 0.5):
                pred[i][j] = 1
            else:
                pred[i][j] = 0

    return pred
    


np.random.seed(2)
dados = datasets.load_iris()
# The 4 training examples by columns
#---X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
X = dados.data
# The outputs of the XOR for every example in X
#------Y = np.array([[0, 1, 1, 0]])
y = dados.target

onehotencoder = OneHotEncoder(categories='auto')
aux = []

for i in y:
    aux.append([i])
y = aux
y = onehotencoder.fit_transform(y).toarray()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# No. of training examples
m = X.T.shape[1]

# Set the hyperparameters
n_x = X.shape[1]     #No. of neurons in first layer
n_h1 = 10   #No. of neurons in hidden layer 16
n_h2 = 8  #No. of neurons in hidden layer 15
n_h3 = 7  #No. of neurons in hidden layer 12
n_y = y.shape[1]    #No. of neurons in output layer
num_of_iters = 2000
learning_rate = 0.2  #1.2
print('Numero Neuronio Layer 1: '+ str(n_h1))
print('Numero Neuronio Layer 2: '+ str(n_h2))
print('Numero Neuronio Layer 3: '+ str(n_h3))
print('Learning rate:'+ str(learning_rate)) 


trained_parameters = model(X_train.T,y_train.T, n_x, n_h1,n_h2,n_h3, n_y, num_of_iters, learning_rate)

# Test 2X1 vector to calculate the XOR of its elements. 
# Try (0, 0), (0, 1), (1, 0), (1, 1)
#X_test = np.array([[1], [1]])
#
y_predict = np.array(predict(X_test.T, trained_parameters, n_y))
#
#print('Neural Network prediction for example ({:d}, {:d}) is {:d}'.format(
#    X_test[0][0], X_test[1][0], y_predict))


valor = accuracy_score(y_test, y_predict)
print('Acuracy:'+str(valor*100)+'%')




