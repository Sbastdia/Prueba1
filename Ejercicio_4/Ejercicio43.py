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
print(new_df)

