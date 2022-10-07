import numpy as np
import pandas as pd

columnas = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']
df = pd.read_csv('Ejercicio_4/auto-mpg.csv', sep='\s+')

print(df)
