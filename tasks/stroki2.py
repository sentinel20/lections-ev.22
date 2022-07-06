
# Методы строк
# dir()- Функция которая вытаскивает методы типов данных
# print(dir(str))

# '<соеденитель>'.join(<массив который нужно соединить>) - соединяет массив из строк 
# по соединителю в одну строку 
# ls = ['milk', 'bread', 'water', 'apple']
# joined = ' '.join(ls)
# print(joined)

# split(разделитель) - Дробит строку по разделителю и возвращает тип данных list.
# text = 'Milk.Bread.Water.Apple'
# splited = text.split('.')
# print(splited)

# joined = ', '.join(splited)
# print(joined)

# replace (<old value>, <new value>, [count]) - Меняет в строке значение old на new
# value, если вы укажите count то он заменит count раз.

# text = "ha ha ha ha ha"
# result = text.replace('ha', 'La')
# print(result)
# print(text)

# strip() - Убирает пробельные символы в начале и в конце строки.

# rstrip() - В конце удаляет
# lstrip() - В начале удаляет

# text = input('Введите ФИО: ')
# result = text.lstrip()
# print(text.strip())
# print(result)

# count('<simbol>') - Считает количество вхождений <simbol> в строку

# text = 'Hello world! I\'m from Earth!'
# result = text.count('l')
# print(result)

# index('<value>', [start], [end]) - Выводит индекс значения value в нашей строке.

# text = 'Hello world! This is Makers!'
# result = text.index('!', 12)
# print(result)
# print(len(text))
# print(text.find('T'))



# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения: <, >, ==(равно), <=, =>, !=(не равно)

# num1 = 18
# num2 = 15
# stroka1 = 'Hello'
# print(ord('H'))
# stroka2 = 'World'
# print(ord('W'))
# result = stroka1 < stroka2
# print(result)
# print(chr(1080))

# bool -- True(1) or False(0)

# Условные операторы
# if
# elif
# else
# if <condition>:
#     если в if приходит True <body if>

# elif <condition>:
#      <body>

# else:
#     <body>

# string = input('Enter smt: ')
# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'Mercedes':
#     print('Mercedes-Benz S class')
# else:
#     print('Совпадений не найдено')


# print('Код закончился') 

# sign up 
# email = input('Enter email: ')
# password1 = input('Enter password: ')
# password2 = input('Enter password confirmation: ')
# if password1 != password2:
#     raise Exception('Password didn\'t match!!!')
# else:
#     print('Successfully sign up!')    


# age = input('Enter your age: ')
# print(type(age))

# if age.isdigit():
#     age = int(age)
# else:
#     print('Введите корректные данные!!')
#     raise Exception('Value error!')    

# if age < 18:
#     print(f'Chuvak prihodi cherez {18-age} goda/let')
# else:
#     print('Vy podhodite po vozrastu!')

# ЛОГИЧЕСКИЕ ОПЕРАТОРЫ
# 1. and -> логическое И
# 2. or -> логическое ИЛИ
# 3. not -> логическое ОТРИЦАНИЕ

# my_age = 20
# your_age = 18
# result = (my_age == 20) and (your_age == 18)
# print(result)

# result = my_age > 18 or your_age == 20
# print(result)

# result = not my_age == 20
# print(result)

# is_user_google_user = True
# is_user_github_user = True
# is_user_age_greater_21 = False
# user_accounts_coins = 8000

# if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins > 5000):
#     print('You can enter the system mr John Snow')
# else:
#     print('Sorry, you couldnt enter!')    



