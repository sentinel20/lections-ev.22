# string - строки

# строки - это набор последовательных символов которые мы используем для хранения и представления текстовой информации

# 'Меня зовут Санжар. Мне 20 лет!' - str()

# name = 'john'
# name1 = "john"
# name2 = '''
# john 
# snow
# '''
# name3 = str('john snow')
# # '''сейчас мы все это выведем в терминал'''
# print(name)
# print(name1)
# print(name2)
# print(name3)

# print (type(name))
# print (type(name1))
# print (type(name2))
# print (type(name3))
# print(type(5))

# Экранирование - механизм при помощи которого можно вставлять символы которые сложно ввести с клавиатуры.

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \f -> перевод страницы
# \r -> возврат указателя (коретки)
# \v -> вертикальная табуляция

# name = 'john\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'
# print(name)
# print(lastName)
# print(last_name)


# name = 'Raychel'
# print(name * 3)
# print(name + 'John')

# Индексация символов в строке
# name = 'John'
# J = 0 = -4
# o = 1 = -3
# h = 2 = -2
# n = 3 = -1

# print(name[0]) 
# print(name[-1]) 
# print(name[2]) 

# Срезы по индексам
# string[start:end:step]
# len() - выводит длину строки
# print(len('Hello world!'))
# name = 'John Snow'
# print(len(name))


# text = 'Hello world! My name is John Snow!'
# print(text[0:5])
# print(text[13:-1])
# print(text[13:])
# print(text[:12])
# print(text[::2])
# print(text[::-1])
# print(text[::-2])
# print(text[:14:-1])

# Конкатенация строк (слияние, соединение)
# word1 = 'Hello'
# word2 = 'world'
# probel = ' '

# result = word1 + probel + word2
# print(result)
# print(word1 + probel + word2 +'!!!')
# print(word1, probel, word2, '!!!')
# strl = word1 + word2 + probel
# print (type(strl))

# Форматирование строк
# 1. способ с помощью %
# 2. способ с помощью .format()
# 3. интерполяция строк (f-строки)

# %
# name = input('Enter your name:')
# last_name = input('Enter your last name: ')
# print('Hello, mr/mrs %s %s' %(name, last_name))

# .format
# name = input('Enter your name:')
# last_name = input('Enter your last name: ')
# print('Hello, mr/mrs {} {}'.format(name, last_name))

# f-строки
# name = input('Enter your name:')
# last_name = input('Enter your last name: ')
# print(f'hello, mr/mrs {name} {last_name}')
# print('Hello, mr/mrs ' + name, last_name)
# print('Hello, mr/mrs ' + name + ' ' + last_name)