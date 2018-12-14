import math
from scipy import interpolate


def f(t):
    return math.exp(t)*t*t*math.cos(t)+2+2*t**3-t**4+2*t**2


n = 1000
h = math.pi/n

a = [0]
for i in range(1, n):
    a.append(1+((h*i)**2-2)*h)
a.append(0)

b = [1]
for i in range(1, n):
    b.append(-2-((i*h)**2-2)*h+((i*h)**2-2)*h*h*math.cos(i*h))
b.append(1)

c = [0]
for i in range(1, n):
    c.append(1)

d = [0]
for i in range(1, n):
    d.append(f(1+i*h)*h*h)
d.append((math.pi)**2)

Y = [0]*(n+1)
A = [0]*(n+1)
B = [0]*(n+1)
y = [0]*(n+1)
Y[0] = b[0]
A[0] = -c[0]/Y[0]
B[0] = d[0]/Y[0]
for i in range(1, n):
    Y[i] = b[i] + a[i] * A[i - 1]
    A[i] = -c[i] / Y[i]
    B[i] = (d[i] - a[i] * B[i - 1]) / Y[i]
Y[n] = b[n] + a[n]*A[n-1]
B[n] = (d[n] - a[n]*B[n-1])/Y[n]
y[n] = B[n]
for k in reversed(range(n)):
    y[k] = A[k]*y[k+1] + B[k]

x = []
for i in range(len(y)):
    x.append(i*h)


def Inter(z):
    tck = interpolate.splrep(x, y)
    return interpolate.splev(z, tck)


print(Inter(0.5), Inter(1), Inter(1.5), Inter(2), Inter(2.5), Inter(3))

