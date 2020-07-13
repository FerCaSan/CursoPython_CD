# Red Neuronal Artificial

# Instalando Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Instalando Tensorflow
# pip install tensorflow==1.0.0

# Instalando Keras
# pip install keras

# Parte 1 - Pre procesamiento de datos

# Importando las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando los datasets
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Codificando datos categoricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Separando sets de datos en Entrenamiento y Prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Escalado de Caracteristicas
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Parte 2 - Creando Red neuronal

# Importando librerias de Keras
import keras
from keras.models import Sequential
from keras.layers import Dense

# Iniciando Red Neuronal (Sequential significa que la red neuronal sera creada en secuencias, capa por capa, manualmente)
classifier = Sequential()

# Agregaando capa Input y primera capa oculta
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Agregando segunda capa oculta
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Agregando la capa output
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compilando la Red Neuronal
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Encajando Red Neuronal con set de Entrenamiento
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Parte 3 - Haciendo Predicciones y Evaluando el Modelo

# Prediccion
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Creando matriz de confusion
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)