import os
lst = os.listdir("D://papka") # your directory path
number_files = len(lst)
print("\n")
print (number_files)
print("файлов в папке")
print("\n")

class row():
    idx = 0

    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val

class model(row):
    idx = 0
    number = 0
    date = ""
    fio = ""
    stip = ""
    kuda = ""

    def __init__(self, idx: int, number: int, date: str, fio: str, stip: int, kuda: str):
        super().__init__(idx)
        self.idx = idx
        self.number = number
        self.date = date
        self.fio = fio
        self.stip = stip
        self.kuda = kuda

    def __str__(self):
        return f"Запись №{self.idx}: номер = {self.number}, дата = {self.date}, ФИО студента = {self.fio}, размер стипендия = {self.stip}, куда выдается справка = {self.kuda}"

    def __repr__(self):
        return f"model(idx={self.idx},number={self.number},date={self.date},fio={self.fio},stip={self.stip},kuda={self.kuda})"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value
class Data():
    file_path = ""
    data = {}
    pointer = 0

    def __init__(self, file):
        self.file_path = file
        self.data = self.parse(file)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"Контейнер хранит в себе следущее:\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer - 1]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def as_generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    @staticmethod
    def parse(file):
        parsed = []
        with open(file, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (idx, number, date, fio, stip, kuda) = line.replace("\n", "").split(",")
                parsed.append(model(int(idx), int(number), date, fio, stip, kuda))
        return parsed

    def sorted_by_kuda(self):
        return sorted(self.data, key=lambda f: f.kuda)

    def sorted_by_number(self):
        return sorted(self.data, key=lambda f: f.number)

    def value(self, value):
        r = []
        for d in self.data:
            if (d.number > value):
                r.append(d)
        return r

    def add_new(self, number, date,fio, stip, kuda):
        self.data.append(model(len(self.data) + 1, number, date,fio, stip, kuda))
        self.save(self.file_path, self.data)

    @staticmethod
    def save(file, new_data):
        with open(file, "w", encoding='utf-8') as f:
            for r in new_data:
                f.write(f"{r.idx},{r.number},{r.date},{r.fio},{r.stip},{r.kuda}\n")

    def print(self):
        for r in self.data:
            print(f"Запись №{r.idx}: номер = {r.number}, дата= {r.date},ФИО студента= {r.fio}, размер стипендии = {r.stip}, куда выдается справка = {r.kuda}")

    def printd(self, d):
        for r in d:
            print(f"Запись №{r.idx}: номер = {r.number}, дата= {r.date},ФИО студента= {r.fio} размер стипендии = {r.stip}, куда выдается справка = {r.kuda}")

def get_files_count_in_directory(file):
        (loc, dirs, files) = next(os.walk(file))
        return len(files)

data = Data("D:\\papka\\data1.csv.txt")

# __repr__()
print(repr(data), "\n")

# __str__()
print(data, "\n")

# Итератор
for item in iter(data):
    print(item)

print("-" * 64)

# Генератор
for item in data.as_generator():
    print(item)

print("-" * 64)


print("\n")
data.printd(data.sorted_by_number())#сортировка по номеру
print("\n")
data.printd(data.sorted_by_kuda())#сортировка по имени
print("\n")
data.printd(data.value(50))#номер больше 50