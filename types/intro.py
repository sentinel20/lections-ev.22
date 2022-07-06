# -*- coding: utf-8 -*- 
# # # типы данных в питоне




















# 1. NoneType
# 2. boolem
# 3. int (), float (), complex ()
# 4. str ()
# 5. range ()
# 6. tuple ()
# # ******************************************************
# '''стандартный вывод данных'''
# "" в пайтоне для вывода данных в терминале используется функция print ()""
# print("hello world") 
# '''стандартный вывод данных через терминал используется функция input'''
# input () 
# a = input ('Введите число')
# print (a)
# type() выводит тип данных
# print (type(a))

# b = int (input ('введите число номер2:'))
# print (b)
# print (type(b))

# print(input('asd'))
# print(input('asd'))

# a=2
# b=5
# c=7
# print (pow (a,b))

# divmod (a, b) она выводит два числа, первое число это результат целочисленного деления //
#"a" на "b" целое число

# print (divmod (5, 2))
# print (12 / 5)
# print (divmod(12, 5))

# abs() - выводит абсолютное значение числа

# print (abs(-5))
# print (abs(5))

#import math

# a = 25
# print (math.sqrt(a))

# a = 'hello'
# print (a)
# a = 5
# print (a)

# a=40
# b=5
# result (a+b)
# print ('40+5')

# num1 = 10
# num2 = 3
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print('num1 =', num1, 'num2 =', num2)


# a = input().split()
# for i in range(0, len(a), 2):
#     print(a[i])


# Даны два списка с рандомным набором чисел, объединить эти списки, а затем вывести сумму всех чисел

# from random import randint

# ls1 = [randint(1,20) for in range(10)]
# ls2 = [randint(1,20) for in range(10)]
# print(ls1)
# print(ls2)

# from random import randint
 
# a1 = [randint(1, 20) for _ in range(10)]
# a2 = [randint(1, 20) for _ in range(10)]
# print(a1)
# print(a2)
# print(sum((a1) + (a2)))



# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# suitcase = []
# suitcase.append('towels, sunglasses, shorts, cap, cream')
# print(suitcase)
# suitcase.append('towels, sunglasses, shorts, cap, cream')
# # item = suitcase.pop()
# # print(item)
# # print(suitcase.append)
# # t = suitcase.index('cream')
# print(suitcase)