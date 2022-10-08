'''list1=["PEP 8", "PEP 248", "PEP 257"]

def numero_caracteres(list):
    contador=0
    for i in list:
        contador+=len(i)
    return contador

print(numero_caracteres(list1))'''
class Ejercicio22:
    def __init__(self,lista):
        self.lista=lista
    def numero_caracteres(self):
        contador=0
        for i in self.lista:
            contador+=len(i)
        return contador
    @staticmethod
    def ejecutar():
        list1=["PEP 8", "PEP 248", "PEP 257"]
        ejercicio22=Ejercicio22(list1)
        numero=ejercicio22.numero_caracteres()
        print(numero)

if __name__=="__main__":
    Ejercicio22.ejecutar()