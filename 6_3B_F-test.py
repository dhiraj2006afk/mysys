import numpy as np
from scipy.stats import f

A=[10.2,9.8,10.5,10.1,9.9,10.3,10.0]
B=[9.5,10.6,9.2,10.8,9.4,10.9,9.1]

var1=np.var(A,ddof=1)
var2=np.var(B,ddof=1)

n1 = len(A)
n2 = len(B)

if var1 >= var2:
	F = var1/var2
	df1 = n1-1
	df2 = n2-1
else:
	F=var2/var1
	df1=n2-1
	df2=n1-1

c=f.cdf(F,df1,df2)
p=2*min(c,1-c)

critical = f.ppf(1-0.05/2,df1,df2)

print("Var1 - ",round(var1,4))
print("Var2 - ",round(var2,4))
print("F distribution -",round(F,4))
print("P value-",round(p,4))
print("Critical- ",round(critical,4))

if p <= 0.05:
	print("Reject H0")
else:
	print("Fail to reject H0")
