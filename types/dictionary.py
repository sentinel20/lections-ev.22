
# dict() - словарь -> это упорядоченная коллекция элементов (python 3.7 -> ordered).
# Каждый элемент в словаре содержится в паре ключ: значение.

# Ключи (key) должны быть уникальными и быть неизменяемым типом данных(str, int, tuple etc).
# Тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }

# print(thisdict)
# print(type(thisdict))

# Hash tables, ассоциативный массив, dictionary, object(JS) == dictionary(py)
# a = {1,2,3,} #set
# some_tuple = 1,2,3,4
# print(type(some_tuple))
# print(some_tuple)

# some_dic = {}
# print(type(some_dic))
# key_values = {'key': 'value', 'key1': 'value1'}
# print(type(key_values))
# dict_created_with_function = dict()
# print(type(dict_created_with_function))

# dict_ = dict((('key', 'value',), ('key2', 'value2')))
# print(dict_)
# print(type(dict_))

# ---------------------------------------------------------------------

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',
#     'list': [1,2,3],
    # [1,2,3]: 'list', #error
    # 'first_name': 'Raychal'
# }
# print(user_info)
# print(type(user_info))
# print(user_info['first_name'])
# print(user_info.get('age'))
# print(dir(user_info))
# print(user_info.items())
# for items in user_info.items():
#     print(items)

# print(user_info.keys()) # before changes


# user_info['hight'] = 185
# print(user_info.keys())  # after changes
# print(user_info)

# Выводит все ключи:

# for key in user_info.keys():
#     print(key)


# Выводит значения ключей:

# for value in user_info.values():
#     print(value)

# pop() -> Удаляет элемент по определенному ключу    
# popitem() -> Удаляет последнюю пару в словаре

# user_info.pop('list')
# user_info.pop('email')
# user_info.popitem()
# user_info.popitem()

# print(user_info)

# setdefault(key, [default value]) -> Работает так же как и метод get(), но если такого ключа не существует, то он создаст новую пару

# Первый способ применения, получение значений:
# dict_ = {'name': 'John', 'age': 23}
# result = dict_.setdefault('age')
# print(result)

# Второй способ применения,добавления пары:
# dict_ = {'name': 'John', 'age': 23}
# result = dict_.setdefault('address', 'Toktogula str.')
# print(dict_)

# print(user_info)
# user_info.update({'first_name': 'Raychel'})
# user_info.update({'hight': 170})

# print(user_info)



# roles = {
#     0: 'Admin',
#     1: 'Moderator',
#     2: 'Customer',
#     3: 'Vendor',
#     4: 'Guest',
# }

# users = [
#     {
#         'id': 0,
#         'name': 'John',
#         'role': roles[0]
#     },
#     {
#         'id': 1,
#         'name': 'Raychel',
#         'role': roles[3]
#     },
#     {
#         'id': 2,
#         'name': 'Aibek',
#         'role': roles[4]
#     },

# ]

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy S20',
#     'discription': 'Lorem Ipsum',
#     'price': 1000
# }

# print(users)
# print(product)

# user_id = int(input('Enter your ID: '))

# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('Vvedite novoe opisanie productu: ')
# else:
#     raise Exception('U vas nedostatochno prav!!')    

# print(product)    

# print(dir(dict))

# print(dir(list))


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {k: v for k, v in a.items() if v}
# print(b)