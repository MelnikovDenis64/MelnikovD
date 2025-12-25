# Задача 1
#
# Раздел: Методы класса
#
# Создайте класс Robot.
#
# Внутри класса создайте метод greet. Этот метод должен выводить на экран фразу: "Привет! Я робот."
#
# Создайте объект (экземпляр) этого класса с именем r2d2.
#
# Используя созданный объект, вызовите метод greet, чтобы увидеть сообщение.

class Robot:
    def greet(self):
        print("Привет! Я робот.")

r2d2 = Robot()

r2d2.greet()

# Задача 2
#
# Раздел: Конструктор класса __init__
#
# Создайте класс Book (Книга).
#
# Определите метод __init__ (конструктор), который будет принимать два параметра (кроме self): title (название) и author (автор).
#
# Внутри конструктора сохраните переданные значения в атрибуты объекта с именами title и author.
#
# Создайте объект (экземпляр) этого класса с именем my_book, передав в него значения "1984" (название) и "Джордж Оруэлл" (автор).
#
# После создания объекта выведите на экран значение его атрибута author.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_book = Book("1984", "Джордж Оруэлл")

print(my_book.author)

# Задача 3
#
# Раздел: Общие атрибуты (атрибуты класса)
#
# Создайте класс Student.
#
# Объявите на уровне класса атрибут класса (общий для всех объектов) с именем school_name и присвойте ему значение "Школа №1".
#
# В конструкторе (__init__) создайте атрибут объекта с именем name (имя студента), который будет принимать значение из параметра.
#
# Создайте два объекта (экземпляра) этого класса: student1 с именем "Анна" и student2 с именем "Петр".
#
# Выведите на экран значение атрибута класса school_name, обратившись к нему через один из созданных объектов (например, student1.school_name).

class Student:
    school_name = "Школа №1"
    def __init__(self, name):
        self.name = name

student1 = Student("Анна")
student2 = Student("Петр")

print(student1.school_name)


# Задача 4
#
# Раздел: Понимание параметра self
#
# Создайте класс Counter (Счётчик).
#
# В конструкторе (__init__) создайте атрибут объекта count и установите его начальное значение в 0.
#
# Создайте метод increment. Этот метод не должен принимать никаких аргументов, кроме self. Его задача — увеличивать значение атрибута count у того объекта,
# у которого он вызван, на 1.
#
# Создайте объект (экземпляр) этого класса с именем my_counter.
#
# Дважды вызовите метод increment для объекта my_counter.
#
# После всех вызовов выведите на экран значение атрибута count объекта my_counter.

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

my_counter = Counter()

my_counter.increment()
my_counter.increment()

print(my_counter.count)

# Задача 5
#
# Раздел: Создание класса и объекта
#
# Создайте класс Dog (Собака).
#
# Внутри класса создайте только один метод (кроме __init__) с именем bark. Этот метод должен выводить на экран фразу: "Гав!"
#
# Не добавляйте конструктор (__init__) в этот класс. Создайте класс без явного конструктора.
#
# Создайте объект (экземпляр) этого класса с именем my_dog.
#
# Используя созданный объект, вызовите метод bark.


class Dog:
    def bark(self):
        print("Гав!")

my_dog = Dog()
my_dog.bark()

# Задача 6
#
# Раздел: Методы класса
#
# Создайте класс Calculator (Калькулятор).
#
# В конструкторе (__init__) создайте атрибут объекта result и установите его начальное значение в 0.
#
# Создайте метод add, который принимает один параметр num (кроме self) и прибавляет его значение к атрибуту result текущего объекта.
#
# Создайте объект (экземпляр) этого класса с именем calc.
#
# Вызовите метод add для объекта calc дважды: сначала с аргументом 5, затем с аргументом 3.
#
# После всех вызовов выведите на экран значение атрибута result объекта calc.

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num

calc = Calculator()
calc.add(5)
calc.add(3)
print(calc.result)

# Задача 7
#
# Раздел: Общие атрибуты (атрибуты класса) и Понимание параметра self
#
# Создайте класс Car (Автомобиль).
#
# Объявите на уровне класса атрибут класса wheels (колёса) и присвойте ему значение 4.
#
# В конструкторе (__init__) создайте атрибут объекта color (цвет), который будет принимать значение из параметра.
#
# Создайте метод describe, который не принимает аргументов, кроме self. Этот метод должен выводить на экран одну фразу в формате:
# "Это автомобиль цвета {color}. У него {wheels} колеса.", где {color} — это значение атрибута объекта, а {wheels} — значение атрибута класса.
#
# Создайте объект этого класса с именем my_car, передав в конструктор значение "красный".
#
# Вызовите метод describe для объекта my_car.

class Car:
    wheels = 4
    def __init__(self, color):
        self.color = color
    def describe (self):
        print(f"Это автомобиль цвета {self.color}. У него {self.wheels} колеса.")

my_car = Car("красный")
my_car.describe()


# Задача 8
#
# Раздел: Комбинированная (Конструктор, методы, атрибуты объекта, параметр self)
#
# Создайте класс BankAccount (Банковский счёт).
#
# Конструктор (__init__) должен принимать один параметр owner (владелец) и сохранять его в атрибут объекта. Также в конструкторе создайте атрибут объекта balance (баланс) и установите его начальное значение в 0.
#
# Создайте метод deposit, который принимает один параметр amount (сумма) и увеличивает баланс счёта (balance) на эту сумму.
#
# Создайте метод withdraw, который принимает один параметр amount (сумма). Если запрошенная сумма (amount) меньше или равна текущему балансу (balance), то уменьшите баланс на эту сумму. Если сумма больше баланса, метод должен вывести сообщение: "Недостаточно средств."
#
# Создайте метод info, который выводит строку в формате: "Владелец: {owner}, Баланс: {balance} руб.", где {owner} и {balance} — значения атрибутов объекта.
#
# Создайте объект класса BankAccount с именем account для владельца "Иван".
#
# Выполните операции:
#
# Внесите на счёт 1000 руб. (вызовите deposit).
#
# Попытайтесь снять 700 руб. (вызовите withdraw).
#
# Попытайтесь снять 400 руб. (вызовите withdraw).
#
# Выведите информацию о счёте (вызовите info).


class BankAccount:
    def deposit(self, amount):
        self.balance += amount
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств.")
    def info(self):
        print(f"Владелец: {self.owner}, Баланс: {self.balance} руб.")

account = BankAccount("Иван")
account.deposit(1000)
account.withdraw(700)
account.withdraw(400)
account.info()


# Задача 9
#
# Раздел: Комбинированная (Конструктор, атрибуты объекта и класса, методы, параметр self)
#
# Создайте класс Employee (Сотрудник).
#
# Объявите атрибут класса company (компания) со значением "TechCorp". Этот атрибут общий для всех сотрудников.
#
# Конструктор (__init__) должен принимать два параметра: name (имя) и position (должность). Сохраните их в атрибуты объекта с такими же именами.
#
# Создайте метод introduce, который выводит строку в формате:
# "Меня зовут {name}. Я работаю в компании {company} на должности {position}."
# Значения {name} и {position} должны браться из атрибутов объекта, а {company} — из атрибута класса.
#
# Создайте объект класса Employee с именем emp1 для сотрудника с именем "Алексей" и должностью "Инженер".
#
# Вызовите метод introduce для этого объекта.

class Employee:
    company = "TechCorp"
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def introduce(self):
        print(f"Меня зовут {self.name}. Я работаю в компании {self.company} на должности {self.position}.")

emp1 = Employee("Алексей", "Инженер")
emp1.introduce()

# Задача 10 (повторение и комбинирование)
#
# Создайте класс Student, который представляет студента.
#
# Требования:
#
# Общий атрибут класса university со значением "National University".
#
# Конструктор принимает name (имя студента) и student_id (номер студенческого билета). Инициализирует атрибуты name и student_id объекта.
#
# Метод add_grade(self, subject, grade) – добавляет оценку по предмету. Предметы и оценки храните в словаре self.grades,
# где ключ – название предмета (строка), значение – оценка (целое число). Если словаря ещё нет, создайте его в конструкторе (или при первом добавлении).
# Метод должен обновлять словарь и печатать: "Добавлена оценка {grade} по предмету {subject}".
#
# Метод get_average(self) – возвращает средний балл студента по всем предметам (округлить до двух знаков после запятой). Если оценок нет, возвращает 0.
#
# Метод show_info(self) – выводит информацию в формате:
#
# text
# Student: {self.name}
# ID: {self.student_id}
# University: {self.university}
# Grades: {self.grades}
# Average: {средний балл}
# Пример использования:
#
# python
# stud = Student("Anna Petrova", "ST123")
# stud.add_grade("Math", 85)
# stud.add_grade("Physics", 92)
# print(stud.get_average())  # 88.5
# stud.show_info()
# Напишите код класса Student, реализующий все указанные требования.


class Student:
    university = "National University"
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Добавлена оценка {grade} по предмету {subject}")
    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)
    def show_info(self):
        print(f"""Student: {self.name}
ID: {self.student_id}
University: {self.university}
Grades: {self.grades}
Average: {self.get_average()}""")


stud = Student("Anna Petrova", "ST123")
stud.add_grade("Math", 85)
stud.add_grade("Physics", 92)
print(stud.get_average())
stud.show_info()





