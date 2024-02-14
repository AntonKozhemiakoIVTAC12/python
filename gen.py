import random
import numpy as np

# Функция для генерации N случайных чисел
def generate_random_sequence(N):
    return [random.random() for _ in range(N)]

# Функция для вычисления математического ожидания и дисперсии
def compute_stats(sequence):
    mean = np.mean(sequence)
    variance = np.var(sequence)
    std_deviation = np.sqrt(variance)
    return mean, variance, std_deviation

# Функция для вычисления вероятности попадания числа в интервал
def compute_probability(sequence, num_intervals):
    interval_counts = [0] * num_intervals
    for value in sequence:
        interval = int(value * num_intervals)
        interval_counts[interval] += 1
    probability = [count / len(sequence) for count in interval_counts]
    return probability

# Заданные значения N
N_values = [100, 1000, 10000]

for N in N_values:
    random_sequence = generate_random_sequence(N)
    mean, variance, std_deviation = compute_stats(random_sequence)
    num_intervals = 50  # Количество интервалов

    probability = compute_probability(random_sequence, num_intervals)

    print(f"Для N = {N}:")
    print(f"Математическое ожидание (М): {mean:.4f}")
    print(f"Дисперсия (D): {variance:.4f}")
    print(f"Среднеквадратичное отклонение: {std_deviation:.4f}")
    probability_str = ' '.join(map(lambda x: str(x).replace('.', ','), probability))
    print('Вероятности для интервалов:')
    for prob in probability_str.split():
        print(prob)

# N = 1000
# random_sequence = generate_random_sequence(N)  # Генерация новой последовательности для N = 1000
# mean, variance, std_deviation = compute_stats(random_sequence)
# M_values = [(mean - x) for x in random_sequence]
#
# for i in range(10):
#     print(f'\nЗависимость (M-Mi) для N = {N} и i = {i + 1}:')
#     diff = M_values[i]
#     print(f"(M-M{i + 1}) = {diff:.10f}")
#
# # Создаем зависимость (M-Mi) от i для N = 1000 * i, где i изменяется от 1 до 10, исключая N = 1000
# N_values = [1000 * i for i in range(1, 11)]
#
# for N in N_values:
#     random_sequence = generate_random_sequence(N)  # Генерация новой последовательности для каждого N
#     mean, variance, std_deviation = compute_stats(random_sequence)
#     M_values = [(mean - x) for x in random_sequence]
#
#     i = 1  # Выводим только для i = 1
#     print(f'\nЗависимость (M-Mi) для N = {N} и i = {i}:')
#     diff = M_values[i - 1]
#     print(f"(M-M{i}) = {diff:.10f}")