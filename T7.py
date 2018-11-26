import math
from scipy import interpolate


def f(x):
    return math.exp(-2*x)*((math.cos(x) - math.sin(x))/math.cos(x))**2


e = math.pow(10, -6)
c2 = 1
a21 = c2
b2 = 1/(2*c2)
b1 = 1 - 1/(2*c2)

def mrk2():
    N = 100
    h = 1 / N
    a = 0
    b = 1
    x0 = a
    y0 = 0
    X = [0]*(N+2)
    Y = [0]*(N+2)
    X[1] = x0
    Y[1] = y0
    solutions = [0]*(N+2)
    for i in range(1, N+1):
        k1 = f(x0)
        k2 = f(x0 + a21*h*k1)
        y1 = y0 + h*(b1*k1 + b2*k2)

        x0 = x0 + h
        y0 = y1
        X[i+1] = x0
        Y[i+1] = y1
        solutions[i] = [X[i], Y[i]]
    print(solutions)
    return solutions


def mrk2AS():
    x = 0
    y = 0
    b = 1
    N = 100
    h1 = 1/100
    h2 = h1/2
    H = []
    solutions = []
    solutions.append([x, y])
    while x < b:
        k1 = f(x)
        k2 = f(x + a21 * h1 * k1)
        y1 = y + h1 * (b1 * k1 + b2 * k2)

        K1 = k1
        K2 = f(x + a21 * h2 * K1)
        y21 = y + h2 * (b1 * K1 + b2 * K2)

        K12 = f(x+h2)
        K22 = f(x + h2 + a21 * h2 * K12)
        y22 = y21 + h2*(b1 * K12 + b2 * K22)

        if (y1 - y22)/(2**2 - 1) > e:
            h1 = h1/2
        else:
            h1 = h1*2
        H.append(h1)
        x = x + h1
        y = y1
        solutions.append([x, y])
    H.sort()
    results = [solutions, H.pop()]
    return results


Res = mrk2AS()
sol = Res[0]
Hmax2 = Res[1]
u = []
v = []
for i in range(len(sol)):
    u.append(sol[i][0])
    v.append(sol[i][1])


def Inter(z):
    tck = interpolate.splrep(u, v)
    return interpolate.splev(z, tck)


print(Inter(0.1), Inter(0.25), Inter(0.5), Inter(0.75), Inter(1))
print(Hmax2)


def mrk4AS():
    x = 0
    y = 0
    b = 1
    h1 = 1 / 100
    h2 = h1 / 2
    H = []
    solutions = []
    solutions.append([x, y])
    while x < b:
        k1 = h1*f(x)
        k2 = h1*f(x + k1/2)
        k3 = h1*f(x + k2/2)
        k4 = h1*f(x + k3)
        y1 = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

        K1 = h2 * f(x)
        K2 = h2*f(x + K1/2)
        K3 = h2*f(x + K2/2)
        K4 = h2*f(x + K3)
        y21 = y + (1 / 6) * (K1 + 2 * K2 + 2 * K3 + K4)

        K12 = h2*f(x + h2)
        K22 = h2 * f(x + h2 + K12 / 2)
        K32 = h2 * f(x + h2 + K22 / 2)
        K42 = h2 * f(x + h2 + K32)
        y22 = y21 + (1 / 6) * (K12 + 2 * K22 + 2 * K32 + K42)

        if (y1 - y22) / (2 ** 2 - 1) > e:
            h1 = h1 / 4
        else:
            h1 = h1 * 4
        H.append(h1)
        x = x + h1
        y = y1
        solutions.append([x, y])
    H.sort()
    results = [solutions, H.pop()]
    return results

Res4 = mrk4AS()
sol4 = Res4[0]
Hmax4 = Res4[1]
I = []
J = []
for i in range(len(sol4)):
    I.append(sol4[i][0])
    J.append(sol4[i][1])


def Interpol(z):
    tck = interpolate.splrep(I, J)
    return interpolate.splev(z, tck)


print(Interpol(0.1), Interpol(0.25), Interpol(0.5), Interpol(0.75), Interpol(1))
print(Hmax4)

