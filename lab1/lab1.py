def preobrazList(list): #создание функции для нахождения максимальной последовательности
    a = 1
    k = ka = 1
    for i in range(len(list)):
        if list[i] == list[i - 1]:
            k += 1 #счетчик элементов
        else:
            if k > ka:
                ka = k//обновляем максимальное
                a = i//приравниваем а к правой границе списка
            k = 1// сбрасываем k
    return a - ka, a// лвозвращается левая и правая граница


list1 = [int(i) for i in input().split()] #создание списка(массива) с использованием функции split для разделения строки на список строк на основе разделителя с типом данных integer
list2 = [int(i) for i in input().split()]
l1, r1 = preobrazList(list1) #использование созданной функции для переменных первого и второго списков
l2, r2 = preobrazList(list2)
print(list1[:l1] + list2[l2:r2] + list1[r1:]) #вывод с заменой элементов списков
print(list2[:l2] + list1[l1:r1] + list2[r2:])