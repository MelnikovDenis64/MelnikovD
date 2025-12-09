# Комплексная задача 1.
# Словарь + строки - Создай словарь person с ключами name (строка), age (число), city (строка).
# Затем используй f-строку чтобы вывести: "Имя: [name], Возраст: [age], Город: [city]"

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

