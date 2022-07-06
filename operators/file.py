
# Task #5
# a = int(input(3))
# b = int(input(7))
# if a<b:
#     print(a)
# else:
#     print(b)

# Task #6
# a = 7
# b = 9
# c = 5
# if a <= b and a <= c:
#     print(a)
# if b <= a and  b <= c:
#     print(b)
# if c <= b and  c <= a:
#     print(c)

# Task #7
# a = 6
# b = 5
# c = 9

# if a == b == c:
#     print(3)
# elif a == b or b ==c or c == a:
#     print(2)
# else:
#     print(0)        
    
# Task #8
# a = 678
# b = 23

# if a % b == 0:
#     print('%d Делится %d' % (a,b))
# else:
#     print('%d Не делится на %d' % (a,b))
#     print('Остаток: %d' % (a%b))
# print('Частное: %d' % (a//b))        

# ????????
# n = int(input(10))
# c = input("Перевести в байты (b) or килобайты (k): ")
# if c == 'b':
#     print("%dКб = %d байт" % (n, n*1024))
# elif c == 'k':
#     print("%d байт = %.2fКб" % (n, n/1024))


# 12.Объявите переменную count, значение которой равно 0. 
# Затем, запросите у пользователя ввод целого числа. 
# Проверьте строку, введённую пользователем. 
# Если он ввёл число, то преобразуйте данную строку в число и запишите результат в count. 
# Распечатайте значение count. Например: "0" -> count = 0, "5" -> count = 5, 10 -> count = 10.

# count = 0
# number = input('Введите целое число: ')

# if number.isdigit():
#     count = int(number)
#     print(count)
#     print(type(count))
# else:
#     print('0')    


# text = 'Hello world'
# result = text.count()
# print(result)

# from datetime import datetime
# from datetime import 

# date = seco(input())
# d = date.datetime()
# print(d)


# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
 
# print("Значение этого элемента:", fib2)


# fib1 = fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n) - 2
 
# while n > 0:
#     fib1, fib2 = fib2, fib1 + fib2
#     n -= 1
 
# print("Значение этого элемента:", fib2)