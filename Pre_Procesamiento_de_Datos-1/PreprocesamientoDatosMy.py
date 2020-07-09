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

#importando datos
df = pd.read_csv('Data.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,-1]

#Imputar valores
imputer = SimpleImputer(missing_values =np.nan,strategy ='mean')

imputerf = imputer.fit(X[:,1:3])

X[:,1:3] = imputerf.transform(X[:,1:3])

#Dummies Label Encoder
le = preprocessing.LabelEncoder()
X[:,0] = le.transform(X[:,0])

ohe = preprocessing.OneHotEncoder(categories='Country')

X = ohe.fit_transform(X)
