import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4])
matrix_a = np.array([[1, 0], [0, 1]])
matrix_b = np.array([[-1, 0], [0, 1]])
matrix_c = np.array([[-1, 0], [0, -1]])
matrix_d = np.array([[1, 0], [0, -1]])



shift_1_quadrant = np.dot(matrix_a, x)
shift_2_quadrant = np.dot(matrix_b, x)
shift_3_quadrant = np.dot(matrix_c, x)
shift_4_quadrant = np.dot(matrix_d, x)


# plot
# plt.scatter(x[0], x[1], color="black", label="Original")
plt.scatter(shift_1_quadrant[0], shift_1_quadrant[1], color="black", label="quadrant 1")
plt.scatter(shift_2_quadrant[0], shift_2_quadrant[1], color="red", label="quadrant 2")
plt.scatter(shift_3_quadrant[0], shift_3_quadrant[1], color="blue", label="quadrant 3")
plt.scatter(shift_4_quadrant[0], shift_4_quadrant[1], color="violet", label="quadrant 4")
plt.title("Vector on Cartesian Plane")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()