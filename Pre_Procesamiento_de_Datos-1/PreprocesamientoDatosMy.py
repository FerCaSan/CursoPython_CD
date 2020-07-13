# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:54:52 2020

@author: ingfe
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

#importando datos
df = pd.read_csv('Data.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1]

#Imputar valores
imputer = SimpleImputer(missing_values =np.nan,strategy ='mean')

imputerf = imputer.fit(X[:,1:3])

X[:,1:3] = imputerf.transform(X[:,1:3])

#Dummies Label Encoder - Pasa a números las categorías (0,1,2)
le = preprocessing.LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])

#Para cada valor numérico generado en el paso anterior, generará una columna con valores de 1 y 0
ct = ColumnTransformer([('one_hot_encoder', preprocessing.OneHotEncoder(categories='auto'),[0])],
                        remainder='passthrough')

X = ct.fit_transform(X)

y = le.fit_transform(y)

#Separando en set de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Escalando variables - Dada diferencia de pesos, el modelo no se debe sesgar, por lo que se escalan variables
sc = preprocessing.StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
