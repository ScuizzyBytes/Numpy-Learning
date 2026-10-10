import numpy as np

array = np.array([10, 5, 20, 2, 15, 23, 87, 56, 12, 56 ,7])

pidoras = np.where((array >= 10) | (array == 2), "_", array)

print(pidoras)