# # Типы данных в питоне:
# 1. NoneType -> Ничего, пустота
# 2. Boolean -> Правда или Ложь (True/False)
# 3. Числовые типы данных:
#         а. integer(int) -> Целое число(1,2)
#         b. float() -> Числа с плавающей точкой(-1.2, 100,200, 2,7)
#         c. complex() комлекстные числа(3+5i/j)
# 4. Списковые типы данных:
#         а. list(список)(массив) -> [1,2,3,True, None, "Hello",]
#         b. tuple(кортеж) -> (1,2,3,False)
#         c. range(1,3) -> range(1,2)
# 5. str() -> Строки: "Hello world",'Salam 312'
# 6. set() -> Множества
# 7. dict -> Словарь: содержит данные в виде ключа: значения -> {1: 'one', 2: 'two'...}

# ******************************************
# Mutable(изменяемые типы данных)
#     1. list()
#     2. set()
#     3. dict()

# Immutable(неизменяемые типы данных)
#     1. NoneType
#     2. boolen
#     3. int(), float(), complex()
#     4. str()
#     5. range()
#     6. tuple()

# ******************************************
# '''Стандартный вывод данных'''
# """
# в пайтоне для вывода данных в терминал
# используется функция print()
# """
# print('Hello world')

# """Стандартный ввод данных через терминал
# используется функция input"""

# a = input('Введите число: ')
# print(a)
# # type() выводит тип данных
# print(type(a))

# b = int(input('Введите число номер2: '))
# print(b)
# print(type(b))

# # print(input('asd'))
# print(a, b, 'Salam')

# import random

# num1 = uniform(0.1, 1)
# num2 = uniform(9.5, 99.5)


# num1 = round(num1, 2)
# num2 = round(num2, 2)

# print(num1, num2)

# result = num1 * num2
# print(result)

# a = 20
# int = 45
# print(int)

# text = 'Hello world'
# print(text)

# a = 4
# b = 'world'
# print(a*b)

# from itertools import count

# a = 10
# b = 5
# print(a + b)

# from unittest import result


# a = 10
# b = 5
# result = a / b
# print(result)

# a = 10
# b = -5
# a = abs(10)
# b = abs(-5)
# result = a, b
# print(result)

# a = 3
# b = 3
# result = a ** b
# print(result)

# a = 10
# b = 4
# result = a % b
# print(result)

# a = 4
# b = 2
# c = 5
# result = (a ** b) % c
# print(result)

# a = 4
# b = 5
# c = 3
# result = (a * b) % c
# print(result)

# a = 11
# b = 3
# c = 1.5

# result = (a % b) * c
# print(result)

# from math import sqrt

# a = 5
# x = sqrt(a)
# print(pow(a,2))
# print(pow(a,3))
# print(x)

# a, b = map(float, input("a b » ").split())
# print("c =", (a * a + b * b)**0.5)

# a = 5
# b = 3
# result = sqrt((a**2) + (b**2))
# print(result)

# import math
# from turtle import circle

# r = 5
# obj = circle
# result = (math.pi*r**2)
# print(result)

# x = 2
# y = 1
# z = 3

# x, y, z = y, z, x
# print(x)
# print(y)
# print(z)

# data = 10500
# key = 90
# result = data ^ key
# print(result)

# from random import random

# num1 = uniform(0.1, 1)
# num2 = uniform(9.5, 99.5)


# num1 = round(num1, 2)
# num2 = round(num2, 2)

# print(num1, num2)

# # result = num1 * num2
# # print(result)

#задачи 10.06

# name = 'black'
# print(name[0])
# print(name[-5])

# name = 'black'
# print(name[4])
# print(name[-1])

# text = 'black star'
# print(text[8:10])

# text = 'black star'
# print(text[::-1])

# word1 = 'black'
# word2 = 'star'
# probel = ' '
# result = word1 + probel + word2
# print(result)

# name = 'redstar'
# result = 'redstar' * 4
# print(result)

# text = 'black star'
# print(len(text))

# from ast import Str
# import string
# from turtle import position


# text = 'The quick brown fox jumps over the lazy dog'
# print(text.replace('o','*'))

# text = 'redstar'
# print(text.upper())

# text = 'REDSTAR'
# print(text.lower())

# text = 'blackstar'
# text2 = list(text)
# text2[0],text2[-1]=text2[-1],text2[0]
# result = ''.join(text2)
# print(result)

# text = #makers#bootcamp#программирование#it#курсы 
#  ['makers', 'bootcamp', 'программирование', 'it', 'курсы']

#  text = 

# text = '#makers#bootcamp#программирование#it#курсы'
# splited = text.split('#')
# print(splited)

# "Вас зовут Иван Пупкин, Ваш возраст: 35, Вы проживаете в городе Москва"
# name = input('Enter your name:')
# last_name = input('Enter your last name: ')
# age = input('Enter your age: ')
# city = input('Enter your city: ')
# print(f'Your name is {name} {last_name}, you are {age} years old, you live in {city}')
# print('Hello, mr/mrs ' + name, last_name)
# print('Hello, mr/mrs ' + name + ' ' + last_name)

# 14) Дана строка. Выведите только символы с нечётными индексами при помощи срезов. Например: 'Makers bootcamp' -> 'aesbocm'.

# text = 'Makers bootcamp'

# print(len(text))
# print(text[::2])

# 15) Объявите строку "abracadabra", затем поменяйте шестую букву на "K". Например: "abracadabra" -> abracKdabra.


# text = 'abracadabra'
# print(text[:5] + 'K' + text[6:])



# 2. Дана строка. Рандомно вытащите один символ bp этой строки. Пример: "Makers" -> "s".

# import random
# import string

# text = 'Makers'
# print(random.choice(text))



# 3. Даны две переменные s1 = "America" и s2 = "Japan". Выведите 
#    новую строку в который будут записаны первый, средний и последний элемент двух переменных. Вывод: "AJrpan".

# s1 = 'America'
# s2 = 'Japan'

# print(s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1])