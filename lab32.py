from random import uniform

# Функция, определяющая попадание точки в заданную область
def check_hit(x, y, R):
    if x <= 0 and x**2 + y**2 <= R**2 and y <= 0:
        return True
    elif y >= (x-1)**2 and x >= 0:
        return True
    else:
        return False

# Вывод шапки
print("Результат тестирования программы")
print("X\t    Y\t    Res")
print("-------------------")

# Цикл для десяти выстрелов
for _ in range(10):
    # Генерация координат точки
    x = uniform(-1, 4)
    y = uniform(-1, 10)

    # Проверка попадания
    result = "Yes" if check_hit(x, y, 2) else "No"

    # Вывод результатов
    print(f"{x:.2f}\t{y:.2f}\t{result}")