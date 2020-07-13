# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 00:46:04 2020

@author: ingfe
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#importando datos
df = pd.read_csv('Data.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1]

#Separando en set de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Escalando variables - Dada diferencia de pesos, el modelo no se debe sesgar, por lo que se escalan variables
#sc = preprocessing.StandardScaler()
#X_train = sc.fit_transform(X_train)
#X_test = sc.fit_transform(X_test)