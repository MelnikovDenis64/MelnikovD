# Комплексная задача 1.
# Словарь + строки - Создай словарь person с ключами name (строка), age (число), city (строка).
# Затем используй f-строку чтобы вывести: "Имя: [name], Возраст: [age], Город: [city]"
import time

person = {"name": "Denis",
           "age": 25,
           "city": "Moscow"
           }
print(f"Имя: {person["name"]}, Возраст: {person["age"]}, Город: {person["city"]}")



# Создай класс Car.
# В его методе __init__ определи атрибуты brand (марка) и model (модель), которые должны устанавливаться при создании объекта.
# Создай метод get_info, который возвращает строку в формате "Марка: [brand], Модель: [model]".
# Создай объект этого класса с любыми значениями и выведи результат работы метода get_info.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}"

my_car = Car("БМВ", "М1")
print(my_car.get_info())



# Напиши простой декоратор my_decorator, который перед вызовом декорируемой функции печатает строку "Функция вызывается",
# а после вызова — "Функция завершила работу". Примени этот декоратор к функции say_hello, которая принимает один аргумент name
# (со значением по умолчанию 'Гость') и печатает f"Привет, {name}!". Вызови say_hello() и say_hello('Анна').

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Функция вызывается")
        func(*args, **kwargs)
        print("Функция завершила работу")
    return wrapper

@my_decorator
def say_hello(name="Гость"):
    print(f"Привет, {name}!")

say_hello()
say_hello("Анна")



# Используя цикл while, выводи числа от 1 до 10.
# Но внутри цикла сделай условие: если текущее число равно 5, прерви цикл с помощью break. После цикла выведи строку "Цикл завершен".

number = 1
while number <= 10:
    if number == 5:
        break
    else:
        print(number)
        number += 1
print("Цикл завершен")



# Создай функцию process_list, которая принимает один аргумент input_list. Внутри функции создай пустой список result.
# С помощью цикла for пройдись по input_list и добавь в result каждый элемент, умноженный на 2.
# Верни список result. Вызови функцию, передав ей список [1, 2, 3, 4, 5], и выведи результат.

def process_list(input_list):
    result = []
    for item in input_list:
        result.append(item * 2)
    return result

print(process_list([1, 2, 3, 4, 5]))

def process_list(input_list):
    result = [item * 2 for item in input_list]
    return result

print(process_list([1, 2, 3, 4, 5]))



# Создай переменную name с твоим именем и переменную age с твоим возрастом (числом).
# Используя f-строку, создай переменную greeting, которая будет строкой: "Привет, меня зовут [name], мне [age] лет".
# Напиши условие: если возраст больше или равен 18, выведи "Совершеннолетний", иначе — "Несовершеннолетний".

name = input("Имя: ")
age = int(input("Возраст: "))
greeting = f"Привет, меня зовут {name}, мне {age} лет"
print(greeting)
if age >= 18:
    print("Совершеннолетний")
else:
    print("Несовершеннолетний")



# Создай словарь book с ключами: title (значение — название любой книги), author (имя автора), year (год издания, число).
# Проверь с помощью операции in, есть ли в словаре ключ 'pages'. Если нет — добавь его со значением 300.
# Запиши все пары ключ-значение этого словаря в файл book.txt, каждую пару с новой строки в формате ключ: значение.

book = {"title": "Random book",
        "author": "Random author",
        "year": 1998}

if not "pages" in book:
    book["pages"] = 300

with open("book.txt", "w") as file:
    for key, value in book.items():
        file.write(f"{key}: {value}\n")



# Создай строку text = "Программирование".
# С помощью среза получи из нее подстроку с 3-го по 10-й символ (включительно) и сохрани в переменную part.
# Создай переменную length_check, которая с помощью тернарного оператора будет содержать строку "Длинное" если длина part больше 5, иначе — "Короткое".
# Выведи результат в формате "Часть строки: [part]. [length_check]."


text = "Программирование"
part = text[3:11]
length_check = "Длинное" if len(part) > 5 else "Короткое"
print(f"Часть строки: {part}. {length_check}.")




# Создай словарь inventory = {"яблоки": 10, "бананы": 5, "хлеб": 1}.
# Напиши цикл while, который спрашивает у пользователя (функция input()) название товара.
# Если товар есть в словаре, выведи его количество, иначе выведи "Товар отсутствует".
# Цикл должен прерываться (break), если пользователь вводит "стоп".

inventory = {"яблоки": 10, "бананы": 5, "хлеб": 1}
while True:
    name = input("Название товара: ")
    if name.lower() in inventory:
        print (inventory[name.lower()])
    elif name.lower() == "стоп":
        break
    else:
        print("Товар отсутствует")



# Создай базовый класс Animal с методом __init__, который принимает name (имя животного) и сохраняет его в атрибут.
# Добавь метод sound, который печатает "Издает звук". Создай дочерний класс Dog, который наследует Animal.
# В классе Dog переопредели метод sound, чтобы он печатал "[name] гавкает".
# Создай объект класса Dog с именем "Бобик" и вызови его метод sound.

class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Издает звук")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} гавкает")

my_dog = Dog("Бобик")
my_dog.sound()


# Создай декоратор log_call, который перед вызовом функции печатает "Вызов функции [имя_функции]".
# Примени его к функции greet, которая принимает name (по умолчанию "Друг") и возвращает строку f"Привет, {name}!".
# Вызови greet() и greet("Мария"), выведи результаты.


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name="Друг"):
    return f"Привет, {name}!"

print(greet())
print(greet("Мария"))


# Создай список numbers = [10, 20, 30, 40, 50, 60, 70].
# С помощью среза создай новый список middle, содержащий элементы с 3-го по 5-й (включительно).
# Затем напиши цикл for, который проходит по middle и выводит только те элементы, которые больше 35.

numbers = [10, 20, 30, 40, 50, 60, 70]
middle = numbers[3:6]
for number in middle:
    if number > 35:
        print(number)


# Создай класс BankAccount. В __init__ задай атрибуты owner (владелец, строка) и balance (баланс, число, по умолчанию 0).
# Добавь метод deposit(amount), который увеличивает баланс на amount.
# Добавь метод withdraw(amount), который уменьшает баланс на amount, но только если amount не превышает balance, иначе выводит "Недостаточно средств".
# Создай объект, пополни баланс на 100, затем попробуй снять 30 и выведи итоговый баланс.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")

my_account = BankAccount("Denis")
my_account.deposit(100)
my_account.withdraw(30)
print(my_account.balance)



# Создай строку data = "Python;42;3.14;True". Раздели её на список по символу ;.
# Преобразуй второй элемент списка в целое число, третий — в число с плавающей точкой, четвёртый — в булево значение (используй функцию bool()).
# Запиши полученные преобразованные значения (кроме первого) в файл data.txt через запятую в одну строку.

data = "Python;42;3.14;True"
data_list = data.split(";")
data_list[1] = int(data_list[1])
data_list[2] = float(data_list[2])
data_list[3] = data_list[3] == "True"
with open("data.txt", "w") as file:
    file.write(f"{data_list[1]}, {data_list[2]}, {data_list[3]}")


# Напиши программу, которая запрашивает у пользователя два числа (input).
# Преобразуй их к типу int. Используя тернарный оператор, определи переменную relation, которая будет строкой "первое больше"
# если первое число больше второго, "второе больше" если второе больше первого, и "равны" если они равны.
# Выведи результат в формате "Числа: [a] и [b]. [relation]." с помощью f-строки.

num_a, num_b = int(input("Первое число: ")), int(input("Второе число: "))
relation = "первое больше" if num_a > num_b else ("равны" if num_a == num_b else "второе больше")
print(f"Числа: {num_a} и {num_b}. {relation}.")


# Создай базовый класс Device с атрибутами brand (бренд) и power (мощность в ваттах, число),
# которые задаются в __init__. Добавь метод get_info, который возвращает строку "Устройство: [brand], мощность: [power]Вт".
# Создай дочерний класс CoffeeMachine, который наследует Device. В его __init__ также принимай аргумент cups (количество чашек, число по умолчанию 2)
# и сохраняй его в атрибут. Переопредели метод get_info, чтобы он возвращал строку от родительского метода с добавлением ",
# количество чашек: [cups]" в конце.
# Напиши функцию print_device_info(device), которая принимает любой объект класса Device (или его наследника)
# и выводит результат вызова его метода get_info.
# Создай объект Device с брендом "Generic" и мощностью 1000. Создай объект CoffeeMachine с брендом "Bosch", мощностью 1200 и количеством чашек 4.
# Вызови для каждого функцию print_device_info.


class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
    def get_info(self):
        return f"Устройство: {self.brand}, мощность: {self.power}Вт"

class CoffeeMachine(Device):
    def __init__(self, brand, power, cups):
        Device.__init__(self, brand, power)
        self.cups = cups
    def get_info(self):
        return f"Устройство: {self.brand}, мощность: {self.power}Вт, количество чашек: {self.cups}"

def print_device_info(device):
    print(device.get_info())

my_device = Device("Generic", 1000)
my_coffee_machine = CoffeeMachine("Bosch", 1200, 4)

print_device_info(my_device)
print_device_info(my_coffee_machine)



# Напиши декоратор repeat(n), который принимает число n и вызывает декорируемую функцию n раз.
# Декоратор должен возвращать функцию-обёртку, которая при вызове запускает целевую функцию указанное количество раз
# и возвращает список результатов всех вызовов.
# Создай также функцию add_five(x), которая возвращает x + 5. Примени к ней декоратор repeat(4) и вызови с аргументом 10. Выведи результат.

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(n):
                result.append(func(*args, **kwargs))
            return result
        return wrapper

#@repeat(4)
def add_five(x):
    return x + 5

print(add_five(10))




# Создай список lines = ["Первая строка", "Вторая строка", "Третья строка", "Четвертая строка"].
# Запиши в файл output.txt только второй и третий элементы списка (используй срез), каждый с новой строки.
# Затем прочитай файл и выведи его содержимое.



lines = ["Первая строка", "Вторая строка", "Третья строка", "Четвертая строка"]
with open("output.txt", "w+", encoding='utf-8') as file:
    file.write(f"{lines[1]}\n{lines[2]}")
    file.seek(0)
    print(file.read())


# Создай словарь products = {"хлеб": 50, "молоко": 80, "сыр": 200}.
# Напиши цикл for, который проходит по парам ключ-значение и выводит строку в формате "Товар: [название], Цена: [цена] руб."
# только для товаров дороже 70 рублей.

products = {"хлеб": 50, "молоко": 80, "сыр": 200}
for key, value in products.items():
    if value > 70:
        print(f"Товар: {key}, Цена: {value} руб.")


# Напиши программу, которая в цикле while запрашивает у пользователя числа (input).
# Прерывает цикл, если введено 0. Внутри цикла проверяй: если число больше 100, выведи "Большое число",
# если меньше 0 — "Отрицательное", иначе — "Обычное число".


while True:
    number = int(input("Введите число: "))
    if number > 100:
        print("Большое число")
    elif number < 0:
        print("Отрицательное")
    elif number == 0:
        break
    else:
        print("Обычное число")


# Создай класс Student с атрибутами name (строка) и grades (список чисел).
# Добавь метод add_grade(grade), который добавляет оценку в список grades.
# Создай дочерний класс GroupStudent, который добавляет атрибут group (строка).
# Переопредели метод add_grade, чтобы он выводил "Оценка добавлена в группу [group]" перед добавлением.
# Создай объект GroupStudent, добавь две оценки и выведи список оценок.


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        self.grades += [grade,]

class GroupStudent(Student):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def add_grade(self, grade):
        print(f"Оценка добавлена в группу {self.group}")
        super().add_grade(grade)

i_student = GroupStudent("Denis", "One")
i_student.add_grade(10)
i_student.add_grade(20)
print(i_student.grades)



# Напишите функцию starts_with, которая принимает два аргумента: строку text и строку prefix.
# Функция должна возвращать True, если text начинается с подстроки prefix, и False в противном случае.
# Используйте срезы строк для сравнения.

def starts_with(text, prefix):
    number = len(prefix)
    prefix_text = text[:number]
    return prefix_text == prefix


# Создайте класс Book.
# В конструкторе (__init__) инициализируйте три атрибута объекта: title (название, строка), author (автор, строка),
# pages (количество страниц, целое число).
# Добавьте метод description, который возвращает строку в формате: "<название>", автор: <автор>, страниц: <pages>.
#
# После определения класса создайте объект этого класса с данными:
# title="1984", author="George Orwell", pages=328.
# Вызовите у этого объекта метод description и выведите результат на экран.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def description(self):
        return f"\"{self.title}\", автор: {self.author}, страниц: {self.pages}"

my_book = Book("1984", "George Orwell", 328)
print(my_book.description())


# Дан словарь:
# data = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
#
# Добавьте в словарь новый элемент с ключом "fig" и значением 4.
#
# Увеличьте значение для ключа "banana" на 3 (т.е. обновите его).
#
# Используя цикл for, выведите на экран только те ключи, у которых значение больше или равно 5, в формате:
# Ключ: <ключ>, Значение: <значение>
# Каждая пара — на новой строке.
#
# Примечание: Для проверки условия используйте оператор сравнения внутри цикла.

data = {"apple": 5, "banana": 2, "cherry": 8, "date": 1}
data["fig"] = 4
data["banana"] += 3

for key, value in data.items():
    if value >= 5:
        print(f"Ключ: {key}, Значение: {value}")
    else:
        continue


# Напишите декоратор timer, который измеряет время выполнения функции и выводит его в секундах с сообщением:
# "Функция выполнялась <время> сек."
#
# Для измерения времени импортируйте модуль time и используйте time.time() до вызова функции и после.
# Декоратор должен возвращать результат исходной функции.
#
# Примените декоратор к простой функции sum_list, которая принимает список чисел и возвращает их сумму.

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция выполнялась {end_time - start_time} сек.")
        return result
    return wrapper

@timer
def sum_list(a, b, c, d, e):
    return a + b + c + d + e

print(sum_list(1, 2, 3, 4, 5))


# Создайте текстовый файл notes.txt и запишите в него три строки:
#
# text
# Первая строка.
# Вторая строка.
# Третья строка.
# Затем, используя контекстный менеджер with, откройте этот файл для чтения, прочитайте все строки в список и выведите на экран:
#
# Количество строк в файле (используйте функцию len).
#
# Саму последнюю строку файла (вспомните индексацию списка).

with open("notes.txt", "w", encoding='utf-8') as file:
    file.write("Первая строка.\nВторая строка.\nТретья строка.")

with open("notes.txt", "r", encoding='utf-8') as file:
    string_file = []
    for line in file:
        string_file.append(line.strip())
    print(len(string_file))
    print(string_file[-1])


# Напишите код, который:
#
# Создаёт список numbers = [12, 7, 19, 3, 14, 10].
#
# С помощью цикла for и условного оператора if формирует новый список even_squares, содержащий квадраты только тех чисел из numbers,
# которые являются чётными.
#
# Используя f-строку, выводит результат в формате:
# Чётные числа в квадрате: [список].

numbers = [12, 7, 19, 3, 14, 10]
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number**2)
print(f"Чётные числа в квадрате: {even_squares}")


# Создайте базовый класс Animal (Животное).
# В его конструкторе (__init__) должен быть один параметр name (имя животного), который сохраняется в атрибут self.name.
# Также в классе Animal определите метод make_sound, который возвращает строку "Some generic sound".
#
# Затем создайте дочерний класс Dog (Собака), который наследует от Animal.
# В классе Dog переопределите метод make_sound, чтобы он возвращал строку "Woof!".
#
# После этого:
#
# Создайте объект класса Dog с именем "Rex".
#
# Вызовите у этого объекта метод make_sound и выведите результат на экран.
#
# Также выведите на экран значение атрибута name этого объекта.


class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

my_dog = Dog("Rex")
print(my_dog.make_sound())
print(my_dog.name)


# Создайте строку text = "Automation with Python".
# С помощью срезов получите из неё три подстроки и сохраните их в переменные:
#
# first_word — первое слово (до первого пробела).
#
# last_word — последнее слово (после последнего пробела).
#
# middle — фраза, которая начинается со второго символа исходной строки и заканчивается предпоследним символом включительно.
#
# Затем, используя f-строку, выведите результат в формате:
# Слова: <первое слово> - <последнее слово>. Средняя часть: <middle>

text = "Automation with Python"
sep_string = text.split(" ")
first_word = sep_string[0]
last_word = sep_string[2]
middle = text[1:-1]
print(f"Слова: {first_word} - {last_word}. Средняя часть: {middle}")


# Напишите код, который:
#
# Запрашивает у пользователя целое число с помощью input() и преобразует его в тип int.
#
# Используя тернарный оператор, определяет, является ли это число чётным.
#
# Результат тернарного оператора сохраните в переменную result. Он должен быть строкой: "чётное" или "нечётное".
#
# Используя f-строку, выведите сообщение: "Число <число> — <result>.".

number = int(input("Число: "))
result = "чётное" if number % 2 == 0 else "нечётное"
print(f"Число {number} — {result}.")


# Напишите программу, которая:
#
# Создаёт словарь inventory с начальными данными:
# {"apples": 10, "bananas": 5, "oranges": 8}
#
# Запрашивает у пользователя название товара (ключ) и количество (целое число) через input().
#
# Проверяет, есть ли такой ключ в словаре, используя оператор in.
#
# Если ключ есть, то увеличивает его значение на введённое количество (обновляет словарь).
#
# Если ключа нет, то добавляет новый элемент в словарь с этим ключом и введённым количеством.
#
# В конце, используя цикл while, выводит на экран все элементы словаря в формате "<ключ>: <значение>" (каждый на новой строке), пока не будут выведены все. Для этого:
#
# Создайте список ключей словаря.
#
# Используйте переменную-счётчик (индекс) для прохода по списку.
#
# Выход из цикла должен происходить, когда счётчик достигнет длины списка ключей.

inventory = {"apples": 10, "bananas": 5, "oranges": 8}
client_key, client_value = input("Товар: "), input("Кол-во: ")
if client_key in inventory.keys():
    inventory[client_key] += int(client_value)
else:
    inventory[client_key] = int(client_value)
numbers = len(inventory)
iteration_number = 0
inventory_list = []
for key in inventory.keys():
    inventory_list.append(key)
while iteration_number < numbers:
    print(f"{inventory_list[iteration_number]} : {inventory[inventory_list[iteration_number]]}")
    iteration_number += 1
