import pandas as pd


df1=pd.read_csv('weatherHistory.csv')
df1=df1.dropna()
df1.reset_index(drop=True, inplace=True)
df2=pd.read_csv('Dataset_FUERTEVENTURA.csv')
df2=df2.dropna()
df2.reset_index(drop=True, inplace=True)
print('Holi encontre estos dataset de temas metereologicos con cositas en comun que alguien siga que me da mucha pereza')
