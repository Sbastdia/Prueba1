class Ejercicio11:
    def __init__(self,lista):
        self.lista=lista

    def selecAlternado(self):
        lista2=[]
        for i in range(len(self.lista)-1,0,-2):
            lista2.append(self.lista[i-1])
        return lista2

    def ultAprim(self):
        prim=self.lista[0]
        self.lista[0]=self.lista[-1]
        self.lista[-1]=prim
        print(self.lista)

    def repList(self):
        nuevaLista= []
        for i in self.lista:
            nuevaLista.append(i)
            nuevaLista.append(i)
        return nuevaLista
    @staticmethod
    def ejecutar():
        #Definimos una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python
        lista=[1, "abc", 3.4, -5, 6]#1.1.1
        ejercicio11=Ejercicio11(lista)
        print("Ejercicio 1.1.2")
        Alt=ejercicio11.selecAlternado()#1.1.2
        print(Alt)
        print("Ejercicio 1.1.3")
        ejercicio11.ultAprim()#1.1.3
        print("Ejercicio 1.1.4")
        ejercicio11.lista.pop()#1.1.4
        print(ejercicio11.lista)
        print("Ejercicio 1.1.5")
        NuevaLista=ejercicio11.repList()#1.1.5
        print(NuevaLista)

if __name__=="__main__":
    Ejercicio11.ejecutar()