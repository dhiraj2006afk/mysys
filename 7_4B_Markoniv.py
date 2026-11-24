import numpy as np
import matplotlib.pyplot as plt

# Transition Matrix
P = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.6, 0.3],
    [0.4, 0.2, 0.4]
])

# State names
states = ["Sunny", "Cloudy", "Rainy"]

# Calculate n-step transition matrix
for n in [1, 2, 5, 10, 20]:
    Pn = np.linalg.matrix_power(P, n)
    print("\n", n, "step transition matrix:")
    print(np.round(Pn, 4))

# Probability of Rainy after 5 steps from Sunny
print("\nProbability of Rainy after 5 steps from Sunny:")
print(round(np.linalg.matrix_power(P, 5)[0][2], 4))

# Calculate probability starting from Sunny
evolution = []

for n in range(1, 21):
    Pn = np.linalg.matrix_power(P, n)
    evolution.append(Pn[0])

evolution = np.array(evolution)

# Plot graph
for i in range(3):
    plt.plot(range(1, 21), evolution[:, i],
             marker="o", label=states[i])

plt.xlabel("Number of Steps")
plt.ylabel("Transition Probability")
plt.title("Markov Chain Transition Probability")
plt.legend()
plt.grid()
plt.show()