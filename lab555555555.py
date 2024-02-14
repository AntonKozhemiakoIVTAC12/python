import random  as rd

matrix = [[1, 0.8, 1, 0.9, 0.9], [0.8, 1, 0.6, 0.9, 0.7], [0.8, 0.7, 0.7, 0.9, 0.8],
          [0.9, 0.6, 0.5, 1, 1],[0.8, 0.9, 0.7, 0.9, 1]]
priority = [[0.1,0.5,0.1,1,1], [0.1, 1, 0.1, 0.1, 0.1],
            [rd.random(), rd.random(), rd.random(), rd.random(), rd.random()]]
alt = 5
crit = 5


def calc_matrix(n):
    for i in range(alt):
        for j in range(crit):
            matrix[i][j] *= priority[n - 1][j]


def print_res(name, f):
    print('\n' + name + ':')
    for i in range(alt):
        print(f'{i + 1} альтернатива: {f[i]}')
    print(f'Оптимальный выбор: {f.index(max(f)) + 1}')


def crit_lplsa():
    f = []
    for i in range(alt):
        f.append(sum(matrix[i]) / 5)
    print_res('Критерий Лапласа', f)


def crit_valda():
    f = []
    for i in range(alt):
        f.append(min(matrix[i]))
    print_res('Критерий Вальда', f)


def crit_savja():
    f = []
    r = []
    for i in range(alt):
        r.append([])
        for j in range(crit):
            mx = max(matrix[i])
            r[i].append(mx - matrix[i][j]) if matrix[i][j] != mx else None
    for i in range(alt):
        f.append(min(r[i]))
    print_res('Критерий Сэвиджа', f)


def crit_gurvica(a):
    f = []
    for i in range(alt):
        f.append(max(matrix[i]) * a + min(matrix[i]) * (1 - a))
    print_res('Критерий Гурвица (' + str(a) + ')', f)


exp = int(input('Номер эксперимента (1, 2 или 3): '))
calc_matrix(exp)

crit_lplsa()
crit_valda()
crit_savja()
crit_gurvica(0)
crit_gurvica(0.5)
crit_gurvica(1)
