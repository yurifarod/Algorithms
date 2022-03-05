#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:20:30 2022

@author: yurifarod
"""

import keras
from keras.wrappers.scikit_learn import KerasClassifier
import mlxtend
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow import keras

dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(dataset.data,
                                                    dataset.target,
                                                    test_size=0.2)

EPOCHS_IRIS = 100
BATCH_SIZE_IRIS = 16
TRAIN_TEST_SPLIT = 0.8

def create_model(train_input):
    # 1 ReLU layer + 1 Dropout layer + 1 softmax layer for 3 classes
    model = keras.Sequential([
        keras.layers.Dense(16,
                           activation='relu',
                           input_shape=((train_input.shape[1]),)),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(3,
                           activation='softmax')
    ])
    
    model.compile(optimizer=keras.optimizers.Adam(lr=1e-3),
                  loss=keras.losses.SparseCategoricalCrossentropy())

    return model

keras.backend.clear_session()

# Wrap Keras nn and generating SFS object
class MakeModel(object):

    def __init__(self, X=None, y=None):
        pass

    def predict(self, X):
        y_pred = self.model.predict(X)
        y_pred = (y_pred > 0.5)
        return y_pred
    
    def fit(self, X, y):
        skwrapped_model = KerasClassifier(build_fn=create_model,
                                          train_input=X,
                                          epochs=EPOCHS_IRIS,
                                          batch_size=BATCH_SIZE_IRIS,
                                          validation_split=1-TRAIN_TEST_SPLIT,
                                          verbose=0)
        self.model = skwrapped_model
        self.model.fit(X, y)
        return self.model

sffs = SFS(MakeModel(),
           k_features=(1, X_train.shape[1]),
           floating=True,
           clone_estimator=False,
           cv=0,
           n_jobs=1,
           scoring='accuracy')

# Apply SFS to identify best feature subset
sffs = sffs.fit(X_train, y_train)
result_sub = sffs.subsets_
result_id = sffs.k_feature_idx_
