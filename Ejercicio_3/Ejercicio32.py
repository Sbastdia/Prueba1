import numpy as np
class Ejercicio32:
    def __init__(self):
        self.matriz=np.arange(0,100,9).reshape(3,4)
    def filtrar(self):
        for i in range(0,len(self.matriz)):
            for j in range(len(self.matriz)+1):
                if self.matriz[i][j]%5==0 and self.matriz[i][j]>=0:
                    pass
                else:
                    self.matriz[i][j]=-1
    @staticmethod
    def ejecutar():
        ejercicio32=Ejercicio32()
        ejercicio32.filtrar()
        print(ejercicio32.matriz)

if __name__=="__main__":
    Ejercicio32.ejecutar()