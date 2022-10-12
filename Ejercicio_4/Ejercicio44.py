import pandas as pd
import numpy as np


df1=pd.read_csv('weatherHistory.csv')
df1=df1.dropna()
df1.reset_index(drop=True, inplace=True)

df2=pd.read_csv('Dataset_FUERTEVENTURA.csv')
df2=df2.dropna()
df2.reset_index(drop=True, inplace=True)

#4.4.1
df3=pd.concat([df1,df2])
df3.reset_index(drop=True, inplace=True)
print(df3.columns)

#4.4.2
df1=df1.rename(columns={'Wind Speed (km/h)':'ws','Wind Bearing (degrees)':'wd','Pressure (millibars)':'atmos_pres','Temperature (C)':'temp','Formatted Date':'time'})
df4=pd.concat([df1,df2])
def nuevo_dtf(dtf):
    lst=dtf.columns
    dtf1=pd.DataFrame()
    for i in range(len(lst)):
        if lst[i]=='ws' or lst[i]=='wd' or lst[i]=='temp' or lst[i]=='time' or lst[i]=='atmos_pres':
                dtf1[lst[i]]=dtf.iloc[:,i]
    dtf1.reset_index(drop=True, inplace=True)
    return dtf1
df5=nuevo_dtf(df4)
print(df5)

#4.4.3
print(len(df3.index))

#4.4.4
result1 = pd.merge(df1, df2, how="outer", on=["ws", "wd","temp","atmos_pres","time"])
print(len(result1.index))

#4.4.5
df11=nuevo_dtf(df1)
df22=nuevo_dtf(df2)
result2 = pd.merge(df11, df22, how="outer", on=["ws", "wd","temp","atmos_pres","time"])
print(len(result2.index))

#4.4.6
data=pd.read_csv('auto-mpg.csv',sep='\s+',names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))




"""class Ejercicio44:
    def __init__(self,data1,data2):
        self.df1=data1
        self.df2=data2
    def juntar(self):
        self.dataframe=pd.concat(self.df1,self.df2)"""

