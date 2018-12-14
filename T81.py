import math
from scipy import interpolate


def g(t):
    return -200*math.cos(100*t) + math.exp(-t)*(math.pow(10, 4)*math.cos(t) - 2*math.sin(100*t))


h = math.pow(10, -3)
y0 = 1
y1 = 1 - 101*h
t = 0
T = []
Y = []
while t <= 2:
    yn = h*h*g(t) - y1*((10**4+2*math.exp(-t))*h*h-2-2*h) - y0
    T.append(t)
    Y.append(yn)
    y0 = y1
    y1 = yn
    t += h


def Inter(z):
    tck = interpolate.splrep(T, Y)
    return interpolate.splev(z, tck)


print(Inter(0.1), Inter(0.5), Inter(1), Inter(1.5), Inter(2))

