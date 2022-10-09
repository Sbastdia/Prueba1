import numpy as np
import pandas as pd

df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))
print(df)
#print(t.head())
#print(df.head())
def filtro_peso_minimo(dtf,peso):
    for c in range(len(dtf['Weight'])):
        if dtf['Weight'][c]<=peso:
            dtf=dtf.drop(c)
    return dtf
print(filtro_peso_minimo(df,5000))

def filtro_antiguedad(dtf,año):
    for c in range(len(dtf['Model Year'])):
        if dtf['Model Year'][c]!=año:
            dtf=dtf.drop(c)
    return dtf

new_df=filtro_antiguedad(df,76)
new_df.reset_index(drop=True, inplace=True)
print(new_df['Cylinders'][0])

def frecuencia_valor(serie,valor):
    contador=0
    valores=[]
    for i in range(len(serie)):
        if serie[i] not in valores:
            valores.append(serie[i])
    if valor in valores:
        for i in range(len(serie)):
            if valor==serie[i]:
                contador+=1
            else:pass
        return contador
    else:
        return f'{valor} no es un valor de la serie'

def frecuencia_serie(serie):
    dict={}
    for i in range(len(serie)):
        dict[serie[i]]=frecuencia_valor(serie,serie[i])
    return dict

frecuencia_cilindros=frecuencia_serie(new_df['Cylinders'])
print(frecuencia_cilindros)
#como podemos observar, el numero de cilindros mas frecuente es 4

año_70=filtro_antiguedad(df,70)
año_79=filtro_antiguedad(df,79)
consumo_medio_año_70=año_70['MPG'].mean()
consumo_medio_año_79=año_79['MPG'].mean()
diferencia_consumo=abs(consumo_medio_año_70-consumo_medio_año_79)
print (diferencia_consumo)