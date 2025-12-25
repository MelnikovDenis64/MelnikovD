# Задача 1
#
# Создай базовый класс Vehicle (Транспортное средство).
#
# В его конструкторе (__init__) определи атрибут self.name, который должен принимать значение из параметра name.
#
# Также в конструкторе определи атрибут self.speed = 0.
#
# Создай дочерний класс Car (Автомобиль), который наследуется от Vehicle.
#
# В конструкторе класса Car должен вызываться конструктор родительского класса.
#
# Добавь в конструктор класса Car новый атрибут self.brand, который принимает значение из параметра brand.
#
# Создай экземпляр класса Car с именем "Седан" и брендом "Toyota". Выведи на экран его атрибуты name, brand и speed.

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = 0

class Car(Vehicle):
    def __init__(self, name, brand):
        Vehicle.__init__(self, name)
        self.brand = brand

my_car = Car("Седан", "Toyota")
print(my_car.name, my_car.brand, my_car.speed)



# Создай базовый класс Animal (Животное).
#
# В его конструкторе (__init__) определи атрибут self.name, который принимает значение из параметра name.
#
# Добавь метод speak(self), который печатает строку: "Животное издает звук.".
#
# Создай дочерний класс Dog (Собака), который наследуется от Animal.
#
# В классе Dog переопредели метод speak(self), чтобы он печатал строку: "Гав!".
#
# Создай экземпляр класса Dog с именем "Бобик". Вызови его метод speak().

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Животное издает звук.")

class Dog(Animal):
    def speak(self):
        print("Гав!")

my_dog = Dog("Бобик")
my_dog.speak()