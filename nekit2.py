import numpy as np
import matplotlib.pyplot as plt
import math  # Используем стандартную библиотеку math для факториала

# Параметры для распределения Пуассона
lambda_parameter = 30  # Математическое ожидание
sample_size = 1000  # Увеличим размер выборки для лучшей оценки

t = []
for _ in range(sample_size):
    x = np.random.poisson(lambda_parameter)
    t.append(x)

t.sort()

# Выведем математическое ожидание и дисперсию, чтобы оценить соответствие с параметрами распределения
mean = np.mean(t)
variance = np.var(t)
print('Математическое ожидание (M):', mean)
print('Дисперсия (D):', variance)

# Строим графики
plt.figure(figsize=(12, 4))

# График функции плотности вероятностей f(X)
plt.subplot(131)
plt.hist(t, bins=range(max(t)+1), density=True, color='b', alpha=0.5, rwidth=0.85)
plt.title('Функция плотности вероятностей f(X)')
plt.xlabel('Значение X')
plt.ylabel('Плотность вероятности')

# График функции распределения вероятностей F(X)
plt.subplot(132)
plt.hist(t, bins=range(max(t)+1), density=True, color='g', alpha=0.5, cumulative=True, rwidth=0.85)
plt.title('Функция распределения вероятностей F(X)')
plt.xlabel('Значение X')
plt.ylabel('Вероятность')

# График плотности вероятностей p(X) (по распределению Пуассона)
x = np.arange(0, max(t) + 1)
p = [math.exp(-lambda_parameter) * (lambda_parameter ** i) / math.factorial(i) for i in x]
plt.subplot(133)
plt.plot(x, p, 'r.-')
plt.title('Плотность вероятностей p(X)')
plt.xlabel('Значение X')
plt.ylabel('Плотность вероятности')

plt.tight_layout()
plt.show()
