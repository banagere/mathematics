import numpy as np

b1, b2, b3 = 2.0, 2.0, 1.0
b = np.array([b1, b2, b3])

A = np.array([[1, 2],
             [1, -1],
             [0, 1]], dtype=float)



u, v, w = np.linalg.solve(A, b)

det = np.linalg.det(A)


print(b)
print(A)
print(det)

print(u, v, w)