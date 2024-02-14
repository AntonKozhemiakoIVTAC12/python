import csv
import os.path
import os

lst = os.listdir("D://papka") # your directory path
number_files = len(lst)
print (number_files)
print("\n")

def print_date(dict): #функция на вывод таблицы
    for a,b in dict.items():
        print(
            f"Id{a}: номер = {b['number']}, дата = {b['date']},ФИО студента = {b['fio']} стипендия = {b['stip']}, куда выдается справка = {b['kuda']}")

def parse_csv(file):  # функция парсинга файла
     got_data = {}
     with open(file, "r", encoding='utf-8') as raw_csv:
         for line in raw_csv:
             (idx, number, date, fio, stip, kuda) = line.replace("\n", "").split(",")
             got_data.update({int(idx): {"number": int(number), "date": date, "fio": fio, "stip": stip, "kuda": kuda}})
     return got_data

def sort_by_fio(c) -> dict:  # функция сортировки по месту выдачи справки
    return dict(sorted(c.items(), key=lambda f: f[1]["fio"]))

def sort_by_number(c) -> dict:  # функция сортировки по номеру
    return dict(sorted(c.items(), key=lambda f: f[1]["number"]))

def sort_by_values(c,value)->dict: #функция сортировки по номеру больше какого-либо значения
    return dict((a, b) for a, b in c.items() if b["number"] > value)

data = parse_csv('D:\\papka\\data.csv.txt') #путь до файла

print_date(data)#вывод таблицы
print("\n")

print_date(sort_by_fio(data)) #сортировка по фамилии
print("\n")

print_date(sort_by_number(data)) #сортировка по номеру
print("\n")

print_date(sort_by_values(data, 22)) #сортировка по значению номера больше 22

def add(file,c,number,date,fio,stip,kuda): #функция сохраненеия
    with open(file, "w",encoding='utf-8') as f:
        for a,b in c.items():
            f.write(f"{a},{b['number']},{b['date']},{b['fio']},{b['stip']}.{b['kuda']}\n")
        f.write(f"{len(c) + 1},{number},{date},{fio},{stip},{kuda}\n")
    с.update({len(c) + 1: {"number": number, "date": date,"fio":fio, "stip": stip, "kuda": kuda}})
#add('D:\\papka\\data.csv.txt', 5, 555, '31.01.2023', 'Данила Давыдов', 5000, 'в горы') #сохранение новых данных в файл