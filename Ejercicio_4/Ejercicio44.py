from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#df1=pd.read_csv('weatherHistory.csv')
#df1=df1.dropna()
#df1.reset_index(drop=True, inplace=True)
#df2=pd.read_csv('Dataset_FUERTEVENTURA.csv')
#df2=df2.dropna()
#df2.reset_index(drop=True, inplace=True)
#print('Holi encontre estos dataset de temas metereologicos con cositas en comun que alguien siga que me da mucha pereza')

class Ejercicio44:

    def __init__(self):
        self.data1= pd.read_csv('weather.csv')
        self.data2= pd.read_csv('weather2.csv')

    #ejercicio 4.4.1
    def concatenar(self):
        self.data3= pd.concat ([self.data1, self.data2], axis=1)
        return self.data3

    #ejercicio 4.4.2
    def concatenarComun(self):
        self.data4=pd.merge(self.data1, self.data2, how='inner', suffixes=('_x', '_y'))
        return self.data4

    #ejercicio 4.4.3
    def concatenar2(self):
        self.df1= pd.read_csv('aportaciones.csv')
        self.df2= pd.read_csv('aportaciones2.csv')
        self.dfJuntas= pd.concat ([self.df1, self.df2], axis=1)
        self.filas= len(self.dfJuntas.axes[0])
        print('El número de filas de las dos tablas concatenadas es: ' +self.filas)

    #ejercicio 4.4.4
    def union(self):
        self.unidas=pd.merge(self.df1, self.df2, how='left')
        self.filas2= len(self.unidas.axes[0])
        print('El número de filas de las dos tablas concatenadas es: ' +self.filas2)

    #ejercicio 4.4.5
    def unionComun(self):
        self.unidas2=pd.merge(self.df1, self.df2, how='inner', suffixes=('_x', '_y'))
        self.filas3= len(self.unidas2.axes[0])
        print('El número de filas de las dos tablas concatenadas es: ' +self.filas3)

    #ejercicio 4.4.6
    def medias(self):
        self.df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))
        self.by_year= self.df.groupby('Model year')
        return self.by_year.mean()

    #ejercicio 4.4.7
    def evolucion(self):
        self.x_values=self.df['Model year'].value_counts().to_list()
        self.y_values= self.by_year.mean()
        plt.figure()
        plt.bar(self.x_values, self.y_values)
        plt.title('Evolución de las variables por año')
        plt.show()

    #ejercicio 4.4.8
    def pesoMedioCoches(self):
        self.x_values=self.df['Model year'].value_counts().to_list()
        self.y_values= self.df.groupby('Model year').mean()['Weight']
        plt.figure()
        plt.bar(self.x_values, self.y_values)
        plt.title('Peso medio de los coches a lo largo de los años')
        plt.show()

    @staticmethod
    def ejecutar():
        print('Ejercicio 4.4.1')
        Ejercicio44.concatenar()
        print('Ejercicio 4.4.2')
        Ejercicio44.concatenarComun()
        print('Ejercicio 4.4.3')
        Ejercicio44.concatenar2()
        print('Ejercicio 4.4.4')
        Ejercicio44.union()
        print('Ejercicio 4.4.5')
        Ejercicio44.unionComun()
        print('Ejercicio 4.4.6')
        Ejercicio44.medias()
        print('Ejercicio 4.4.7')
        Ejercicio44.evolucion()
        print('Ejercicio 4.4.8')
        Ejercicio44.pesoMedioCoches()

if __name__=='__main__':
    Ejercicio44.ejecutar()