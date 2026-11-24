import numpy as np
import matplotlib.pyplot as plt

# Data
x = [2, 4, 6, 8, 10, 3, 7, 5, 9, 1]
y = [50, 60, 68, 82, 90, 55, 75, 65, 88, 40]

# Convert into arrays
x = np.array(x)
y = np.array(y)

# Manual calculation
xm = np.mean(x)
ym = np.mean(y)

num = np.sum((x-xm) * (y-ym))
den = np.sqrt(np.sum((x-xm)**2) * np.sum((y-ym)**2))

r_manual = num / den

# NumPy calculation
r_numpy = np.corrcoef(x, y)[0, 1]

# Display both results
print("Manual correlation:", round(r_manual, 4))
print("NumPy correlation:", round(r_numpy, 4))

# Compare both
if np.isclose(r_manual, r_numpy):
    print("Both results are equal")

# Interpretation
if r_manual > 0.7:
    print("Strong Positive Correlation")
elif r_manual > 0.3:
    print("Moderate Positive Correlation")
elif r_manual > -0.3:
    print("Weak or No Linear Correlation")
elif r_manual > -0.7:
    print("Moderate Negative Correlation")
else:
    print("Strong Negative Correlation")

# Scatter plot
plt.scatter(x, y, label="Data Points")

# Best-fit line
m, c = np.polyfit(x, y, 1)
plt.plot(x, m*x+c, "r--", label="Best Fit Line")

plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Hours Studied vs Marks")
plt.legend()
plt.grid()
plt.show()