import pandas as pd


stats = pd.read_csv('P4-Demographic-Data.csv')

stats.columns = ['CountryName','ContryCod','BirthRate','InternetUsers','IncomeGroup']

calculo = stats.BirthRate * stats.InternetUsers

stats['calculo'] = stats.BirthRate * stats.InternetUsers

#print(calculo)
#print(stats['calculo'].head(5))

########
#FILTROS
########

#Op 1
filtro = stats.InternetUsers < 2
filtro2 = stats.BirthRate > 40
filtro3 = stats.IncomeGroup == 'Low income'

#print(stats[filtro & filtro2 & filtro3])

#Op 2.
#print(stats[(stats['InternetUsers'] < 2) & (stats['BirthRate'] < 40 )])

#######
#.iat()
#######
print(stats.head(5))
print(stats.iat[2,3])

#######
#.at() - Especifíco nombre de columna
#######
print(stats.at[2,'InternetUsers'])

#######
#.iloc()
print(stats.iloc[2,3])

#######
#.loc() - Especifíco nombre de columna
#######
print(stats.loc[2,'InternetUsers'])



