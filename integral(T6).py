import math
import numpy as np


def f(x):
    return math.sin(100*x)*math.exp(x**2)*math.cos(2*x)


n = 30000
step = 0.0001
x = []
for i in range(n+1):
    x.append(step*i)


I = [0]*(n+1)
for i in range(n):
    I[i] = step*(f(x[i+1]) + f(x[i]))/2


print(sum(I))

