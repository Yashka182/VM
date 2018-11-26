import math


def f(x):
    return x*math.cos(x) - 0.56


def der(x):
    return math.cos(x) - x*math.sin(x)


def newton(left, right):
    x0 = (left + right)/2
    x1 = x0 - f(x0)/der(x0)
    a = 10
    m = -6
    while abs(x1 - x0) > math.pow(a, m):
        x0 = x1
        x1 = x0 - f(x0) / der(x0)
    print(x1)
    return x1


def rootsearch(left, right, n):
    #left = int(input("Ведите левую границу "))
    #right = int(input("Ввелите правую границу "))
    #n = int(input("Введите количество отрезков "))
    dx = (right - left)/n
    p = 1
    roots = {1 : left}
    for i in range(-1, n):
        if f(left + i*dx)*f(left + (i+1)*dx) <= 0:
            p += 1
            roots[p] = left + i*dx
            print(p)
            print(left+i*dx)
    roots[p + 1] = right
    return roots


roots1 = rootsearch(-2, 2, 50)
solutions = {}
for n in range(1, len(roots1) - 1):
    solutions[n] = newton(roots1[n], roots1[n + 1])
print(dict.items(solutions))
