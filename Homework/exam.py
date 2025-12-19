# Задача 1

number = 42
number_str = str(number)
text = "The answer is: "
result = number_str + text

print(number)
print(type(number))

print(number_str)
print(type(number_str))

print(text)
print(type(text))

print(result)
print(type(result))


# Задача 2

name = input("внесите ваше имя сюда ")
age = input("введите ваш возраст ")
print(f"Меня зовут {name}, мне {age} лет.")



# Задача 3

my_list = [1, 2, 3]
copy_my_list = my_list.copy()
copy_my_list[0] = 10
print(my_list)
print(copy_my_list)

# Задача 4

number = int(input("Введите число: "))
if number > 0:
    print("Положительное")
elif number == 0:
    print("Ноль")
else:
    print("Отрицательное")


# Задача 5

person = {
   "name":{
      "first_name":"Иван",
      "last_name":"Иванов"
   },
   "address":{
      "city":"Москва",
      "country":"Россия"
   }
}
person["address"]["city"] = "Санкт-Петербург"
person["address"]["postal_code"] = "333777"
print(person)
del person["address"]["city"]
print(person)


# Задача 6

number = 0
while number < 20:
    number += 1
    if number % 4 == 0:
        continue
    else:
        print(number)


# Задача 7

with open("fruits.txt", "w+", encoding='utf-8') as file:
    file.write("""яблоко
банан
апельсин""")
    file.seek(0)
    for line in file:
        if line.startswith("а"):
            print(line)


#  Задача 8

def greet_user(user_role, user_name=None):
    if user_name:
        print(f"Привет, {user_name}! Ваша роль: {user_role}")
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")


# Задача 9

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_student = Student("Denis", 30)
print(my_student.name)
print(my_student.age)


# Задача 10

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        print("Животное ест")
    def sleep(self):
        print("Животное спит")

class Dog(Animal):
    def bark(self):
        print("Собака лает")

my_dog = Dog("Спайк", "Собака")
my_dog.eat()
my_dog.sleep()
my_dog.bark()










