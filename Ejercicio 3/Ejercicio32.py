import numpy as np
matriz=np.arange(0,100,9).reshape(3,4)
print(len(matriz))
for i in range(len(matriz)):
    for j in range(len(matriz+1)):
        if matriz[i][j]%5==0:
            pass
        else:
            matriz[i][j]=-1
print(matriz)