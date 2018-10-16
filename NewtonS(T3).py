import matplotlib.pyplot as plt
import numpy as np
import math

'''lag = 0.001
x = np.arange(-2, 2, lag)
y = np.tan(x)
fig = plt.figure()

circle = plt.Circle((0, 0), 1, color='b')
ax = plt.gca()
ax.cla()
plt.plot(x, y)
ax.add_artist(circle)


plt.grid(True)

plt.show()'''


def mtr(u):
    return [u[0]**2 + u[1]**2 - 1, u[1] - math.tan(u[0])]


def J(u):
    det = 1/(2*u[0] + 2*u[1]/(math.cos(u[0]))**2)
    return [[det, det*((1/math.cos(u[0]))**2)], [(-2*u[1])*det, 2*u[0]*det]]


def opmtr22(x):
    matrix = []
    det = x[1][1]*x[2][2] - x[1][2]*x[2][1]
    matrix[1][1] = x[2][1]/det
    matrix[2][2] = x[1][1]/det
    matrix[1][2] = -x[1][2]/det
    matrix[2][1] = -x[2][1]/det
    return matrix


'''def multiply22(x, y):
    matrix = [[0, 0], [0, 0]]
    matrix[0][0] = x[0][0]*y[0][0] + x[1][0]*y[0][1]
    matrix[1][0] = x[0][0]*y[1][0] + x[1][0]*y[1][1]
    matrix[0][1] = x[0][1]*y[0][0] + x[1][1]*y[0][1]
    matrix[1][1] = x[0][1]*y[1][0] + x[1][1]*y[1][1]
    return matrix'''


def multiply21(x, y):
    matrix = [0, 0]
    matrix[0] = x[0][0]*y[0] + x[1][0]*y[1]
    matrix[1] = x[0][1]*y[0] + x[1][1]*y[1]
    return matrix


def subtract(x, y):
    matrix = [0, 0]
    matrix[0] = x[0] - y[0]
    matrix[1] = x[1] - y[1]
    'matrix[0][1] = x[0][1] - y[0][1]'
    'matrix[1][1] = x[1][1] - y[1][1]'
    return matrix


def norm(u):
    return max(u[0], u[1])


def newtons(lx, rx, ly, ry):
    u0 = [(lx+rx)/2, (ly+ry)/2]
    u1 = subtract(u0, multiply21(J(u0), mtr(u0)))
    while norm(subtract(u1, u0)) > math.pow(10, -6):
        u0 = u1
        u1 = subtract(u0, multiply21(J(u0), mtr(u0)))
    return u1


print(newtons(0, 1.5, 0, 2))
print(newtons(-1.5, 0, -2, 0))



