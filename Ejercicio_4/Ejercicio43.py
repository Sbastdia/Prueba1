import numpy as np
import pandas as pd

df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))
print(df)
#print(t.head())
#print(df.head())

#4.3.1
def filtro_peso_minimo(dtf,peso):
    for c in range(len(dtf['Weight'])):
        if dtf['Weight'][c]<=peso:
            dtf=dtf.drop(c)
    return dtf
print(filtro_peso_minimo(df,5000))

#4.3.2
def filtro_antiguedad(dtf,año):
    for c in range(len(dtf['Model Year'])):
        if dtf['Model Year'][c]!=año:
            dtf=dtf.drop(c)
    return dtf

new_df=filtro_antiguedad(df,76)
new_df.reset_index(drop=True, inplace=True)
print(new_df)

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

#4.3.3
año_70=filtro_antiguedad(df,70)
año_79=filtro_antiguedad(df,79)
consumo_medio_año_70=año_70['MPG'].mean()
consumo_medio_año_79=año_79['MPG'].mean()
diferencia_consumo=abs(consumo_medio_año_70-consumo_medio_año_79)
print(diferencia_consumo)

#4.3.4, 4.3.5, 4.3.6
def localizar_defectos(dtf):
    lst=dtf.columns
    dtf1=pd.DataFrame()
    for i in lst:
        for j in range(len(dtf[i])):
            if dtf[i][j]=='?':
                print(f'({i},{j})')
                dtf1[j]=dtf.iloc[j]
    return dtf1.T

df_defectos=localizar_defectos(df)
print(df_defectos)
df_defectos.reset_index(drop=True, inplace=True)
frecuencia_cilindros_defect=frecuencia_serie(df_defectos['Cylinders'])
print(frecuencia_cilindros_defect)


#4.3.7
def filtro_cilindros_minimos(dtf,num):
    for c in range(len(dtf['Cylinders'])):
        if dtf['Cylinders'][c]<num:
            dtf=dtf.drop(c)
    return dtf

def filtro_mpg_maximo(dtf,mpg):
    for c in range(len(dtf['MPG'])):
        if dtf['MPG'][c]>mpg:
            dtf=dtf.drop(c)
    return dtf

df1=filtro_cilindros_minimos(df,6)
df1.reset_index(drop=True, inplace=True)
df1=filtro_peso_minimo(df1,4000)
df1.reset_index(drop=True, inplace=True)
df1=filtro_mpg_maximo(df1,10)
df1.reset_index(drop=True, inplace=True)
print(df1)

class Ejercicio43:
    def __init__(self,df):
        self.df=df
    def filtro_peso_minimo(self,peso):
        for c in range(len(self.df['Weight'])):
            if self.df['Weight'][c]<=peso:
                dtf=self.df.drop(c)
        return dtf
    def filtro_antiguedad(self,año):
        for c in range(len(self.df['Model Year'])):
            if self.df['Model Year'][c]!=año:
                dtf=self.df.drop(c)
        return dtf
    def localizar_defectos(self):
        lst=self.df.columns
        dtf1=pd.DataFrame()
        for i in lst:
            for j in range(len(self.df[i])):
                if self.df[i][j]=='?':
                    print(f'({i},{j})')
                    dtf1[j]=self.df.iloc[j]
        return dtf1.T

    def filtro_minimos(self,num,mpg,peso):
        for c in range(len(self.df['Cylinders'])):
            if self.df['Cylinders'][c]<num | self.df['MPG'][c]>mpg | self.df['Weight'][c]<=peso:
                dtf=self.df.drop(c)
        return dtf
    @staticmethod
    def ejecutar():
        df = pd.read_csv('auto-mpg.csv', sep='\s+', names= np.array(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car_name']))
        ejercicio43=Ejercicio43(df)

        print("4.3.1")
        df5000=ejercicio43.filtro_peso_minimo(5000)
        print(df5000)

        print("4.3.2")
        df76=ejercicio43.filtro_antiguedad(76)
        df76.reset_index(drop=True, inplace=True)
        print(df76)

        print("4.3.3")
        df70=ejercicio43.filtro_antiguedad(70)
        df79=ejercicio43.filtro_antiguedad(79)
        media70=df70["MPG"].mean()
        media79=df79["MPG"].mean()
        diferencia_consumo=abs(media70-media79)
        print(diferencia_consumo)

        print("4.3.4")
        dfNulos=ejercicio43.localizar_defectos()
        print(dfNulos)

        print("4.3.5")


        print("4.3.6")


        print("4.3.7")
        dfMin=ejercicio43.filtro_minimos(6,4000,10)
        print(dfMin)