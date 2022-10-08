import numpy as np
import pandas as pd



df = pd.read_csv('Ejercicio_4/auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))

t = df.loc[:, 'Weight']

#print(t.head())
#print(df.head())



for i in range(len(df)):
    df[i] 

for df[]




for  c in range(len(t)):
    if t[c]<5000.0 and t[c]==float:
        t=t.drop(c)

print(t)
