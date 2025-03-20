import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[58, 79, 32], [12, 34, 98], [83, 64, 33]])

determinant_x = np.linalg.det(x)
determinant_y = np.linalg.det(y)

inverse_x = np.linalg.inv(x)
inverse_y = np.linalg.inv(y)

print(f"\n x: \n{x}")
print(f"\n determinant_x: \n{determinant_x}")
print(f"\n inverse_x: \n{inverse_x}")

print(f"\n y: \n{y}")
print(f"\n determinant_y: \n{determinant_y}")
print(f"\n inverse_y: \n{inverse_y}")
