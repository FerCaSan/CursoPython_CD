

import numpy as np
import pandas as pd

personaje = {"Nombre": ['David Martinez','Fernanda Castro'],
            "Edad": ['26',31]}

df = pd.DataFrame(personaje)

df['Apellido'] = df.Nombre.str.split(" ",1).str[1]
print(df)