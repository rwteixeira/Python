matrix = [[1, 2, 3,
           4, 5, 6,
           7, 8, 9]]
print([[i + 1 for i in row] for row in matrix])

# -----------------------------------------------

# Importar o NumPy
import numpy as np
array1 = np.array([10, 100, 1000.])
array2 = np.array([[1., 2., 3.],
                   [4., 5., 6.]])

print(array1)
print(array2)

print("-" * 40)

print(array2 + 1)
