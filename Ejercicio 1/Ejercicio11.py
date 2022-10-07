#Definimos una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python
lista=[1, "abc", 3.4, -5, 6]
lista2=[]
for i in range(len(lista)-1,0,-2):
    lista2.append(lista[i-1])

lista[0] =lista[-1]
lista[-1]=lista[0]
lista.pop()
nuevaLista= []
for i in lista:
    nuevaLista.append(i)
    nuevaLista.append(i)

print(nuevaLista)



