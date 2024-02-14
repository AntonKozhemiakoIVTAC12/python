import numpy as np
import math
from operator import itemgetter
from datetime import datetime
import openpyxl
import pandas as pd
import xlsxwriter
from openpyxl import load_workbook
from sympy.physics.units import wb


def str_time(sec):
    hours = int(sec // 3600)
    minutes = int((sec % 3600) // 60)
    seconds = int(sec % 60)
    milliseconds = int((sec % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"


v = 50
# Разработанный алгоритм эмуляции канала сообщений применяет относительный принцип, где обслуживание текущей заявки
# завершается перед началом обслуживания новой заявки, даже если новая заявка обладает более высоким приоритетом.


def non_prior_channel(v, message):
    arr = [] #Создается двумерный массив arr размером, соответствующим количеству сообщений. Каждый элемент массива инициализируется значением None
    for i in range(len(message)):
        row = []
        for j in range(7):
            row.append(None)
        arr.append(row)
# Устанавливаются начальные значения для первого сообщения в массиве arr:
    arr[0][0] = 1#Номер шага (arr[0][0]) устанавливается в 1.
    arr[0][1] = message[0][3] #устанавливается равным времени поступления первого сообщения.
    arr[0][2] = message[0][3] #Время начала обслуживания (arr[0][2]) устанавливается равным времени поступления первого сообщения.
    arr[0][3] = arr[0][2] + message[0][2] / v #вычисляется как время начала обслуживания плюс продолжительность обслуживания первого сообщения, деленная на параметр v.
    arr[0][4] = 0 #Время ожидания (arr[0][4]) устанавливается в 0
    arr[0][5] = round(arr[0][3] - arr[0][1], 4) #Время ответа (arr[0][5]) вычисляется как разница между временем завершения обслуживания и временем поступления первого сообщения
    arr[0][6] = message[0][0] #Идентификатор сообщения (arr[0][6]) устанавливается в идентификатор первого сообщения.
#Итерация по остальным сообщениям: Происходит итерация по оставшимся сообщениям:
    for i in range(len(message) - 1):
        arr[i+1][0] = i+2 #На каждом шаге обновляются значения массива arr в соответствии с логикой канала без приоритета.
        arr[i+1][1] = round(message[i + 1][3], 2) #В частности, вычисляются времена поступления, начала и завершения обслуживания, времена ожидания и ответа для каждого сообщения.
        if (arr[i+1][1] > arr[i][3]):

            arr[i+1][2] = arr[i+1][1]
        else:
            arr[i+1][2] = arr[i][3]
        arr[i+1][3] = round(arr[i+1][2] + message[i+1][2] / v, 4)
        arr[i+1][4] = round(arr[i+1][2] - arr[i+1][1], 4)
        arr[i+1][5] = round(arr[i+1][3] - arr[i+1][1], 4)
        arr[i+1][6] = message[i+1][0] + 1
    arr[0][6] = message[0][0] + 1
    return arr #Функция возвращает массив arr, содержащий результаты моделирования для каждого шага.


def prior_channel(v, message):
    arr = []
    for i in range(len(message)):
        row = []
        for j in range(7):
            row.append(None)
        arr.append(row)

    arr[0][0] = 1
    arr[0][1] = message[0][3]
    arr[0][2] = message[0][3]
    arr[0][3] = arr[0][2] + message[0][2] / v
    arr[0][4] = 0
    arr[0][5] = round(arr[0][3] - arr[0][1], 4)
    arr[0][6] = message[0][0]

    for i in range(len(message) - 1):#Если текущее сообщение имеет меньшее время поступления по сравнению с временем завершения обслуживания предыдущего сообщения, производится коррекция порядка сообщений в соответствии с их приоритетами.
#Ищется подпоследовательность сообщений с более низким приоритетом, и сообщение с минимальным приоритетом перемещается на позицию перед текущим сообщением.
#Обновляются значения массива arr в соответствии с логикой канала с приоритетом.
        arr[i+1][0] = i+2
        if (arr[i][3] > message[i+1][3]):
            ar = []
            j = i + 1
            while (arr[i][3] > message[j][3]):
                ar.append(message[j][0])
                j += 1
                if (j > len(message) - 1):
                    break
            minimum = ar[0]
            index = 0
            for k in range(1, len(ar)):
                if ar[k] < minimum:
                    minimum = ar[k]
                    index = k
            row = message.pop(i + 1 + index)
            message.insert(i + 1, row)
            arr[i+1][1] = round(message[i+1][3], 2)
            arr[i+1][2] = arr[i][3]
        else:
            arr[i+1][1] = round(message[i+1][3], 2)
            arr[i+1][2] = arr[i+1][1]
        arr[i+1][3] = round(arr[i+1][2] + message[i+1][2] / v, 4)
        arr[i+1][4] = round(arr[i+1][2] - arr[i+1][1], 4)
        arr[i+1][5] = round(arr[i+1][3] - arr[i+1][1], 4)
        arr[i+1][6] = message[i+1][0] + 1
    arr[0][6] = message[0][0] + 1
    return arr


probabilities_table = np.array([
    [0.22, 0.26, 0.29, 0.03, 0.2],
    [0.21, 0.47, 0.05, 0.13, 0.14],
    [0.62, 0.13, 0.02, 0.19, 0.04]
])

generated_messages = []
message_counts = [0, 0, 0]  # Для подсчета количества сообщений каждого типа

abonent_counts = [0, 0, 0, 0, 0]
abonent_probabilities = [0, 0, 0, 0, 0]
abonent_type_counts = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
total_message_length = 0
max_message_length = 0
total_time_intervals = 0
current_time = 0

for _ in range(100):
    message_type = np.random.choice(3, p=[0.05, 0.17, 0.78])
    abonent = np.random.choice(5, p=probabilities_table[message_type])
    abonent_type_counts[message_type][abonent] += 1

    if message_type % 2 == 1:
        message_length = np.random.choice(range(231), p=[1 / 231] * 231)
    else:
        message_length = np.random.randint(14, 245)



    time_intervals = round(np.random.normal(6.0, math.sqrt(4.7)))
    current_time += time_intervals

    generated_messages.append((message_type, abonent, message_length, current_time))

    message_counts[message_type] += 1
    abonent_counts[abonent] += 1
    abonent_type_counts[message_type][abonent] += 1

    if message_length > max_message_length:
        max_message_length = message_length

generated_messages = [(message_type, abonent + 1, message_length, current_time) for
                      message_type, abonent, message_length, current_time in
                      generated_messages]

m = non_prior_channel(v,generated_messages) #вызовы функций
m2 = prior_channel(v,generated_messages)

total_messages = len(generated_messages)
message_type_probabilities = [message_count / total_messages for message_count in message_counts]  # вероятность каждого типа

abonent_type_probabilities = []
for message_type in range(3):
    message_type_counts = abonent_type_counts[message_type]  # количество сообщений данного типа для каждого типа абонента
    total_messages = sum(message_type_counts)
    if total_messages > 0:
        message_type_probability = [count / total_messages for count in message_type_counts]   # вероятность каждого типа сообщения
    abonent_type_probabilities.append(message_type_probability)

# Вывод таблицы с данными
total_message_types = len(message_counts)
total_abonent = len(abonent_counts)
frequency_message_type = [0] * total_message_types
frequency_abonent_type = [0] * total_abonent
total_length = 0
max_length = 0

print()


print("\nХарактеристики без приоритетного потока заявок:")
sum_time = [0, 0, 0]
serv_time = [0, 0, 0]
ap_time = [0, 0, 0]
time_in_sys = [0, 0, 0]

k = [0, 0, 0]

#time_in_sys = 0

for i in range(100):
   # time_in_sys += m[i][5]
    serv_time[m[i][6] - 1] += m[i][3] - m[i][2] #время обслуживания
    sum_time[m[i][6] - 1] += m[i][4] #время ожидания
    time_in_sys[m[i][6] - 1] += m[i][5] #время пребывания в канале
    ap_time[m[i][6] - 1] = m[i][1] #время  появления
    k[m[i][6] - 1] += 1 # тип сообщения

v_i = [round(serv_time[i] / k[i], 4) for i in range(3)] #Среднее время обслуживания заявки

D_i = [round(sum((m2[i][3] - m2[i][2] - v_i[m2[i][6] - 1]) ** 2 for i in range(100)) / k[j], 4) for j in range(3)] #дисперсия времени обслуживания
sigma_i = [round(math.sqrt(D_i[i]), 4) for i in range(3)] # Среднеквадратичное отклонение времени обслуживания заявки

mu_i = [round(1 / v_i[i], 4) for i in range(3)] #Интенсивность обслуживания заявки
lambda_i = [round(k[i] / ap_time[i], 4) for i in range(3)] #среднее число заявок, поступающих на обслуживание или интенсивность поступления заявок i-го типа
rho_i = [round(lambda_i[i] / mu_i[i], 4) for i in range(3)] # коэффициент загрузки оборудования заявками i-го типа
n_i = [round(1 - rho_i[i], 4) for i in range(3)] #Коэффициент простоя

R = round(sum(rho_i), 4) #Коэффициент загрузки:
Lambda = round(sum(lambda_i), 4) #Интенсивность поступления заявок:
# tau_i1 = [round(ap_time[i] / k[i], 4) for i in range(3)]
# lambda_i1 = [round(1 / tau_i1[i], 4) for i in range(3)]
tau_i = [round(1 / lambda_i[i], 4) for i in range(3)] #Средний промежуток времени между поступлением заявок
p_i = [round(lambda_i[i] / Lambda, 4) for i in range(3)] #Вероятность поступления заявки
w_i = [round(sum_time[i] / k[i], 4) for i in range(3)] #среднее время пребывания заявки i-го типа в очереди
W = round(sum([p_i[i] * w_i[i] for i in range(3)]), 4) #среднее время пребывания заявки в очереди
l_i = [round(w_i[i] * lambda_i[i], 4) for i in range(3)] #средняя длина очереди заявок i-го типа
u_i = [round(time_in_sys[i] / k[i], 4) for i in range(3)] #среднее время пребывания заявки в системе
U = round(sum([p_i[i] * u_i[i] for i in range(3)]), 4) #среднее время пребывания заявки в системе;
L = round(sum([lambda_i[i] * u_i[i] for i in range(3)]), 4) #среднее число заявок в системе

print('\nv_i')
for i in range(3):
    print(f"Среднее время обслуживания заявки {i+1} типа: {v_i[i]}")

print('\nD_i')
for i in range(3):
    print(f"Дисперсия времени обслуживания {i + 1} типа: {D_i[i]}")

print('\nsigma_i')
for i in range(3):
    print(f"Среднеквадратичное отклонение времени обслуживания заявки {i + 1} типа: {sigma_i[i]}")

print('\nmu_i')
for i in range(3):
    print(f"Интенсивность обслуживания заявки {i+1} типа: {mu_i[i]}")

print('\nλ_i')
for i in range(3):
    print(f"Среднее число заявок, поступающих на обслуживание {i+1} типа: {lambda_i[i]}")

print('\nrho_i')
for i in range(3):
    print(f"Коэффициент загрузки оборудования заявками {i+1} типа: {rho_i[i]}")

print('\nn_i')
for i in range(3):
    print(f"Коэффициент простоя {i+1} типа: {n_i[i]}")

print('\nR')
print(f"Коэффициент загрузки: {R}")

print('\nΛ')
print(f"Интенсивность поступления заявок: {Lambda}")

print('\ntau_i')
for i in range(3):
    print(f"Средний промежуток времени между поступлением заявок {i+1} типа: {tau_i[i]}")

print('\np_i')
for i in range(3):
    print(f"Вероятность поступления заявки {i+1} типа: {p_i[i]}")

print('\nw_i')
for i in range(3):
    print(f"Среднее время пребывания заявки {i+1} типа в очереди: {w_i[i]}")

print('\nl_i')
for i in range(3):
    print(f"Средняя длина очереди заявок  {i+1} типа: {l_i[i]}")

print('\nW')
print(f"Среднее время пребывания заявки в очереди: {W}")

print('\nu_i')
for i in range(3):
    print(f"Среднее время пребывания заявки {i+1} типа в системе: {u_i[i]}")

print('\nU')
print(f"Среднее время пребывания заявки в системе: {U}")

print('\nL')
print(f"Среднее число заявок в системе: {L}")


print("\nХарактеристики приоритетного потока заявок:")

sum_time = [0, 0, 0]
serv_time = [0, 0, 0]
ap_time = [0, 0, 0]
time_in_sys = [0, 0, 0]

k = [0, 0, 0]

#time_in_sys = 0

for i in range(100):
   # time_in_sys += m[i][5]
    serv_time[m2[i][6] - 1] += m2[i][3] - m2[i][2]
    sum_time[m2[i][6] - 1] += m2[i][4]
    time_in_sys[m2[i][6] - 1] += m2[i][5]
    ap_time[m2[i][6] - 1] = m2[i][1]
    k[m2[i][6] - 1] += 1

v_i = [round(serv_time[i] / k[i], 4) for i in range(3)]

D_i = [round(sum((m2[i][3] - m2[i][2] - v_i[m2[i][6] - 1]) ** 2 for i in range(100)) / k[j], 4) for j in range(3)]
sigma_i = [round(math.sqrt(D_i[i]), 4) for i in range(3)]

mu_i = [round(1 / v_i[i], 4) for i in range(3)]
lambda_i = [round(k[i] / ap_time[i], 4) for i in range(3)]
rho_i = [round(lambda_i[i] / mu_i[i], 4) for i in range(3)]
n_i = [round(1 - rho_i[i], 4) for i in range(3)]

R = round(sum(rho_i), 4)
Lambda = round(sum(lambda_i), 4)

tau_i = [round(1 / lambda_i[i], 4) for i in range(3)]
p_i = [round(lambda_i[i] / Lambda, 4) for i in range(3)]
w_i = [round(sum_time[i] / k[i], 4) for i in range(3)]
W = round(sum([p_i[i] * w_i[i] for i in range(3)]), 4)
l_i = [round(w_i[i] * lambda_i[i], 4) for i in range(3)]
u_i = [round(time_in_sys[i] / k[i], 4) for i in range(3)]
U = round(sum([p_i[i] * u_i[i] for i in range(3)]), 4)
L = round(sum([lambda_i[i] * u_i[i] for i in range(3)]), 4)

print('\nv_i')
for i in range(3):
    print(f"Среднее время обслуживания заявки {i + 1} типа: {v_i[i]}")

print('\nD_i')
for i in range(3):
    print(f"Среднее время обслуживания заявки {i + 1} типа: {D_i[i]}")

print('\nsigma_i')
for i in range(3):
    print(f"Среднеквадратичное отклонение времени обслуживания заявки {i + 1} типа: {sigma_i[i]}")

print('\nmu_i')
for i in range(3):
    print(f"Интенсивность обслуживания заявки {i + 1} типа: {mu_i[i]}")

print('\nλ_i')
for i in range(3):
    print(f"Среднее число заявок, поступающих на обслуживание {i + 1} типа: {lambda_i[i]}")

print('\nrho_i')
for i in range(3):
    print(f"Коэффициент загрузки оборудования заявками {i + 1} типа: {rho_i[i]}")

print('\nn_i')
for i in range(3):
    print(f"Коэффициент простоя {i + 1} типа: {n_i[i]}")

print('\nR')
print(f"Коэффициент загрузки: {R}")

print('\nΛ')
print(f"Интенсивность поступления заявок: {Lambda}")

print('\ntau_i')
for i in range(3):
    print(f"Средний промежуток времени между поступлением заявок {i + 1} типа: {tau_i[i]}")


print('\np_i')
for i in range(3):
    print(f"Вероятность поступления заявки {i + 1} типа: {p_i[i]}")

print('\nw_i')
for i in range(3):
    print(f"Среднее время пребывания заявки {i + 1} типа в очереди: {w_i[i]}")

print('\nl_i')
for i in range(3):
    print(f"Средняя длина очереди заявок  {i+1} типа: {l_i[i]}")

print('\nW')
print(f"Среднее время пребывания заявки в очереди: {W}")

print('\nu_i')
for i in range(3):
    print(f"Среднее время пребывания заявки {i + 1} типа в системе: {u_i[i]}")

print('\nU')
print(f"Среднее время пребывания заявки в системе: {U}")

print('\nL')
print(f"Среднее число заявок в системе: {L}")

all_processed_messages = []
all_prior_messages = []

processed_messages = m
prior_messages = m2
all_processed_messages.extend(processed_messages)
all_prior_messages.extend(prior_messages)

df_processed_messages = pd.DataFrame(all_processed_messages, columns=[
    "Номер заявки", "Момент появления в канале",
    "Момент начала обслуживания", "Момент конца обслуживания", "Время ожидания", "Время пребывания в канале",
    "Тип сообщения"
])

df_processed_messages["Момент появления в канале"] = df_processed_messages["Момент появления в канале"].apply(str_time)
df_processed_messages["Момент начала обслуживания"] = df_processed_messages["Момент начала обслуживания"].apply(
    str_time)
df_processed_messages["Момент конца обслуживания"] = df_processed_messages["Момент конца обслуживания"].apply(str_time)
df_processed_messages["Время ожидания"] = df_processed_messages["Время ожидания"].apply(str_time)
df_processed_messages["Время пребывания в канале"] = df_processed_messages["Время пребывания в канале"].apply(str_time)


df_prior_messages = pd.DataFrame(all_prior_messages, columns=[
    "Номер заявки", "Момент появления в канале",
    "Момент начала обслуживания", "Момент конца обслуживания", "Время ожидания", "Время пребывания в канале",
    "Тип сообщения"
])

# Преобразование времени в строковый формат
df_prior_messages["Момент появления в канале"] = df_prior_messages["Момент появления в канале"].apply(str_time)
df_prior_messages["Момент начала обслуживания"] = df_prior_messages["Момент начала обслуживания"].apply(str_time)
df_prior_messages["Момент конца обслуживания"] = df_prior_messages["Момент конца обслуживания"].apply(str_time)
df_prior_messages["Время ожидания"] = df_prior_messages["Время ожидания"].apply(str_time)
df_prior_messages["Время пребывания в канале"] = df_prior_messages["Время пребывания в канале"].apply(str_time)

# Запись в Excel
excel_filename = "lab4.xlsx"

with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
    df_processed_messages.to_excel(writer, sheet_name='processed_messages', index=False)
    df_prior_messages.to_excel(writer, sheet_name='prior_messages', index=False)
