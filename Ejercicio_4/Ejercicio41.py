from matplotlib import pyplot as plt
import numpy as np


'''x = list(range(1, 10))
y = np.ones(9)

plt.plot(x, y, 'o', color='red')
plt.show()'''
class Ejercicio41:
    def __init__(self,menor,mayor):
        self.dist=(mayor-menor)/100
    @staticmethod
    def ejecutar():
        ejercicio41=Ejercicio41(0,10)
        x = list(np.arange(ejercicio41.dist, 10,ejercicio41.dist))
        y = list()
        for i in x:
            y.append(i**3)

        plt.plot(x, y, 'o', color='red')
        plt.show()

if __name__=="__main__":
    Ejercicio41.ejecutar()