import numpy as np
import pandas as pd


df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))

t = df.loc[:, 'Weight']
t=t.astype(float)
#print(t.head())
#print(df.head())



"""for i in range(len(df)):
    df[i] 

for df[]"""




for  c in range(len(t)):
    if t.iloc[c]<3000.0 :
        t=t.drop(c)
print(type(t))



