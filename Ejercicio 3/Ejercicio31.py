import numpy as np
import sys


lista = np.random.rand(6)*10
print(sys.getsizeof(lista))

media = sum(lista) / len(lista)

varianza = 0
for i in range(len(lista)):
    varianza +=  pow((lista[i] - media), 2)

varianza /= len(lista)

print(varianza)
