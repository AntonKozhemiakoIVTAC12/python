class Animal:
    # создаем атрибуты класса
    name = "lion"
    fro_m = "Africa"
    age = 10
    k = 0

    # создаем методы класса
    def __str__(self): # переопределяем метод __str__ , предоставив наше собственное определение метода
        return "Animal class Object"

    def __init__(self):# За исключением названия, конструктор может использоваться как обычный метод. Вы можете передавать и получать значения из конструктора. Он обычно используется таким образом, когда вам нужно инициализировать значения атрибута при создании экземпляра класса.
        Animal.k += 1
        print(Animal.k)

    def start(self):
        print("Лев проснулся")

    def stop(self):
        print("Лев уснул")

    @staticmethod #метод который может быть вызван напрямую при помощи имени класса
    def get_class_details():
        print("Это класс Animal")

#Animal.get_class_details() #вызов статического метода

class Animal2:
    k = 0
    def start(self, name, fro_m, age):
        print("Капибара проснулась")
        self.name = name
        self.fro_m = fro_m
        self.age = age
        Animal2.k += 1

class Animal3:

    def start(self, name, fro_m, age):
        print("Тигр проснулся")
        self.name = name #переменная public
        self.__fro_m = fro_m #переменная private
        self._age = age #переменная protected


""" Реализация наследования"""
class Animal5:
    def __init__(self, kind, height):
         self.kind = kind
         self.age = 0
         self.height = height

    def info(self):
        """ Метод вывода информации"""
        print("{} years old {}. {} meters high.".format(self.age, self.kind, self.height))

    def grow(self):
        """ Метод роста """
        self.age += 1
        self.height += 0.5

class Zebra(Animal5):
    def __init__(self, kind, height):
        # Необходимо вызвать метод инициализации родителя.
        # В Python 3.x это делается при помощи функции super()
        super().__init__(kind, height)
    def give(self):
        print("Зебра".format(self.kind))

""" Реализация полиморфизма"""
'''str1 = "Антон"
str2 = "Крутой"
print(str1+" "+str2) #самый простой пример

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))'''
#Создаем два класса с похожей структурой, благодаря полиморфизму возможно использовать общую переменную animal для двух классов вместо родительного компонента
class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

class Zebra:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

""" Реализация инкапсуляции"""
class Animal6:

    # создаем конструктор класса Car
    def __init__(self, age):
        # Инициализация свойств
        self.age = age

    # создаем свойство
    @property
    def date_age(self):
        return self.__date_age

    # Сеттер для создания свойств.
    @date_age.setter
    def age(self, date_age):
        if date_age < 1999:
            self.__date_age = 1999
        elif date_age > 2023:
            self.__date_age = 2023
        else:
            self.__date_age = date_age

    def getAnimalAge(self):
        return "Год рождения " + str(self.date_age)

#Создаем объекты классов
'''anim3 = Animal6(1998)

print(anim3.getAnimalAge())'''

'''lion1 = Lion("Richard", 2.5)
zebra1 = Zebra("Artur", 4)

for animal in (lion1, zebra1):
    animal.info()'''

'''anim = Animal5('tiger', 1)
anim.info()
anim.grow()
anim.info()
anim.grow()
anim.info()

anim1 = Zebra('Zebra',10)
anim1.info()
anim1.grow()
anim1.info()
anim1.grow()'''

'''tr_a = Animal3()
tr_a.start("Данил", "из Америки", 10)
print(tr_a.name)'''

'''an_a = Animal()
print(an_a)

an_b = Animal()
an_c = Animal()'''

'''an_b = Animal()
# узнаем тип объекта
print(type(an_b))

an_b.start() #вызываем метод start через объект an_b
an_b.stop() #вызываем метод stop через объект an_a

print(an_b.fro_m) # Получаем доступ к атрибутам класса
print(an_b.age)

print(dir(an_b)) #просмотр всех атрибутов и методов объекта с помощью функции dir

cap_a = Animal2()
cap_a.start("Антон", "из России", 14)
print("Эту капибару зовут",cap_a.name,"он",cap_a.fro_m,"Он у нас", cap_a.k, "в команде капибар")
print("Ей", cap_a.age, "лет" )

cap_b = Animal2()
cap_b.start("Артур", "из Африки", 1)
print("Эту капибару зовут",cap_b.name,"он",cap_b.fro_m,"Он у нас", cap_b.k, "в команде капибар")#при вывоже cap_b.k, получаем 2 в выдаче. Это связано с тем, что атрибут k является атрибутом класса и таким образом он разделяется между экземплярами.
print("Ей", cap_b.age, "лет" ) #Объект cap_a увеличил свое значение до 1, а cap_b налогично увеличил свое значение еще раз, так что итоговое значение равняется 2'''