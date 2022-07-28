   # -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from sklearn import metrics
import matplotlib.pyplot as plt

#No caso do projeto, o que recorta é a probabilidade do meio!
y_pred_proba = [0.9 , 0.8, 0.75, 0.65, 0.9 , 0.8, 0.75, 0.65, 0.75, 0.65]
y_test = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]

fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)

#create ROC curve
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc=4)
plt.show()