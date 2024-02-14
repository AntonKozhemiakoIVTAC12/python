import random
import math
import matplotlib.pyplot as plt

class LFSRGenerator:
    def __init__(self, seed, feedback_mask):
        self.state = seed
        self.feedback_mask = feedback_mask

    def generate_bit(self):
        feedback = sum(self.state[i] for i in self.feedback_mask) % 2
        output_bit = self.state[-1]

        self.state = [feedback] + self.state[:-1]

        return output_bit

    def generate_number(self, num_bits):
        output_number = 0
        for _ in range(num_bits):
            output_number = (output_number << 1) | self.generate_bit()
        return output_number

def create(n):
    t = []
    de = (1 / n)

    seed = [random.randint(0, 1) for _ in range(10)]  # Начальное состояние
    feedback_mask = [2, 9]  # Маска обратной связи

    generator = LFSRGenerator(seed, feedback_mask)

    for i in range(n):
        j = generator.generate_number(16) / 65535.0  # Генерация числа между 0 и 1
        t.append(j)

    m = 0
    for i in t:
        m += abs(i * de)

    d = 0
    for i in t:
        d += abs(((i - m) ** 2) * de)

    s = math.sqrt(d)

    return t, m

N_values = [100, 1000, 10000]

for N in N_values:
    random_sequence, M = create(N)

    interval_probabilities = [0] * 50
    interval_size = 1.0 / len(interval_probabilities)

    for value in random_sequence:
        interval_index = int(value / interval_size)
        interval_probabilities[interval_index] += 1

    total_samples = len(random_sequence)

    for i in range(len(interval_probabilities)):
        interval_probabilities[i] /= total_samples

    print(f'\nДля N = {N}:')
    print(f'Математическое ожидание (М): {M:.10f}')
    print(f'Дисперсия (D): {sum((x - M) ** 2 for x in random_sequence) / (N - 1):.10f}')
    print(
        f'Среднеквадратичное отклонение: {math.sqrt(sum((x - M) ** 2 for x in random_sequence) / (N - 1)):.10f}')
    probability_str = ' '.join(map(lambda x: str(x).replace('.', ','), interval_probabilities))
    print('Вероятности для интервалов:')
    for prob in probability_str.split():
        print(prob)

# Создаем зависимость (M-Mi) от i для N = 1000
# N = 1000
# random_sequence, M = create(N)
# M_values = [(M - x) for x in random_sequence]
#
# for i in range(10):
#     print(f'\nЗависимость (M-Mi) для N = {N} и i = {i + 1}:')
#     diff = M_values[i]
#     print(f"(M-M{i + 1}) = {diff:.10f}")
# # Создаем зависимость (M-Mi) от i для n = 1000 * i, где i изменяется от 1 до 10, исключая N = 1000
# N_values = [1000 * i for i in range(1, 11) if i != 1]
#
# for N in N_values:
#     random_sequence, M = create(N)
#     M_values = [(M - x) for x in random_sequence]
#
#     i = 1  # Выводим только для i = 1
#     print(f'\nЗависимость (M-Mi) для N = {N} и i = {i}:')
#     diff = M_values[i - 1]
#     print(f"(M-M{i}) = {diff:.10f}")