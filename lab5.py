import sympy as sp


def lgr(inx_):
    ml = ''
    print('\nL(x) = ', end='')
    for i in range(5):
        sl = ''
        expr = f'yi/('
        for j in range(5):
            if i == j:
                continue
            expr += f'(xi - {X[j]})*'

        a = sp.sympify(expr[:-1] + ')').subs({xi: X[i], yi: Y[i]}) # с помощью sp.sympify вычисляется значение этого выражения, где "xi" и "yi" заменяются на соответствующие значения из массивов X и Y для текущей точки i. Результат записывается в переменную a
        if a > 0:
            sl += '+'
        sl += f'{a:.4f}'
        for j in range(5):
            if i == j:
                continue
            sl += f' * (x - {X[j]})'

        print(sl)
        ml += sl

    print(f'\nL({inx_}) =', f'{sp.sympify(ml).subs(x, inx_):.4f}')
    sp.plot(sp.sympify(ml), (x, 0, 3))


def ntn(inx_):
    fx = [1.082,	1.654462243,	1.579813917,	-1.817785202,	1.112946042] #таблица разделенных разностей
    mn = ''
    print('\nN(x) = ', end='')
    for i in range(5):
        f = fx[i]
        if f > 0:
            expr = f'+{f:.4f}'
        else:
            expr = f'{f:.4f}'
        for j in range(i):
            expr += f' * (x - {X[j]})'
        print(expr)
        mn += expr

    print(f'\nN({inx_}) =', f'{sp.sympify(mn).subs(x, inx_):.4f}')
    sp.plot(sp.sympify(mn), (x, 0, 3))


def lns():
    a, b = sp.symbols("a, b")
    am = []
    bm = []

    print('Коэфиценты:')
    for i in range(4):
        c = sp.linsolve([sp.Eq(X[i] * a + b, Y[i]), sp.Eq(X[i + 1] * a + b, Y[i + 1])], (a, b)) #Решается система линейных уравнений с помощью библиотечной функции
        c = str(c).replace('(', '').replace(')', '').replace('{', '').replace('}', '').replace(',', '').split()
        print(f'a{i + 1} = {float(c[0]):.3f}\tb{i + 1} = {float(c[1]):.3f}')
        am.append(float(c[0]))
        bm.append(float(c[1]))

    print('\nСистема уравнений линейного сплайна:')
    plt = []
    for i in range(4):
        if bm[i] < 0:
            pl = f'{am[i]:.3f} * x - {abs(bm[i]):.3f}'
            print(f'{pl},   {X[i]} <= x <= {X[i + 1]}')
        else:
            pl = f'{am[i]:.3f} * x + {bm[i]:.3f}'
            print(f'{pl},   {X[i]} <= x <= {X[i + 1]}')
        plt.append((sp.sympify(pl), (x, X[i], X[i + 1])))

    sp.plot(plt[0], plt[1], plt[2], plt[3])


X = [0.235,	0.672,	1.385,	2.051,	2.908]
Y = [1.082,	1.805,	4.280,	5.011,	7.082]
x, yi, xi = sp.symbols("x, yi, xi")

print('Выберите функцию:\n1) многочлен Лагранжа\n2) многочлен Ньютона\n3) линейный сплайн')
ch = int(input())
if ch == 1:
    inx = input('Введите произвольную точку x0: ')
    lgr(inx)
if ch == 2:
    inx = input('Введите произвольную точку x0: ')
    ntn(inx)
if ch == 3:
    lns()