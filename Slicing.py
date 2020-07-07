import pandas as pd

stats = pd.read_csv('P4-Demographic-Data.csv')

stats.columns = ['CountryName','ContryCod','BirthRate','InternetUsers','IncomeGroup']

#print(stats.head(5))

#Imprime las filas 2 a 5
#print(stats[2:6])

#Imprime las filas invertidas de la 194 a 0
#print(stats[::-1])

#Imprime las filas de 20 en 20
#print(stats[::20])

#Imprime una columna
#print(stats[['BirthRate','IncomeGroup']].head(5))

#Imprime filas y columnas
print(stats[4:12][['BirthRate','IncomeGroup']])
