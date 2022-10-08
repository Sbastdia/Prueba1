import numpy as np
import sys


'''lista = np.random.randint(10, size=(6,6))
print(lista)
print(sys.getsizeof(lista))
print(lista[0][0])
print(sys.getsizeof(lista[0][0]))
print(sys.getsizeof(lista[2][3]))
num=8
print(sys.getsizeof(num))
media = sum(lista) / len(lista)

varianza = 0
for i in range(len(lista)):
    varianza +=  pow((lista[i] - media), 2)

varianza /= len(lista)

print(varianza)

# Me falta el 3.1.4

lista2 = []

for i in range(len(lista)):
    lista2.append(round(lista[i]))

print(lista2)'''
class Ejercicio31:
    def __init__(self):
        self.lista= np.random.randint(10, size=(6,6))
    def espacioBytes(self):
        #El primer getsize lo que obtiene es el valor en bytes de la matriz creada por numpy sin tomar en cuenta aquello que hay dentro.
        BytesA=sys.getsizeof(self.lista)
        #Ahora para obtener el resto de bytes que pesa debemos ir mirando en cada posición de la matriz y ver cuanto pesa, el resultado será la suma de ambos,
        #del contenido y del contenedor
        count=0
        for i in range(0,3):
            for j in range(0,3):
                count+=sys.getsizeof(self.lista[i][j])
        Bytes=BytesA+count
        return Bytes
        #Para entender mejor lo que sucede haremos una analogía con una mochila. BytesA equivale a lo que pesa la mochila ya de por sí sin meterla nada dentro
        #mientras que count es el peso de los libros, ordenadores y demás cosas que queramos meter dentro de la mochila y Bytes será el resultado de meter ese peso
        #dentro de la mochila.
        #A parte, si en vez de usar numpy usasemos un array por defecto este peso varía y no será el mismo porque numpy mete algo más que ocupa bytes.
    def MediayDesv(self):
        media=np.mean(self.lista)
        desv=np.std(self.lista)
        return media,desv

    @staticmethod
    def ejecutar():
        ejercicio31=Ejercicio31()#3.1.1
        Bytes=ejercicio31.espacioBytes()
        print("La matriz ocupa "+str(Bytes)+"bytes")#3.1.2
        media,desviacion=ejercicio31.MediayDesv()
        print("Tiene una media de "+str(media)+" y una desviación típica de "+str(desviacion))#3.1.3
        MatrizNueva=np.random.normal(loc=media, scale=desviacion, size=(6,6))#3.1.4
        print("Matriz nueva con misma media y desviación")
        print(MatrizNueva)
        MatrizNuevaRed=np.round(MatrizNueva)#3.1.5
        print("Matriz redondeada")
        print(MatrizNuevaRed)

if __name__=="__main__":
    Ejercicio31.ejecutar()