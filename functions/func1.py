
# def <name_of_function>(<a, b>#параметры):
#     <body> #некий код, некая логика
#     <return> #возвращает что-то

# <name_of_function>(<5, 6> #аргумент)  

# Параметры функции - переменные, которые будет принимать наша функция, для того чтобы мы смогли работать
# с данными, которые передаются в эту функцию
  
#   Аргументы - это данные, которые мы передаем для параметров при вызове функций

# return нужен для того чтобы функция что то возвращала и для того чтобы мы могли работать с результатом
# действий функций.
# return является не обязательным оператором (взвращает None - если не указать return)

# ls = []
# result = ls.append(1)
# print(ls)
# print('результат действия:', result)

# result1 = ls.pop()
# print(ls)
# print('результат действия:', result1)

# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     return result

# print(sumTwoNums(5, 5)) #аргументы

# def isEven(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False    
  
# a = 10
# b = int(input('Enter num: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b)) 

# def isEven1(num: int)  -> bool:
#     '''
#     Наша функция проверяет является ли число, типа int, четным.
#     '''
#     if num % 2 == 0:
#         return True
#     return False    

# isEven()
# isEven1()

# def get_polindrom(words: list) -> list:
#     '''Функция возвращяет из полиндрома'''
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result

# some_words = ['John', 'Ono','Peter', 'Anna', 'Dovod', 'apa', 'Juice', 'tenet', 'piko']
# print(get_polindrom(some_words))    


# def func():
#     print('Hello World!')

# func()

#----------------------------------

# default parameters

# def print_welcome(name:str = 'User') -> str:
#     print(f'Welcome, {name}!')

# print_welcome()

'''Напишите функцию, которая будет возвращать ваш депозит через определенное время с процентом 10%, 
возвращать финальное количество денег. Срок 3 года, сумма 30000 сом'''

# from logging import raiseExceptions


# def get_percentage(money:float, period:int) -> float:
#     '''Return final amount money!'''
#     if money < 30000:
#         raiseExceptions('Вы ввели недостаточное количество денег! Мин сумма 30000 сом')
#     if period < 3:
#         raiseExceptions('Вы ввели недостаточный срок для депозита, мин период 3 года!')    
#     i = 0
#     while i < period:
#         print('1') # Количество итераций
#         money = money + (money * 0.1)
#         i += 1 # i = i + 1
#     return money        

# money = float(input('Введите сумму депозита: '))
# year = int(input('Введите срок депозита: '))
# print(get_percentage(money, year))

# 'Hello world! My name is John Snow, last name is Snow. Nice to meet you!'

# def get_reverse_string(text: str) -> str:
#     '''return reversed string'''
#     print(text) # показывает что в тексте хранится
#     spisok = text.split(' ')
#     print(spisok[::-1]) # показывает что в списке происходит
#     result = ' '.join(spisok[::-1])
#     print(result)
#     return result
# get_reverse_string('Hello world! My name is John Snow, last name is Snow. Nice to meet you!')    