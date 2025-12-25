# Задача 2 (Аргументы функций):
# Напишите функцию print_name, которая принимает один аргумент name (имя) и выводит на экран строку "Ваше имя: [name]".

# Задача 5 (Декораторы):
# Создайте простой декоратор my_decorator, который перед вызовом любой декорируемой функции выводит на экран сообщение "Функция вызвана".

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Функция вызвана")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def print_name(name):
    print(f"Ваше имя: {name}")

print_name("Денис")


# Задача 4 (Возвращение данных из функций):
# Напишите функцию multiply, которая принимает два числа и возвращает их произведение. Вызовите функцию и сохраните результат в переменную.

def multiply(x, y):
    return x * y

result_2 = multiply(2, 3)
print(result_2)

# Задача 1 (Функции в Python / Создание и вызов функций):
# Создайте функцию с именем say_hello, которая выводит на экран фразу "Привет, мир!".

def say_hello():
    print("Привет, мир!")

say_hello()

# Задача 3 (Аргументы с дефолтными значениями):
# Создайте функцию greet_user, которая принимает имя пользователя и приветствие. Приветствие должно иметь значение по умолчанию "Здравствуй".

def greet_user(user_name, greetings="Здравствуй"):
    result = f"{greetings}, {user_name}"
    return result

print(greet_user("Денис"))


# Задача D1 (Декораторы):
# Создайте декоратор repeat_hello, который заставляет декорированную функцию вывести "Привет!" два раза подряд.
# Сам декоратор не должен ничего выводить, он должен модифицировать поведение функции.

def repeat_hello(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat_hello
def say_hello():
    print("Привет!")

say_hello()

# Задача D2 (Декораторы):
# Создайте декоратор show_call, который выводит на экран строку "Вызывается функция <имя_функции>"
# перед каждым вызовом декорированной функции. Для получения имени функции используйте func.__name__.

def show_call(func):
    def wrapper():
        print(f"Вызывается функция {func.__name__}")
        func()
    return wrapper

@show_call
def my_function():
    print("Выполняю работу")

my_function()


# Задача D3 (Декораторы):
# Создайте декоратор uppercase_result, который преобразует возвращаемое значение декорированной функции к верхнему регистру
# (используйте .upper()). Предполагается, что функция возвращает строку.

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).upper()
        return result
    return wrapper

@uppercase_result
def return_message():
    return "hello world"

result = return_message()
print(result)

# Задача FD (Функция + Декоратор):
# Функция: Напишите функцию get_full_name(first_name, last_name), которая принимает имя и фамилию, объединяет их через пробел
# и возвращает получившуюся строку.
# Декоратор: Напишите декоратор add_greeting, который модифицирует результат функции, добавляя в начало строку "Привет, ",
# а в конец — восклицательный знак.

def add_greeting(func):
    def wrapper(*args, **kwargs):
        result = f"Привет, {func(*args, **kwargs)}!"
        return result
    return wrapper

@add_greeting
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(get_full_name("Денис", "Мельников"))


