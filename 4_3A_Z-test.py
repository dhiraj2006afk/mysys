# Z-test
import numpy as np
from scipy.stats import norm

np.random.seed(10) # Generate random data
data = np.random.normal(102,3,40) # mean = 102, std = 3, n = 40

mean0 = 100 # Null hypothesis mean
alpha = 0.05 # Significance level
alternative = "two-sided" # Type of test

n = len(data) # Sample size
avg = np.mean(data) # Sample mean
sigma = np.std(data, ddof=1) # Sample standard deviation

z = (avg - mean0) / (sigma / np.sqrt(n)) # Z statistic

if alternative == "two-sided":
    p = 2*(1-norm.cdf(abs(z))) # Two-sided p-value
elif alternative == "greater":
    p = 1-norm.cdf(z) # One-sided p-value (greater)
elif alternative == "less":
    p = norm.cdf(z) # One-sided p-value (less)

print("Sample mean:", round(avg, 4))
print("Z statistic:", round(z, 4))
print("P-value:", round(p, 4))

if p <= alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")