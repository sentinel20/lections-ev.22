
# list()(список, массив) - изменяемый, последовательный тип данных, который из себя 
# представляет коллекцию каких-либо объектов.

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# 1. -> list(<iterable>)
# my_list = list('Hello world')
# print(my_list)

# tuple = ('banana', 'apple', 'cherry')
# print(tuple)
# print(type(tuple))
# my_list = list(tuple)
# print(my_list)
# print(type(my_list))

# 2. range() -> возвращает последовательность элементов (числа)

# a = range(15)
# a = list(range(0, 100, 2))
# print(a)

# 3. -> []

# my_list = [1, 23, 4, 56, 89]
# print(my_list)

# print(dir(list))

# append(element) - Добавляет element в конец списка

# list_ = [1, 2, 3]
# print(list_)
# list_.append(5)
# print(list_)

# list_ = [1, 2, 3]
# print(list_)
# list_.append(5)
# list_.append([1, 2, 3])
# print(list_)

# extend(element[iterable]) -> расширяет список добавляя element в конец.

# list_ = [1,2,3]
# list_.extend([1,2,3])
# print(list_)

# from operator import index

# insert(<index>, <element>) -> добавляет element по указанному index

# list_ = ['string', 2, 3, False]
# list_.insert(1, [1, 2, 3])
# print(list_)

# list_ = ['string', 2, 3, False]
# list_.insert(1, [1, 2, 3, None])
# list_.insert(2, 1)
# print(list_)
# print(list_[5])
# print(list_[1][3])
# print(list_[2:5])
# print(len(list_))

# index(element, [start], [end]) -> возвращает индекс elementa

# ls = [1, 2, 33, 3, 4, 5, 5, 7, 2, 'hello']
# print(ls.index(1,4))

# if 'hello' in ls:
#     print(f'"hello" is in list:{ls.index("hello")}')

# count(element) -> возвращает количество вхождений element в списке

# ls = [1, 2, 3, 4, 5, 5, 5, 5, 1]
# result = ls.count(1)
# print(result)

# remove(element) -> Удаляет element, но если такого elementa нет в списке, то выводит ошибку

# pop([index]) -> удаляет и возвращает элемент по index, 
# но если index не указан, то удаляет последний element 

# list_ = [5, 1, 2, 3, 4, 5]
# list_.remove(5)
# list_.remove(5)
# deleted = list_.pop(0)
# d = list_.remove(4)
# print(list_)
# list_.pop(0)
# print(deleted)
# print(d)

# sort([reverse=True/False], [key=<>]) -> сортирует список. 
# Если в аргументах передан reverse=True то список будет отсортирован в убывающем порядке.

# ls = [5, 0, -2, -101, 102, 23, 1]
# print(ls)
# ls.sort()
# ls.sort(reverse=True)
# print(ls)

# ls = ['hello', 'john', 'London', 'a']
# ls.sort()  #1-var 
# ls.sort(key=len, reverse=True)   #2-var
# print(ls)

# ls = [1, 'h', 3]
# ls[1] = 2
# print(ls)
# del ls[-1]
# print(ls)

# ls.reverse()
# print(ls)

# TASKS

# s = input()
# print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

# l = list([12939447893])
# print(l)

# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# if 86 in list_:
#     print(f'86 is in list_:{list_.index(86)}')

# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# if 86 in list_:
#     print(f'86 is in list_:{list_.index(86)}')
# list_.remove(1546.89)
# print(list_)