import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    a = math.exp(x)*math.sin(x) - 1
    return a


def der(x):
    return math.exp(x)*(math.sin(x) + math.cos(x))


def rootsearch(left, right, n):
    #left = int(input("Ведите левую границу "))
    #right = int(input("Ввелите правую границу "))
    #n = int(input("Введите количество отрезков "))
    dx = (right - left)/n
    p = 0
    roots = {}
    for i in range(-1, n):
        if f(left + i*dx)*f(left + (i+1)*dx) <= 0:
            p += 1
            roots[p] = left + i*dx
            print(p)
            print(left+i*dx)
    return roots


def newton(left, right, a, m):
    x0 = (left + right)/2
    x1 = x0 - f(x0)/der(x0)
    while abs(x1 - x0) > math.pow(a, m):
        x0 = x1
        x1 = x0 - f(x0) / der(x0)
    print(x1)
    return x1

h = 0.02


def getderivative1(y):

    return (f(y + h) - f(y - h))/(2*h)


roots1 = rootsearch(-10, 10, 20)
newton(roots1[2], roots1[3], 10, -6)

lag = 0.001
X = np.arange(0, 3.1, 0.1)
fig = plt.figure()
val = []
deriv = []
d = []
for i in range(len(X)):
    val.append(f(X[i]))
for i in range(len(X)):
    deriv.append(der(X[i]))
for i in range(len(X)):
    d.append(getderivative1(X[i]))
plt.plot(X, val, color = "red", linestyle = "solid")
plt.plot(X, d, color = "green", linestyle="solid")
plt.plot(X, deriv, color = "blue", linestyle="dashed")

plt.show()
