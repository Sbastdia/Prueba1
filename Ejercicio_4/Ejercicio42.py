import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_array = np.array([1.0,2,3,4])
#4.2.1
def convertir(array):
    array=array.astype(int)
    data_df = pd.Series(array)
    return data_df
print(convertir(data_array))

new_serie = pd.Series(map(lambda x: int(x), pd.Series(data_array)))
print(new_serie)

#4.2.2
data_array2=np.array([10, True, 8.00, False, 8, 10])
new=convertir(data_array2)
new2 = pd.Series(map(lambda x: int(x), pd.Series(data_array2)))

#4.2.3 y 4.2.9
print(new2)
print(new)

for i in new:
    print(type(i))

new2=pd.DataFrame(new,columns=['ej_42'])
print(new2.memory_usage())

#4.2.4
plt.plot(new)
plt.show()

#4.2.5
print(new.describe())

#4.2.6
def frecuencia_valor(serie,valor):
    contador=0
    valores=[]
    for i in range(len(serie)):
        if serie[i] not in valores:
            valores.append(serie[i])
    if valor in valores:
        for i in range(len(serie)):
            if valor==serie[i]:
                contador+=1
            else:pass
        return contador
    else:
        return f'{valor} no es un valor de la serie'

def frecuencia_serie(serie):
    dict={}
    for i in range(len(serie)):
        dict[serie[i]]=frecuencia_valor(serie,serie[i])
    return dict

print(frecuencia_serie(new))

#4.2.7
def valores_unicos(serie,valores=[],repetidos=[],unicos=[]):
    for i in range(len(serie)):
        if serie[i] not in valores:
            valores.append(serie[i])
        else:
            repetidos.append(serie[i])
    for i in valores:
        if i not in repetidos:
            unicos.append(i)
    return unicos
print(valores_unicos(new))

#4.2.8
def ordenar(serie):
    n = len(serie)
    for i in range(n):
        derecha = serie[i]
        for j in range(i - 1, -1, -1):
            izquierda = serie[j]
            if derecha > izquierda:
                serie[j + 1] = izquierda
                serie[j] = derecha
                derecha = serie[j]
    return serie

print(ordenar(new))





