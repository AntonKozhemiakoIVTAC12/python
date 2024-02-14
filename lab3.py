from math import *

# Функция, вычисляющая значение заданной функции
def calculate_function_value(x):
    if -9 <= x <= -7:
        y = 0
    elif -7 <= x < -3:
        y = x + 7
    elif -3 <= x < -2:
        y = 4
    elif -2 <= x < 0:
        y = x**2
    elif 0 <= x < 2:
        y = x**2
    elif 2 <= x <= 4:
        y = -2*x + 8
    else:
        y = 0
    return y

# Ввод значений переменных
Xbeg = float(input('Введите начальное значение Xbeg: '))
Xend = float(input('Введите конечное значение Xend: '))
Dx = float(input('Введите шаг dx: '))

# Начальное значение
Xt = Xbeg

# Заголовок таблицы
print(f"+{'-'*8}+{'-'*8}+")
print("| I X I Y I")
print(f"+{'-'*8}+{'-'*8}+")

# Цикл вычисления и вывода значений функции
while Xt <= Xend:
    Yt = calculate_function_value(Xt)
    print(f"| {Xt:.2f} | {Yt:.2f} |")
    Xt += Dx

# Завершение таблицы
print(f"+{'-'*8}+{'-'*8}+")