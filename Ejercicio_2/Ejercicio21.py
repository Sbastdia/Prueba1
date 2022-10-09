class Ejercicio21:
    def __init__(self):
        self.lista=[18, 50, 210, 80, 145, 333, 70, 30]
    @staticmethod
    def ejecutar():
        ejercicio21=Ejercicio21()
        for i in range(len(ejercicio21.lista)):
            if ejercicio21.lista[i] < 200 and ejercicio21.lista[i] % 10 == 0:
                print(ejercicio21.lista[i])
            elif ejercicio21.lista[i] > 300:
                break

if __name__=="__main__":
    Ejercicio21.ejecutar()