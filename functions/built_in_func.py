
# Встроенные функции

# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() etc.

# map()
# filter()
# lambda()
# enumerate()

# Анонимные функции - lambda(такие же функции только без названия)
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращает только одно выражение


# def sum_args(a, b):
#     result = a + b
#     return result
# def sum_args1(a, b): return a + b    

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_arg = lambda a, b: a + b
# print(sum_arg(1, 2))


# x = lambda a, b, c: a + b + c
# print(x(5, 6, 7))


# def myFunc(n):
#     return lambda a: a * n

# mydoubler = myFunc(2)
# mytripler = myFunc(3)
# print(mydoubler(11))
# print(mydoubler(22))
# print(mytripler(11))
# print(mytripler(22))


# ls = ['def', 'Ivan', 'John', '', ' ']

# new_list = sorted(ls, key=len)
# print(new_list)

# import random 

# ls = ['plov', 'manty', 'kuurdak', 'lagman', 'dymdama']

# p = 0
# m = 0
# k = 0
# l = 0
# d = 0

# for i in range(0, 10000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p = p + 1  # p += 1 инкремент
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k += 1    
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'dymdama':
#         d += 1    

# print(f'Plov: {p},\nManty: {m}\nKuurdak: {k},\nlagman: {l}')   

# dict_ = {'plov': p, 'manty': m, 'kuurdak': k, 'lagman': l, 'dymdama': d}
# print(dict_)
# result = sorted(dict_.items(), key=lambda x: x[1])
# winner = result[-1]
# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]}')

# ---------------------------------------------------------------------


# map(function, Iterable) -> применяет функцию к каждому элементу последовательности и возвращает mapobject(итератор) с результатми.

# Например, с помощью map можно выполнять преобразование элементов. Перевести все строки в верхний регистр:

# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)

# result2 = list(map(len, list_of_words))
# print(result2)

# ls = [1, 2, 3, 4, 5]
# result = list(map(int, ls))
# print(result)

# names = ['John', 'Jamie', 'Sansa', 'Tirion', 'Aibek']
# ['Hello mr/mrs', 'Hello mr/mrs Jamie'....]

# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)

# nums = [1, 2, 3, 4, 5]
# num2 = [100, 200, 300, 400, 500]
# 100, 400, 900, 1600, 2500
# result = list(map(lambda x, y: x * y, nums, num2))
# print(result)

# dict_ = {
#     1: 2,
#     3: 4,
#     5: 6
# }
# {1: '2', 3: '4', 5: '6'}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)

# --------------------------------------------------------------------



# filter (function, Iterable) - применяет функции ко всем элементам iterable функцию, которую мы передаем и возвращает filterobject(итератор)
# с теми объектами, для которых функция вернула True.

# list_of_str = ['one', 'two', 'list', '', '100', '1', '50', 'John99']
# result = filter(str.isdigit, list_of_str)
# print(result)
# for x in result:
#     print(x)



# ls = [10, 11, 102, 213, 314, 515]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)


# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22', 'ono']
# result = list(filter(lambda x: len(x) >= 4, list_of_words))
# print(result)

# ---------------------------------------------------------------


# enumerate(Iterable) -> 

# ls = ['str1', 'str2', 'str3']
# i = 0
# for x in ls:
#     print(f'element: {x}, index: {i}')
#     i += 1

# for i, x in enumerate(ls):
#      print(f'element: {x}, index: {i}')

# new_list = list(enumerate(ls))
# print(new_list)

# ----------------------------------------------------------------

# zip(iterables) - она соединяет каждый объект итерируемых элементов между собой в тип данных tuple и возвращает это.

# list1 = [1, 2, 3]
# list2 = [100, 200, 300]

# result = list(zip(list1, list2))
# print(result)

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200, 300]

# result = list(zip(a, b, c))
# print(result)

# zip для создания словарей

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Blode Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
# dict_r1 = dict(zip(d_keys, d_values))
# print(dict_r1)



# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1': ['london_r1', '21 New Blode Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['london_r2', '21 New Blode Walk', 'Cisco', '4451', '15.4', '10.255.0.2'],
#     'sw1': ['london_sw1', '21 New Blode Walk', 'Cisco', '3850', '3.6.XE', '10.255.0.101']
# }
# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)    

# --------------------------------------------------------------------

# all и any
# all -> возвращает True, если все элементы объекта истина (или объект пустой)

# ls = [[1, 2], 1, 'stroka', True]
# print(all(ls))

# ip = '10.255.0.0.1'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает True, если хотя бы один элемент истинный

# ls = [0, 1, '', False]
# print(any(ls))

# def ignore_command(command):
#     '''Функция проверяет если в команде слово из списка ignore. True - если есть, False - если нет такого слова'''
#     ignore = ['rm-rf', 'alias', 'reset']
#     for word in ignore:
#         if word in command:
#             return True
#     return False

# print(ignore_command('sudo root user'))            

# command = 'sudo alias configurations'
# if ignore_command(command):
#     raise Exception('Invalid command')

# print('Vse Ok')    





# ignore = ['rm-rf', 'alias', 'reset']
# command = 'sudo nano configurations'

# if any([word in command for word in ignore]):
#     raise Exception('Invalid command')

# print('Vse Ok') 

# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# q_pass = int(input('Vvedite kolichestvo paroley: '))
# result = ({
#     f(choices(ascii_letters, k=10), choices (digits, k=5)) for f in repeat(lambda x, y: ''.join(set((x + y))),q_pass)
# })
# print(result)
# print(f'Количество паролей: {len(result)}')

# from statistics import mean

# dlina = {len(x) for x in result}
# print(f'Средняя длина пароля: {mean(dlina)}')


# dc = {'Мурат': 24,'Эржан': 21,'Чынгыз': 24,'Алтынай': 17,'Асема': 16}

# 'daniel', 'mark', 'jessica', 'abigale', 'morgan'
# ls = input()
# ls.capitalize()
# print(ls)















