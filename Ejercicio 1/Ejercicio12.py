def edadDiccionario(diccionario,nombre):
    pos=0
    for i in diccionario['Alumnos']:
        if i==nombre:
            edad=diccionario['Edad'][pos];
        pos+=1
    return edad

def claveDiccionario(diccionario,clave):
    for j in diccionario.keys():
        if j==clave:
            return True
    return False
def tipoDiccionario(diccionario,valor):
    lista=diccionario.get(valor)
    tipo=type(lista)
    longitud=len(lista)
    texto="El valor es de tipo: " +str(tipo)+" y de longitud: "+ str(longitud)
    return texto

def setDiccionario(diccionario):
    lista=diccionario["Edad"]
    s=set(lista)
    return s
if __name__=="__main__":
    dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}
edad=edadDiccionario(dic_ejemplo,"Daniela")
print(edad)
esta=claveDiccionario(dic_ejemplo,'Centro')
print(esta)
tipo=tipoDiccionario(dic_ejemplo,"Curso")
print(tipo)
se=setDiccionario(dic_ejemplo)
print(se)