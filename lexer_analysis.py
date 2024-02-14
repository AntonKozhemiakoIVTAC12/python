import math

# Заданные значения
k = 12
target_probability = 0.05

# Перебор значений
closest_t0 = None
closest_lambda = None
closest_probability = float('inf')

for t0 in range(10, 29):
    for lambd in range(10, 29):
        a = t0 * lambd / 60
        probability = (a ** k / math.factorial(k)) * math.exp(-a)

        # Проверка на близость к 0.05
        if abs(probability - target_probability) < abs(closest_probability - target_probability):
            closest_t0 = t0
            closest_lambda = lambd
            closest_probability = probability

print("Ближайшие значения:")
print("t0 =", closest_t0)
print("lambda =", closest_lambda)
print("Вероятность =", closest_probability)
