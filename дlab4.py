import numpy as np
from math import sin
from math import cos


def f(x, y):
    fx1 = 2 * (-0.8 + x + cos(1 - x) * (-0.1 + y - sin(1 - x)) - sin(1 + y))
    fx2 = 2 * (-0.1 + y - sin(1 - x) - cos(1 + y) * (-0.8 + x - sin(1 + y)))
    return fx1, fx2


x1, x2 = 1, 0
a = 0.23
eps = 0.000001
dx = [1]

print(f'k\t[x1, x2]\t\t\t\tdelta_x')
print(f'0\t{x1:.6f}, {x2:.6f}')

k = 1
while dx[-1] > eps:
    X = np.array([x1, x2])
    F = np.array(f(x1, x2))

    nx1, nx2 = X - a * F
    dx.append(max(abs(nx1 - x1), abs(nx2 - x2)))
    x1, x2 = nx1, nx2

    print(f'{k}\t{x1:.6f}, {x2:.6f}\t\t{dx[-1]:.6f}')
    k += 1

print(f'\nx* = [{x1:.6f}, {x2:.6f}]')