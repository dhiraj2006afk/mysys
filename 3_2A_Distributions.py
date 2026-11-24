# Binomial Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom,norm
p=0.5
n=10
x=np.arange(0,n+1)

prob = binom.pmf(x,n,p)
for i in range(11):
    print("P(X = ",i,") =",round(prob[i],4))

plt.bar(x,prob)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")       
plt.title("Binomial Distribution")
plt.show()

# Normal Distribution
mean = 60
std = 10

x = np.linspace(28, 92, 1000)
pdf = norm.pdf(x, mean, std)

print("Mean:", mean)
print("Standard Deviation:", std)   
print("Variance:", std**2)

probability = norm.cdf(60, mean, std)
print("P(X <= 60) =", round(probability, 4))

plt.plot(x, pdf)
plt.xlabel("X") 
plt.ylabel("Probability Density")
plt.title("Normal Distribution")    
plt.show()