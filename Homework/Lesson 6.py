# Задача 3.
# Дан словарь person = {'name': 'Alice', 'age': 25}. Выведи на экран возраст (age) персоны.

person = {'name': 'Alice', 'age': 25}
print(person["age"])

# Задача 7.
# Дан словарь fruit = {'name': 'apple', 'color': 'red', 'weight': 150}. Удали ключ 'weight' и его значение.

fruit = {'name': 'apple', 'color': 'red', 'weight': 150}
del fruit["weight"]
print(fruit)    

# Задача 5.
# Дан словарь car = {'model': 'Toyota'}. Добавь в него новый ключ 'color' со значением 'red'.

car = {'model': 'Toyota'}
car["color"] = "red"
print(car)

# Задача 11.
# Дан словарь user = {'login': 'admin', 'password': '1234'}. Проверь, существует ли в словаре ключ 'login'.
# Результат проверки (True/False) сохрани в переменную.

user = {
    'login': 'admin',
    'password': '1234'
}
result = "login" in user

# Задача 9.
# Дан словарь country = {'name': 'Germany', 'capital': 'Berlin'}. Выведи список всех его ключей.

country = {'name': 'Germany', 'capital': 'Berlin'}
print(country.keys())

# Задача 1.
# Создай словарь book с ключами 'title', 'author' и 'year' и значениями 'Война и мир', 'Лев Толстой' и 1869 соответственно.

book = {
    "title": "Война и мир",
    "author": "Лев Толстой",
    "year": 1869,}


# Задача 8.
# Дан словарь config = {'lang': 'Python', 'version': 3.9}. Удали ключ 'version' с помощью метода pop().

config = {'lang': 'Python', 'version': 3.9}
config.pop("version")

# Задача 6.
# Дан словарь score = {'math': 90}. Обнови оценку по математике на 95.

score = {'math': 90}
score["math"] = 95


# Задача 10.
# Дан словарь color = {'r': 255, 'g': 0, 'b': 0}. Выведи список всех его значений.

color = {'r': 255, 'g': 0, 'b': 0}
print(color.values())

# Задача 4.
# Дан словарь product = {'name': 'iPhone', 'price': 999}. Выведи на экран название товара.

product = {'name': 'iPhone', 'price': 999}
print(product['name'])

# Задача 12.
# Дан словарь bag = {'pen': 2, 'pencil': 1}. Проверь, есть ли в словаре значение 1. Результат проверки (True/False) сохрани в переменную.

bag = {'pen': 2, 'pencil': 1}
result_bool = 1 in bag.values()

# Задача 2.
# Создай пустой словарь с именем my_dict.

my_dict = {}