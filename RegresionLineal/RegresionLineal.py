# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 00:46:04 2020

@author: ingfe
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#importando datos
df = pd.read_csv('salario.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

#Separando en set de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#Adaptación de una regresión lineal simple al conjunto de entrenamiento
lr = LinearRegression()
lr.fit(X_train,y_train)

#Aplicando predicción en set de prueba
y_pred = lr.predict(X_test)

#Visualización de resultados entrenamiento
plt.scatter(X_train,y_train,c='red')
plt.plot(X_train,lr.predict(X_train),c='blue')
plt.title('Salario Vs. Años experiencia (Set de entrenamiento)')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')

#Visualización de resultados prueba
plt.scatter(X_test,y_test,c='green')
plt.plot(X_train,lr.predict(X_train),c='cyan')
plt.title('Salario Vs. Años experiencia (Set de pruebas)')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')