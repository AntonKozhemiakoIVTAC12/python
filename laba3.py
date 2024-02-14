import random
import numpy
import math
import xlsxwriter

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds / 60

def conclusion():
    workbook = xlsxwriter.Workbook('lab3Table data.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Тип')
    worksheet.write('B1', 'Абонент')
    worksheet.write('C1', 'Длина')
    worksheet.write('D1', 'Время')
    row = 0
    # worksheet.write(i + 1, 0, mass_final[i][0])
    for i in range(100):
        worksheet.write(i + 1, 0, mass_final[i][0])
        worksheet.write(i + 1, 1, mass_final[i][1])
        worksheet.write(i + 1, 2, mass_final[i][2])
        worksheet.write(i + 1, 3, mass_final[i][3])
    worksheet.write('H1', 'Практика')
    worksheet.write('M1', 'Теория')

    worksheet.write(1, 5, 'Type 1')
    worksheet.write(2, 5, tp1) #количество
    worksheet.write(3, 5, type[0] * 0.01) #вероятность
    worksheet.write(4, 5, len_mass[0]) #средняя длинна
    worksheet.write(5, 5, len_max_mass[0]) #предельная длина
    worksheet.write(6, 5, tp1 * 0.27) #частота поступления это количество делить на время
    worksheet.write(8, 5, len_mass_abonent[0][0] * 0.01)#вероятности к абонентам
    worksheet.write(9, 5, len_mass_abonent[0][1] * 0.01)
    worksheet.write(10, 5, len_mass_abonent[0][2] * 0.01)
    worksheet.write(11, 5, len_mass_abonent[0][3] * 0.01)
    worksheet.write(12, 5, len_mass_abonent[0][4] * 0.01)


    worksheet.write(1, 6, 'Type 2')
    worksheet.write(2, 6, tp2)
    worksheet.write(3, 6, type[1] * 0.01)
    worksheet.write(4, 6, len_mass[1])
    worksheet.write(5, 6, len_max_mass[1])
    worksheet.write(6, 6, tp2 * 0.29)
    worksheet.write(8, 6, len_mass_abonent[1][0] * 0.01)
    worksheet.write(9, 6, len_mass_abonent[1][1] * 0.01)
    worksheet.write(10, 6, len_mass_abonent[1][2] * 0.01)
    worksheet.write(11, 6, len_mass_abonent[1][3] * 0.01)
    worksheet.write(12, 6, len_mass_abonent[1][4] * 0.01)

    worksheet.write(1, 7, 'Type 3')
    worksheet.write(2, 7, tp3)
    worksheet.write(3, 7, type[2] * 0.01)
    worksheet.write(4, 7, len_mass[2])
    worksheet.write(5, 7, len_max_mass[2])
    worksheet.write(6, 7, tp3 * 0.25)
    worksheet.write(8, 7, len_mass_abonent[2][0] * 0.01)
    worksheet.write(9, 7, len_mass_abonent[2][1] * 0.01)
    worksheet.write(10, 7, len_mass_abonent[2][2] * 0.01)
    worksheet.write(11, 7, len_mass_abonent[2][3] * 0.01)
    worksheet.write(12, 7, len_mass_abonent[2][4] * 0.01)



    worksheet.write(1, 10, 'Type 1')
    worksheet.write(2, 10, 5)
    worksheet.write(3, 10, 0.05)
    worksheet.write(4, 10, 12.2)
    worksheet.write(5, 10, 244)
    worksheet.write(6, 10, 0.83)
    worksheet.write(8, 10, 0.22)
    worksheet.write(9, 10, 0.26)
    worksheet.write(10, 10, 0.29)
    worksheet.write(11, 10, 0.03)
    worksheet.write(12, 10, 0.2)

    worksheet.write(1, 11, 'Type 2')
    worksheet.write(2, 11, 17)
    worksheet.write(3, 11, 0.17)
    worksheet.write(4, 11, 129)
    worksheet.write(5, 11, 244)
    worksheet.write(6, 11, 2.83)
    worksheet.write(8, 11, 0.21)
    worksheet.write(9, 11, 0.47)
    worksheet.write(10, 11, 0.05)
    worksheet.write(11, 11, 0.13)
    worksheet.write(12, 11, 0.14)

    worksheet.write(1, 12, 'Type 3')
    worksheet.write(2, 12, 78)
    worksheet.write(3, 12, 0.78)
    worksheet.write(4, 12, 190.32)
    worksheet.write(5, 12, 244)
    worksheet.write(6, 12, 13)
    worksheet.write(8, 12, 0.62)
    worksheet.write(9, 12, 0.13)
    worksheet.write(10, 12, 0.02)
    worksheet.write(11, 12, 0.19)
    worksheet.write(12, 12, 0.04)


    worksheet.write(2, 4, 'Количество')
    worksheet.write(3, 4, 'Вероятность')
    worksheet.write(4, 4, 'Средняя длина')
    worksheet.write(5, 4, 'Предельная длина')
    worksheet.write(6, 4, 'Частота поступления')
    worksheet.write(7, 4, 'Вероятность к')
    worksheet.write(8, 4, 'Абоненту 1')
    worksheet.write(9, 4, 'Абоненту 2')
    worksheet.write(10, 4, 'Абоненту 3')
    worksheet.write(11, 4, 'Абоненту 4')
    worksheet.write(12, 4, 'Абоненту 5')
    worksheet.write(15, 4, 'Мат ожидание')
    worksheet.write(16, 4, 'Дисперсия')
    worksheet.write(17, 4, 'Ср кв отклонение')
    worksheet.write(18, 4, 'Интенсивность')

    worksheet.write(14, 5, 'Тип')
    worksheet.write(15, 5, checkmate_waiting)
    worksheet.write(16, 5, disper_check)
    worksheet.write(17, 5, sr_kv_ot)



    worksheet.write(14, 6, 'Абонент')
    worksheet.write(15, 6, checkmate_waiting_abonent)
    worksheet.write(16, 6, disper_check_abonent)
    worksheet.write(17, 6, sr_kv_ot_abonent)


    worksheet.write(14, 7, 'Длина')
    worksheet.write(15, 7, checkmate_waiting_line)
    worksheet.write(16, 7, disper_check_line)
    worksheet.write(17, 7, sr_kv_ot_line)




    worksheet.write(14, 8, 'Время')
    worksheet.write(15, 8, mathWaiting)
    worksheet.write(16, 8, time(disper_check_time))
    worksheet.write(17, 8, time(sr_kv_ot_time))
    worksheet.write(18, 8, intensiv)









    worksheet.write(1, 15, 'Практика')
    worksheet.write(2, 15, 'Количество')
    worksheet.write(3, 15, 'Частота')
    worksheet.write(5, 15, 'Теория')
    worksheet.write(6, 15, 'Количество')
    worksheet.write(7, 15, 'Частота')

    worksheet.write(0, 16, 'Аб 1')
    worksheet.write(2, 16, abonent_q[0]) #количество
    worksheet.write(3, 16, abonent_q[0] * 0.08) #частота
    worksheet.write(6, 16, 48)
    worksheet.write(7, 16, 0.08 )

    worksheet.write(0, 17, 'Аб 2')
    worksheet.write(2, 17, abonent_q[1])
    worksheet.write(3, 17, abonent_q[1] * 0.08)
    worksheet.write(6, 17, 10.23)
    worksheet.write(7, 17, 0.017)

    worksheet.write(0, 18, 'Аб 3')
    worksheet.write(2, 18, abonent_q[2])
    worksheet.write(3, 18, abonent_q[2] * 0.08)
    worksheet.write(6, 18, 1.58)
    worksheet.write(7, 18, 0.02)

    worksheet.write(0, 19, 'Аб 4')
    worksheet.write(2, 19, abonent_q[3])
    worksheet.write(3, 19, abonent_q[3] * 0.08)
    worksheet.write(6, 19, 14.8)
    worksheet.write(7, 19, 0.024)

    worksheet.write(0, 20, 'Аб 5')
    worksheet.write(2, 20, abonent_q[4])
    worksheet.write(3, 20, abonent_q[4] * 0.08)
    worksheet.write(6, 20, 3.15)
    worksheet.write(7, 20, 0.005)

    worksheet.write(14, 10, 'Аб 1')
    worksheet.write(14, 11, 'Аб 2')
    worksheet.write(14, 12, 'Аб 3')
    worksheet.write(14, 13, 'Аб 4')
    worksheet.write(14, 14, 'Аб 5')
    worksheet.write(18, 10, 1 / time_to_seconds(mass_abonent_time[0]))
    if tp2 == 0:
        worksheet.write(18, 11, 0)
    else:
        worksheet.write(18, 11, 1 / time_to_seconds(mass_abonent_time[1]))

    worksheet.write(18, 12, 1 / time_to_seconds(mass_abonent_time[2]))
    worksheet.write(18, 13, 1 / time_to_seconds(mass_abonent_time[3]))
    worksheet.write(18, 14, 1 / mass_abonent_time[4])
    workbook.close()


def time(seconds):
    component_time = int(seconds // 60)
    minuts = int(component_time % 60)
    hours = int(component_time // 3600)
    seconds = int(seconds % 60)
    return f'{hours:02}:{minuts:02}:{seconds:02}'


mathWaiting = numpy.exp(0.9 + 1.6/2)

mathWaiting = time(mathWaiting)


mass_final = []


tp1 = 0
tp2 = 0
tp3 = 0
tp4 = 0
len1 = 0
len2 = 0
len3 = 0
len4 = 0
len1_mass = []
len2_mass = []
len3_mass = []
len4_mass = []
len_max_mass = [0, 0, 0, 0]
len_mass = [0, 0, 0, 0]
len_mass_abonent = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
abonent_q = [0, 0, 0, 0, 0]
mass_abonent_q = [0, 0, 0, 0, 0]
mass_abonent_time = [0, 0, 0, 0, 0]
time_mgc = [0, 0, 0, 0]
time_mgc_teory = [0, 0, 0, 0]
mid_len = [0, 0, 0, 0]
past_time = times = 0
past_time1 = times1 = 0
srt = time(4230)
mid_t = [0, 0, 0, 0]
type = [0, 0, 0, 0]
abonent = [0, 0, 0, 0, 0]
#генерация сообщений различного типа с заданными вероятностями и адресация сообщений
for i in range(100):
    n = random.random()
    random_abonent = random.random()
    mass = []
    len_m = 0
    total_time = time(times)
    total_time1 = time(times1)
    #tp1, tp2 и tp3 используются для подсчета количества разных типов сообщений:
    if n < 0.05: #Если n меньше 0,05, сообщение генерируется с вероятностью 0,05. Это соответствует первому условию в коде.
        mass.append(1) #В этом случае сообщения генерируются в цикле с вероятностью 0,05 для каждой итерации цикла и добавляются в список mass.
        # Переменная len_m отслеживает длину сообщения.
        len_m = 14
        for i in range(230):
            if random.random() > 0.05:
                len_m = random.randint(14, 244)

        if random_abonent < 0.22: #После генерации сообщения код переходит к их распределению по разным устройствам на основе значения random_abonent:
            mass.append(1) #Выбранное устройство добавляется в список mass.
        elif random_abonent < 0.48:
            mass.append(2)
        elif random_abonent < 0.77:
            mass.append(3)
        elif random_abonent < 0.8:
            mass.append(4)
        else:
            mass.append(5)
            # print("Hello")
        tp1 += 1 #Количество сообщений отправленных на каждое устройство, увеличивает количество сообщений типа 1 на 1 каждый раз, когда генерируется сообщение этого типа.
        len1 += len_m # общая длина сообщений
        len1_mass.append(len_m)




    elif n < 0.23: #Если n находится между 0,05 и 0,23, сообщение генерируется с вероятностью 0,18 (0,23 - 0,05).
        # Это соответствует второму условию в коде. Сообщения генерируются случайной длины от 14 до 244 символов и добавляются в список mass.
        len_m = random.randint(14, 244)
        mass.append(2)
        if random_abonent < 0.21:
            mass.append(1)
        elif random_abonent < 0.68:
            mass.append(2)
        elif random_abonent < 0.73:
            mass.append(3)
        elif random_abonent < 0.86:
            mass.append(4)
        else:
            mass.append(5)
        tp2 += 1
        len2 += len_m
        len2_mass.append(len_m)
    else:
        len_m = random.randint(14, 244)
        s = random.random()
        for i in range(244):
            if s >= 0.78:
                len_m = random.randint(14, 244)
        mass.append(3)
        if random_abonent < 0.62:
            mass.append(1)
        elif random_abonent < 0.75:
            mass.append(2)
        elif random_abonent < 0.77:
            mass.append(3)
        elif random_abonent < 0.96:
            mass.append(4)
        else:
            mass.append(5)
        tp3 += 1
        len3 += len_m
        len3_mass.append(len_m)


        #моделирование потока сообщений различного типа с заданными законом распредления вероятностей длин


    mass.append(len_m)
    mass_final.append(mass)
    mass.append(total_time)
    times += int(numpy.random.normal(6.0, math.sqrt(4.7))) #моделирования времени по нормальному распределению(средний промежуток времени и среднее кв. отклонение)
    times1 += int(numpy.random.normal(6.0, math.sqrt(4.7)))
    type[mass[0] - 1] += 1
    abonent[mass[1] - 1] += 1 #увеличивает счетчик абонента, которому было отправлено сообщение, в соответствующем элементе списка abonent
    abonent_q[mass[1] - 1] += 1 #abonent_q отслеживает количество сообщений, отправленных каждому абоненту (Абоненту 1,
    # Абоненту 2, Абоненту 3, Абоненту 4, Абоненту 5). Например, abonent_q[mass[1] - 1] += 1 увеличивает количество сообщений,
    len_mass_abonent[mass[0] - 1][mass[1] - 1] += 1
    mass_abonent_time[mass[1] - 1] += times1
    past_time1 = times1 - past_time1
    time_mgc[mass[0] - 1] += times
    past_time = times - past_time



mass_abonent_time[0] = mass_abonent_time[0] / abonent_q[0] #Расчет Среднего Времени для Каждого Абонента
# Каждый элемент массива mass_abonent_time делится на соответствующий элемент массива abonent_q, что,
# является количеством сообщений для каждого абонента. Это дает среднее время, потраченное на каждого абонента.
if tp2 == 0:
    mass_abonent_time[1] = 0
else:
    mass_abonent_time[1] = mass_abonent_time[1] / abonent_q[1]
mass_abonent_time[2] = mass_abonent_time[2] / abonent_q[2]
mass_abonent_time[3] = mass_abonent_time[3] / abonent_q[3]
mass_abonent_time[4] = mass_abonent_time[4] / abonent_q[4]

# masss = [0, 0, 0, 0, 0]
# masss[0] = 1 / mass_abonent_time[0]
# masss[1] = 1 / mass_abonent_time[1]
# masss[2] = 1 / mass_abonent_time[2]
# masss[3] = 1 / mass_abonent_time[3]
# masss[4] = 1 / mass_abonent_time[4]
# print(masss[0])
# print(masss[1])
# print(masss[2])
# print(masss[3])
# print(masss[4])
# abonent_q.append(masss[0])
# abonent_q.append(masss[0])
# abonent_q.append(masss[0])
# abonent_q.append(masss[0])


time_mgc[0] = time_mgc[0] / tp1 #Расчет Среднего Времени для Каждого Типа каждый элемент массива time_mgc делится на количество сообщений каждого типа (tp1, tp2, tp3).
# Это дает среднее время, потраченное на каждый тип сообщения.
if tp2 == 0:
    time_mgc[1] = 0
else:
    time_mgc[1] = time_mgc[1] / tp2
time_mgc[2] = time_mgc[2] / tp3
len_mass[0] = len1 / tp1
if tp2 == 0:
    len_mass[1] = 0 #Расчет Средней Длины Сообщения
    # Вычисляется средняя длина сообщений для каждого типа, делением общей длины сообщений каждого типа на количество сообщений этого типа
else:
    len_mass[1] = len2 / tp2
len_mass[2] = len3 / tp3
for i in range(len(len1_mass)): #Определение Максимальной Длины Сообщения для Каждого Типа Проходит по массивам
    # len1_mass, len2_mass, len3_mass, содержащим длины сообщений каждого типа, и определяет максимальную длину сообщения для каждого типа.
    if len_max_mass[0] < len1_mass[i]:
        len_max_mass[0] = len1_mass[i]
for i in range(len(len2_mass)):
    if len_max_mass[1] < len2_mass[i]:
        len_max_mass[1] = len2_mass[i]
for i in range(len(len3_mass)):
    if len_max_mass[2] < len3_mass[i]:
        len_max_mass[2] = len3_mass[i]

mid_len[0] = len_mass[0] / tp1 #Расчет Средней Длины для Каждого Типа
# Вычисляется средняя длина сообщений для каждого типа, делением общей длины на количество сообщений каждого типа.
if tp2 == 0:
    mid_len[1] = 0
else:
    mid_len[1] = len_mass[1] / tp2
    mid_len[2] = len_mass[1] / tp2

    mid_t[0] = tp1 * 0.05 #Расчет Среднего Времени для Каждого Типа
    # Вычисляется среднее время для каждого типа сообщения, умножением количества сообщений каждого типа на вероятность появления этого типа сообщения
    mid_t[1] = tp2 * 0.17
    mid_t[2] = tp3 * 0.78




    mass_time_math = [0, 0, 0, 0]
    mass_time_math[0] = time_mgc[0]
    mass_time_math[1] = time_mgc[1]
    mass_time_math[2] = time_mgc[2]


    time_mgc[0] = time(time_mgc[0]) #Используется функция time, которая, по всей видимости, преобразует время в формат часов,
    # минут и секунд для массивов time_mgc и mass_abonent_time
    time_mgc[1] = time(time_mgc[1])
    time_mgc[2] = time(time_mgc[2])




    mass_abonent_time[0] = time(mass_abonent_time[0])
    mass_abonent_time[1] = time(mass_abonent_time[1])
    mass_abonent_time[2] = time(mass_abonent_time[2])
    mass_abonent_time[3] = time(mass_abonent_time[3])

# Математическое ожидание!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    checkmate_waiting = tp1 * 0.05 * 0.01 + tp2 * 0.17 * 0.01 + tp3 * 0.78 * 0.01
    checkmate_waiting_abonent = abonent_q[0] * 0.01 * 0.53 + abonent_q[1] * 0.01 * 0.2 + abonent_q[2] * 0.01 * 0.03 + abonent_q[3] * 0.01 * 0.17 + abonent_q[4] * 0.01 * 0.06

    checkmate_waiting_line = (len1 * 0.05 + len2 * 0.17 + len3 * 0.78) * 0.01
    print(len_mass)
    print(checkmate_waiting, "\t\t", checkmate_waiting_abonent, "\t\t", checkmate_waiting_line, "\t\t", mathWaiting)



# Дисперсии
    disper_check = ((tp1 - mid_t[0])**2 + (tp2 - mid_t[1])**2 + (tp3 - mid_t[2])**2) / 100
    disper_check_abonent = ((abonent_q[0] - checkmate_waiting_abonent)**2 + (abonent_q[1] - checkmate_waiting_abonent)**2 + (abonent_q[2] - checkmate_waiting_abonent)**2) / 100
    disper_check_line = ((len_mass[0] - mid_len[0])**2 + (len_mass[1] - mid_len[1])**2 + (len_mass[2] - mid_len[2])**2)/3

    matic = numpy.exp(0.9 + 1.6/2)
    disper_check_time = (numpy.exp(0.9) - 1) * numpy.exp(2 * matic + 0.9)
    print(disper_check, "\t\t", disper_check_abonent, "\t\t", disper_check_line, "\t\t", time(disper_check_time))

# Ср квадратич
    sr_kv_ot = math.sqrt(disper_check)
    sr_kv_ot_abonent = math.sqrt(disper_check_abonent)
    sr_kv_ot_line = math.sqrt(disper_check_line)
    sr_kv_ot_time = math.sqrt(disper_check_time)

    print(sr_kv_ot, "\t\t", sr_kv_ot_abonent, "\t\t", sr_kv_ot_line, "\t\t", time(sr_kv_ot_time))
# интенсивность
    s = times/100 #интенсивность времени поступления сообщений 1 делить на моделируемое время
    intensiv = 1/s
    print(time(intensiv))

    conclusion()