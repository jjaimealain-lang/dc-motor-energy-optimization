import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
y = np.sin(t)

plt.plot(t, y)
plt.show()