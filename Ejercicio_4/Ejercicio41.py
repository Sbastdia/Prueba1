from matplotlib import pyplot as plt
import numpy as np

x = list(range(1, 10))
y = np.ones(9)

plt.plot(x, y, 'o', color='red')
plt.show()
