import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

stats = pd.read_csv('P4-Demographic-Data.csv')

stats.columns = ['CountryName','ContryCod','BirthRate','InternetUsers','IncomeGroup']

#Distribución
#sns.distplot(stats['InternetUsers'],bins = 10)


#Lineal
#sns.lmplot(x = 'InternetUsers', y = 'BirthRate', data = stats)

#Lineal sin Linea de regresión y graficando IncomGroup, definiendo tamaño puntos
sns.lmplot(x = 'InternetUsers', y = 'BirthRate', data = stats, fit_reg = False, hue = 'IncomeGroup', scatter ={'s':80})
plt.show()