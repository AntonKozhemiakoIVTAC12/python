import math

def taylor_series_arctan(x, epsilon):
    result = 0.0
    n = 0

    while True:
        term = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        result += term
        n += 1

        if abs(term) < epsilon:
            break

    return result, n

def generate_table(X_start, X_end, step, epsilon):
    # Вывести заголовок таблицы
    print(f"I X I Y I N I")
    print("+--------+--------+-----+")

    X = X_start

    while X <= X_end:
        result, terms_summed = taylor_series_arctan(X, epsilon)
        print(f"I {X: .2f} I {result: .3f} I {terms_summed:2d} I")
        X += step

    # Вывести завершающую строку таблицы
    print("+--------+--------+-----+")

if __name__ == "__main__":
    # Ввести значения переменных X_start, X_end, step и параметр точности epsilon
    X_start = float(input("Введите начальное значение X: "))
    X_end = float(input("Введите конечное значение X: "))
    step = float(input("Введите шаг: "))
    epsilon = float(input("Введите точность epsilon: "))

    # Вывести "шапку" таблицы
    print(f"Xнач= {X_start:.2f} Xкон= {X_end:.2f}")
    print(f"Dx= {step:.2f} Eps= {epsilon:.5f}")

    # Генерировать и выводить таблицу
    generate_table(X_start, X_end, step, epsilon)
