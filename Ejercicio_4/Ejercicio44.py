import pandas as pd


df1=pd.read_csv('weatherHistory.csv')
df1=df1.dropna()
df1.reset_index(drop=True, inplace=True)
df2=pd.read_csv('Dataset_FUERTEVENTURA.csv')
df2=df2.dropna()
df2.reset_index(drop=True, inplace=True)
print('Holi encontre estos dataset de temas metereologicos con cositas en comun que alguien siga que me da mucha pereza')


class Ejercicio44:
    def __init__(self,data1,data2):
        self.df1=data1
        self.df2=data2
    def juntar(self):
        self.dataframe=pd.concat(self.df1,self.df2)
    
