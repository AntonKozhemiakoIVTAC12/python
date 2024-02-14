import numpy as np
from random import randint
from collections import Counter
N = 3;
M = 4;
a = np.random.randint(0,10,(N,M))
print(a)

def foo(matr, l):  # сколько нулей в верхних l строках
    c = 0
    for i in range(l):
        c += np.count_nonzero(matr[i] == 0)
    return c


def bar(matr, k):  # сколько нулей в левых k столбцах
    c = 0
    for r in matr:
        c += np.count_nonzero(r[0:k] == 0)
    return c
# 1st argument --> numbers ranging from 0 to 9,
# 2nd argument, row = 2, col = 3


print(foo(a,3))
print(bar(a,2))

