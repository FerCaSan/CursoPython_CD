import numpy as np
from numpy.random import randn

answer = None
x = randn() 

# if x > 1:
#     answer = "Es mayor que 1"
# else:
#     answer = "Es menor que 1"
# print(answer) 

# if x > 1:
#     answer = "Es mayor que 1"
# else:
#     if x >= -1:
#         answer = "Entre -1 y 1"
#     else:
#         answer = "Menor que 1"
# print(x)
# print(answer)

if x > 1:
    answer = "Es mayor que 1"
elif x >= -1:
    answer = "Entre -1 y 1"
else:
    answer = "Menor que 1"

print(x)
print(answer)






