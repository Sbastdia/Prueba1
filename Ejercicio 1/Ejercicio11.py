#Definimos una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python
lista=[1, "abc", 3.4, -5, 6]
lista2=[]
#for i in reversed(lista):

    #lista2.append(i)

lista[0] =lista[-1]
lista[-1]=lista[0]
lista.pop()
nuevaLista= [lista]
print(lista)



