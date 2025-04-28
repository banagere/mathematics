import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4])
move_up = 1.7
move_down = 0.3

matrix_a = np.array([[1, 0], [0, 1]]) * move_up
matrix_b = np.array([[-1, 0], [0, 1]]) * move_down
matrix_c = np.array([[-1, 0], [0, -1]]) * move_down
matrix_d = np.array([[1, 0], [0, -1]]) * move_up

shift_1_quadrant = np.dot(matrix_a, x)
shift_2_quadrant = np.dot(matrix_b, x)
shift_3_quadrant = np.dot(matrix_c, x)
shift_4_quadrant = np.dot(matrix_d, x)

# Plot
plt.figure(figsize=(6, 6))
plt.title("Scaled Vectors on Cartesian Plane")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)

# Plot vectors
def plot_vector(start, end, color, label):
    plt.quiver(start[0], start[1], end[0] - start[0], end[1] - start[1], 
               angles='xy', scale_units='xy', scale=1, color=color, label=label)

plot_vector([0, 0], shift_1_quadrant, 'black', "Quadrant 1")
plot_vector([0, 0], shift_2_quadrant, 'red', "Quadrant 2")
plot_vector([0, 0], shift_3_quadrant, 'blue', "Quadrant 3")
plot_vector([0, 0], shift_4_quadrant, 'violet', "Quadrant 4")

plt.legend()
plt.show()
