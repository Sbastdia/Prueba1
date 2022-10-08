import numpy as np
import pandas as pd


df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))

print(df.head())

new_df=df['Displacement']
list=[]
for i in range(len(new_df)):
    if new_df.iloc[i]<=300 and new_df.iloc[i]==float:
        list.append(i)
df=df.drop(list)
print(list)
