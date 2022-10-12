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
print(data['Model Year'])

def eliminar_defectos(dtf):
    lst=dtf.columns
    for i in lst:
        for j in range(len(dtf[i])):
            if dtf[i][j]=='?':
                dtf[i][:]
    return dtf

def filtro_antiguedad(dtf,año):
    for c in range(len(dtf['Model Year'])):
        if dtf['Model Year'][c]!=año:
            dtf=dtf.drop(c)
    return dtf

def dividir(dtf,lst=[]):
    dtf1=pd.DataFrame()
    for i in dtf['Model Year']:
        if i not in lst:
            lst.append(i)
    for i in range(len(lst)):
        print(filtro_antiguedad(dtf,lst[i]))
        for j in range(len(dtf.columns)):
            dtf1[f'{i}']=filtro_antiguedad(dtf,lst[i])[dtf.columns[j]].mean()
    print(dtf1)

dividir(data)
