from random import randint
def preobrazList(list): #создание функции для нахождения максимальной последовательности
    a = 1
    k = ka = 1
    for i in range(len(list)):
        if list[i] == list[i - 1]:
            k += 1  # счетчик элементов
        else:
            if k > ka:
                ka = k
                a = i
            k = 1
    return a - ka, a

list1 = []
for i in range(7):
    list1.append(randint(1,10))

list2 = []
for i in range(7):
    list2.append(randint(1,10))



print(list1)
print(list2)
print("\n")
l1, r1 = preobrazList(list1) #использование созданной функции для переменных первого и второго списков
l2, r2 = preobrazList(list2)
print(list1[:l1] + list2[l2:r2] + list1[r1:]) #вывод с заменой элементов списков
print(list2[:l2] + list1[l1:r1] + list2[r2:])
