
items = [1, 2, 3]
print(type(items))

number_str = "100"
number_int = int(number_str)
print(type(number_int))
print(number_int)

x = 20
y = 20
print(x == y)

word = "Python"
print(word[0])

alphabet = "abcdefgh"
result = alphabet[2:5]
print(result)

message = "Привет"
print(message.count("и"))
print(len(message))

text = "PYTHON"
text_low = text.lower()
print(text_low)

letters = ['a', 'c']
letters.insert(1, 'b')
print(letters)

list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)

age = int(input("Возраст: "))
access = "granted" if age >= 18 else "denied"
print(access)


text = input("Введи строку: ")
text_len = len(text)
print("Длина строки = " + str(text_len))



print("Длина строки = " + str(len(input("Введи строку: "))))




