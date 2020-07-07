import numpy as np

listIni = np.arange(0,20)
print(listIni)

Matriz0 = np.reshape(listIni,(5,4),order='C')
print(Matriz0)
Matriz0 = np.reshape(listIni,(5,4),order='F')
print(Matriz0)

r1 = ["Hola","Test","Jum"]
r2 = [1,2,3]
r3 = ["Si", "No", "Si"]

print(np.array([r1,r2,r3]))