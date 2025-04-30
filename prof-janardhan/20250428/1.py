import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

b1, b2, b3 = [6.0, 5.0, 3.0]
b = np.array([b1, b2, b3])

A = np.array([[1, 1, 1],
                  [0, 1, 1],
                  [0, 0, 1]], dtype=float)

u, v, w = np.linalg.solve(A, b)


print(b)
print(A)

print(u, v, w)


# column vectors
a1, a2, a3 = A[:,0], A[:,1], A[:,2]

# scaled vectors
U = u * a1
V = v * a2
W = w * a3

# parallelepiped vertices
O   = np.zeros(3)
UV  = U + V
UW  = U + W
VW  = V + W
UVW = U + V + W

# faces of the parallelepiped
faces = [
    [O, U, UV, V],
    [O, U, UW, W],
    [O, V, VW, W],
    [UVW, UV, U, UW],
    [UVW, UV, V, VW],
    [UVW, UW, W, VW],
]

fig = plt.figure(figsize=(8,6))
ax  = fig.add_subplot(111, projection='3d')

# plot arrows with visible heads
for start, vec, label in [
    (O,   U,   'u·a₁'),
    (U,   V,   'v·a₂'),
    (U+V, W,   'w·a₃'),
    (O,   b,   'b')
]:
    ax.quiver(*start, *vec,
              arrow_length_ratio=0.05,
              linewidth=2,
              normalize=False)

# fill parallelepiped
poly = Poly3DCollection(faces,
                        facecolors='skyblue',
                        edgecolors='gray',
                        linewidths=1,
                        alpha=0.4)
ax.add_collection3d(poly)

ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('x₃')
ax.set_box_aspect([1,1,1])
plt.tight_layout()
plt.show()