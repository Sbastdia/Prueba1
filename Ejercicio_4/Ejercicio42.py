import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''data_array = np.array([1.0,2,3,4])
#4.2.1
def convertir(array):
    array=array.astype(int)
    data_df = pd.Series(array)
    return data_df
print(convertir(data_array))

new_serie = pd.Series(map(lambda x: int(x), pd.Series(data_array)))
print(new_serie)
print("4.2.2")
#4.2.2
data_array2=np.array([10, True, 8.00, False, 8, 10])
new=convertir(data_array2)
new2 = pd.Series(map(lambda x: int(x), pd.Series(data_array2)))

#4.2.3 y 4.2.9
print("4.2.3")
print(new2)
print(new)

for i in new:
    print(type(i))

#Hay que terminar el 4.2.3
new3=pd.DataFrame(new,columns=['ej_42'])
print("memoria")
print(new3.memory_usage())
print("##########33333")
print(new3)

#4.2.4
plt.plot(new)
plt.show()
print("4.2.5")
#4.2.5
print(new.describe())
print("4.2.6")
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
print("4.2.7")
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
print("4.2.8")
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
print(ordenar(new))'''
####################################
def consulta(serie):
        valores=serie.values
        indice=serie.index
        tipos=serie.dtype
        bits=serie.nbytes
        print("Valores de la serie: ")
        print(valores)
        print("Indices de la serie: ")
        print(indice)
        print("Tipos de datos de la serie: ")
        print(tipos)
        print("Número de bits de la serie: ")
        print(bits)
        return valores,indice,tipos,bits
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
class Ejercicio42:
    def __init__(self,lista):
        self.lista=lista
    def funcion(self):
        nueva_serie = pd.Series(map(lambda x: int(x), pd.Series(self.lista)))
        return nueva_serie

    @staticmethod
    def ejecutar():
        data_array = np.array([1.0,2,3,4])
        print("Apartado 4.2.1")
        ejercicio42=Ejercicio42(data_array)#4.2.1
        serie=ejercicio42.funcion()
        print(serie)
        
        print("Apartado 4.2.2")
        data_array2=np.array([10, True, 8.00, False, 8, 10])#4.2.2
        ejercicio42_2=Ejercicio42(data_array2)
        serie2=ejercicio42_2.funcion()
        print(serie2)

        print("Apartado 4.2.3")
        consulta(serie2)#4.2.3

        print("Apartado 4.2.4")
        plt.plot(serie2)#4.2.4
        plt.show()

        print("Apartado 4.2.5")
        print(serie2.describe())#4.2.5

        print("Apartado 4.2.6")
        print(serie2.value_counts())#4.2.6
        #si quieres la frecuencia relativa debes poner value_counts(normalize=True)

        print("Apartado 4.2.7")
        print(serie2.value_counts().index)#4.2.7
        #los indices están en el corchete

        print("Apartado 4.2.8")
        serieOrd=ordenar(serie2)#4.2.8
        print(serieOrd)

        print("Apartado 4.2.9")
        serieNueva=pd.DataFrame(serie2,columns=['ej_42'])#4.2.9
        print(serieNueva)

if __name__=="__main__":
    Ejercicio42.ejecutar()