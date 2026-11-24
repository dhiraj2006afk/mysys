import numpy as np
import matplotlib.pyplot as plt

# Given data
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Divided difference function
def divided_diff(x, y):
    n = len(x)

    table = []
    for i in range(n):
        table.append([0] * n)

    for i in range(n):
        table[i][0] = y[i]

    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])

    return table

# Calculate divided difference table
table = divided_diff(x, y)

print("Divided Difference Table:")
for row in table:
    print(row)

# Newton interpolation function
def newton(x, table, value):
    n = len(x)
    result = table[0][0]
    product = 1

    for i in range(1, n):
        product = product * (value - x[i-1])
        result = result + table[0][i] * product

    return result

# Find interpolated value
x_new = 2.5
y_new = newton(x, table, x_new)

print("\nInterpolated value:", round(y_new, 4))

# Generate curve points
x_range = np.linspace(min(x), max(x), 200)
y_range = []

for value in x_range:
    y_range.append(newton(x, table, value))

# Plot graph
plt.scatter(x, y, color="red", label="Known Points")
plt.plot(x_range, y_range, color="purple", label="Newton Curve")
plt.scatter(x_new, y_new, color="green", marker="x",
            s=100, label="Interpolated Point")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Newton Divided Difference Interpolation")
plt.legend()
plt.grid()
plt.show()