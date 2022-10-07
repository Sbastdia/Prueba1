import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_array = np.array([1.0,2,3,4])
print(data_array)

def convertir(array):
    array=array.astype(int)
    data_df = pd.Series(array)
    return data_df
print(convertir(data_array))

list1=np.array([10, True, 8.00, False, 8, 10])
h=convertir(list1)
print(h)

for i in h:
    print(type(i))

plt.plot(h)
plt.show()

print(h.describe())
