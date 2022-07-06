
# 1. list -> четные числа 0=200

# list1 = []
# for i in range(0,200):
#     if i%2 == 0:
#         list1.append(i)

# print(list1)        

# 2. list -> /2/3 0=200

# list2 = []

# a = list(range(0,200))

# for i in a:
#     if i%2 == 0 and i%3 == 0:
#         list2.append(i)

# print(list2)        

# ls = [x for x in range(0,200) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# 3. list -> 1,2*,3,4*,5.... 0=100

# ls = []

# for i in range(0,101):
#     if i%2 == 0:
#         ls.append(i**2)
#     elif i%2 != 0:
#         ls.append(i)

# print(ls)

# ls = [x**2 if x%2==0 else x for x in range(0,100)]
# print(ls)

#--------------------------------------------

# LIST_COMPREHENSIONS -> ГЕНЕРАТОР СПИСКА
# 
# newlist = [expression for item in iterable <if condition==True>]

# list-comprehension -> это упращенный подход к созданию списка, который задействует цикл for, а также конструкции if-else для 
# определения того, что в итоге окажется добавлено в наш список.

# ls = []
# for i in range(0,100,2):
#     ls.append(i)
# print(ls)    

# new_list = [i for i in range(0,100,2)]
# print(new_list)

# ls = [i**2 for i in range(0,11)]
# print(ls)


# fruits = ['apple', 'banan', 'kiwi', 'mango', 'limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if x == 'cherry']
# print(ls)

# ls = [x for x in fruits if x != 'apple']
# print(ls)

# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# ls = [1,2,3,4,5,6,7,8,9]
# ls = []
# for inner_list in list_:
#     for num in inner_list:
#         ls.append(num)
# print(ls)        

# ls = [x for inner_list in list_ for x in inner_list]
# print(ls)

# import datetime

# start = datetime.datetime.now()
# ls = [x for x in range(1,100000000)]
# ls = []
# for x in range(1,100000000):
#     ls.append(x)
# finish = datetime.datetime.now()
# print(finish-start)


# ls = [x+10 if x == 8 else x + 1 for x in range(0,10)]
# print(ls)