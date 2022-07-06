
# ЦИКЛЫ

# import random 

# ls = ['plov', 'manty', 'kuurdak', 'lagman']

# p = 0
# m = 0
# k = 0
# l = 0

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

# print(f'Plov: {p},\nManty: {m}\nKuurdak: {k},\nlagman: {l}')      

# задача домой запринтить 'выиграл лагман'... 



# 1. list -> четные числа 0=200
# 2. list -> /2/3 0=200
# 3. list -> 1,2*,3,4*,5.... 0=100

# ls1 = []

# if ls1 = ls.index(::2):
#     print(ls1)

# print(dir(list))

# ls = ()

# print(list(range(index[::2]))

# list1 = []
# for i in range(0,200):
#     if i%2 == 0:
#         list1.append(i)

# print(list1)        

# list2 = []

# a = list(range(0,200))

# for i in a:
#     if i%2 == 0 and i%3 == 0:
#         list2.append(i)

# print(list2)        

# ls = []

# for i in range(0,101):
#     if i%2 == 0:
#         ls.append(i**2)
#     elif i%2 != 0:
#         ls.append(i)

# print(ls)

# dict6 = {
#   'a': 1,
#   'b': 4,
#   'c': 1,
#   'd': 5,
#   'e': 6
# }
# for value in dict6.values():
#   if value%2 == 0:
#     print(value)
#   else:
#     print(value)  

# a = [['A',11],['B',12],['C',13],['D',14],['E',15]]
# c = dict(a)
# print(c) 

# -----------------------28.06.2022 (filter, map, lambda, enumerate)-----------------------




# def countingValleys(steps, path):
#     dolina = 0
#     sea_level = 0
#     for x in path:
#         if x == 'U':
#             sea_level += 1
#             if sea_level == 0:
#                 dolina += 1
#         elif x == 'D':
#             sea_level -= 1
#     return dolina            

# print(countingValleys(12, 'DDUUDDUDUUUD'))


# def get_word():
#     vowels = 0
#     consonants = 0
#     for i in word:
#         letter = i.lower()
#         if letter == 'а' or letter == 'е' or letter == 'о' or letter == 'и' or letter == 'у' or letter == 'ы' or letter == 'э' or letter == 'ю':
#             vowels += 1
#         else:
#             consonants += 1
#     return letter  
# word = input()
# print(get_word(f'Vowels %{i}, Consonants % {i}' % ()))

# "Vowels %i\nConsonants %i" % (vowels, consonants)


ff = ['dffgg', 'sfgrigi', 'hbsidb', 'iuyhwifeu']
names = str(ff)
# c = names.split()
# print(c)
res = names.capitalize()
# res1 = ''.join(res)
print(res)

