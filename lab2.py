import numpy as np
from random import randint
from collections import Counter
N = 3;
M = 4;
a = np.random.randint(0,10,(N,M))
print(a)
f = open('D://papka//lab2.txt','w')  # открытие в режиме записи
f.write(str(a) + "\n")

def foo(matr, l):  # сколько нулей в верхних l строках
    c = 0
    for i in range(l):
        c += np.count_nonzero(matr[i] == 0)#счетчики подсчета с помощью команды numpy, где вместо обычного подсчета используешь команду np.count_nonzero
    return c

def bar(matr, k):  # сколько нулей в левых k столбцах
    c = 0
    for r in matr:
        c += np.count_nonzero(r[:k] == 0)
    return c

b = foo(a,3)
p = bar(a,2)
f.write(str(b) + "\n")
f.write(str(p) + "\n")
print(b)#вывод функции для находения нулей в верхних строках с указанием кол-ва строк
print(p)#вывод функции для находения нулей в левых столбцах с указанием кол-ва столбцов

