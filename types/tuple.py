
# Tuple - это структура данных, неизменяемый, индексируемый, упорядочный

# string1 = str('Hello world')
# string2 = 'Hello world'
# list1 = list(i for i in range(5))
# list2 = [1, 2, 3, 4, 5]
# set = {1,2}
# dic1 = {'key': 'value'}

# tuple1 = (1, 2, 3)
# print(type(tuple1))

# list1 = [1,2]
# list1[0] = 3
# print(list1)

# tuple1 = 1,2
# tuple1[0]= 3
# print(tuple1[0])

# print(tuple1[0])
# print(type(tuple1))

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))

# emails1 = ['Python@gmail.com', 'Tima@mail.ru']

# emails = ('Python@gmail.com', 'Tima@mail.ru', 3, 5, ['potato', 'arbuz', 'apple'])

# print(emails[-1])
# print(type(emails[-1]))
# last_object = emails[-1]

# last_object.append('Tomato')
# print(len(emails))

# print(dir(tuple))

# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first
# print(tuple_sequance.count(1))

# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first
# print(tuple_sequance)
# index = tuple_sequance.index(3)
# print(tuple_sequance.index(3))

# ЦИКЛЫ
# for value in tuple_sequance:
#     print(value)

# names = ('Tima', 'Zhanylai', 'Aidana', 'Bermet', 'ermek')

# names_enter = ['Bermet', 'Ermek']
# for name in names:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!')
#     else:
#         print(f'{name} go home!!!')    

# for name in names:
#     print(f'hello {name}!!')
#     print('it is len: ', len(name))

# names = ('Tima', 'Zhanylai', 'Aidana', 'Bermet', 'ermek')
# for name in names:
#     print(f'hello {name.capitalize()}!!')
      
# print(names[0] + ' Hello!')

# first_step_names = []
# names = input('Enter names: ').split(' ')
# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)
        
# print(first_step_names)

# print('start for')
# for i in range(10):
#     print(i)
# print('stop for')    

# while 3 > 2:
#     print(f' {1} i work')
#     i +=1

# i = 0
# num = 3
# while num > i:
#     print('i work')
#     i += 1


# tries = 3
# while tries:
#     print('>>> ', end='')
#     command = input()
#     if not command:
#         continue
#     if command in ('echo', 'cd', 'help'):
#         break
#     print('Unknown command!')
#     tries -= 1
# else:
#     print('Too many bad tries!')
#     command = None

# a = input()
 
# even = 0
# odd = 0
 
# for i in a:
#     if int(i) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
 
# print("Even: %d, odd: %d" % (even, odd))

# a = [2,4,5,6,7,8,9]
# a = int()
# k = 1
# for i in range (a+1):
#     k = k*i
 
# print (k)

# n = int(input())
 
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
 
# print(factorial)

# a = int(input())
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)

# a = int(input())

# A1 = range[90,100]
# B1 = ('80','89')
# C1 = ('70','79')

# if a == (A1):
#     print('A')