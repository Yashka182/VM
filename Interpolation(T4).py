from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np


x = [i*0.2 for i in range(0, 16)]
F = [0, 1.09351, -0.47812, -0.0620008, 0.965999, -0.960168, -1.42145, -0.328504, -1.88517, -2.36515, 2.33714, -0.684984,
     -0.695581, 1.9807, 2.44249, 3.48356]


def u(i, j):
    return (F[i] - F[j])/(x[i] - x[j])


def v(i, j, k):
    return (u(i, j) - u(j, k))/(x[i] - x[k])


n = 15
a = [0, 0]
for i in range(2, n+1):
    a.append(0.5)


b = [0]
for i in range(1, n+1):
    b.append(2)


c = [0]
for i in range(1, n):
    c.append(0.5)


d = [0*i for i in range(n+2)]
for i in range(1, n):
    d[i] = 6*v(i-1, i, i+1)


Y = [0*i for i in range(n+2)]
A = [0*i for i in range(n+2)]
B = [0*i for i in range(n+2)]
Y[1] = (b[1])
A[1] = (-c[1]/Y[1])
B[1] = (d[1]/Y[1])
Ci = [0*i for i in range(n+1)]
for i in range(2, n):
    Y[i] = b[i] + a[i]*A[i-1]
    A[i] = -c[i]/Y[i]
    B[i] = (d[i] - a[i]*B[i-1])/Y[i]
Y[n] = b[n] + a[n]*A[n-1]
B[n] = (d[n] - a[n]*B[n-1])/Y[n]
Ci[n] = B[n]
for k in reversed(range(1, n)):
    Ci[k] = A[k]*Ci[k+1] + B[k]


Bi = [0*i for i in range(n+1)]
Bi[1] = Ci[1]*0.2/3 + u(0, 1)
for i in range(2, n+1):
    Bi[i] = Ci[i]*0.2/3 + Ci[i-1]*0.2/6 + u(i-1, i)


Di = [0*i for i in range(n+2)]
Di[1] = Ci[1]/0.2
for i in range(2, n+1):
    Di[i] = (Ci[i] - Ci[i-1])/0.2


def getvalue(y):
    t = 0
    P = 0
    for i in range(n):
        if x[i] < y < x[i+1]:
            t = i + 1
            print(t)
            P = F[t] + Bi[t]*(y - x[t]) + 0.5*Ci[t]*(y - x[t])**2 + (1/6)*Di[t]*(y - x[t])**3
            break
        elif(y==x[i+1]):
            P = F[i+1]
    return P

h = 0.02


def getderivative1(y):

    return (getvalue(y + h) - getvalue(y - h))/(2*h)



M = 2.3
V = getvalue(M)

print(V)


def f(z):
    tck = interpolate.splrep(x, F)
    return interpolate.splev(z, tck)


print(f(M))


lag = 0.001
X = np.arange(0, 3.1, 0.1)
fig = plt.figure()
val = []
der = []
for i in range(len(X)):
    val.append(getvalue(X[i]))
for i in range(len(X)):
    der.append(getderivative1(X[i]))
plt.plot(X, val, color = "red", linestyle = "solid")
plt.plot(X, f(X), color = "blue", linestyle="dashed")
plt.plot(X, der, color = "green", linestyle="solid")
for i in range(len(x)):
    plt.scatter(x[i], F[i])


plt.show()
