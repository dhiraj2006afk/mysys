import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Population
population = np.random.uniform(0, 1, 100000)

# Sample values
n = 30
num = 1000

sample_means = []

for i in range(num):
    sample = np.random.choice(population, n)
    avg = np.mean(sample)
    sample_means.append(avg)

sample_means = np.array(sample_means)

# Calculate values
mean = np.mean(population)
std = np.std(population)

mean_avg = np.mean(sample_means)
std_avg = np.std(sample_means)

se = std / np.sqrt(n)

print("Population Mean:", round(mean, 4))
print("Population SD:", round(std, 4))
print("Mean of Sample Means:", round(mean_avg, 4))
print("SD of Sample Means:", round(std_avg, 4))
print("Theoretical SE:", round(se, 4))

# Plot graph
x = np.linspace(min(sample_means), max(sample_means), 500)
pdf = norm.pdf(x, mean_avg, std_avg)

plt.hist(sample_means, bins=30, density=True, alpha=0.6)
plt.plot(x, pdf, "r", linewidth=2)
plt.title("Central Limit Theorem")
plt.xlabel("Sample Mean")
plt.ylabel("Density")
plt.grid()
plt.show()
