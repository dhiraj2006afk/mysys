import numpy as np
import matplotlib.pyplot as plt

# Given data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 7]

# Lagrange interpolation function
def lagrange(x, y, value):
    result = 0
    n = len(x)

    for i in range(n):
        term = y[i]

        for j in range(n):
            if i != j:
                term = term * (value - x[j]) / (x[i] - x[j])

        result = result + term

    return result

# Find interpolated value
x_new = 2.5
y_new = lagrange(x, y, x_new)

print("Interpolated value:", round(y_new, 4))

# Generate curve values
x_range = np.linspace(min(x), max(x), 200)
y_range = []
for value in x_range:
    y_range.append(lagrange(x, y, value))

# Plot graph
plt.scatter(x, y, color="red", label="Known Points")
plt.plot(x_range, y_range, color="blue", label="Interpolation Curve")
plt.scatter(x_new, y_new, color="green", marker="x",
            s=100, label="Interpolated Point")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Lagrange Interpolation")
plt.legend()
plt.grid()
plt.show()

