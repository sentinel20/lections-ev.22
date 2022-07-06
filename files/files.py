
# Работа с файлами 

# Каретка - указатель
# Hello world

# open(<Путь до вашего файла>)

# file = open('/Users/emilbegaliev/desktop/ev.22/files/files.py') # Абсолюный путь

# file = open('files.py') # Относительный путь

# print(file)

# Режимы для работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))


# file = open('/Users/emilbegaliev/desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()

# file = open('text.txt', 'w')
# file.write('Hello world!\nMy name is John Snow\nI am back-end developer')
# file.close()

# file = open('text.txt', 'a')
# file.write('\nI am 37 years old')
# file.close()


# file = open('text1.txt', 'r')
# file.close

# Контекстный менеджер

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)

# print(file) #Ошибка будет если открыть вне тело

# write
# writelines

# ls = ['Hello world!', 'My name is John!', 'I am 35 years old!']
# with open('text.txt', 'w') as file:
#     file.writelines(line + '\n' for line in ls)

# file.tell() -> возвращает индекс где находится каретка(указатель)

# file.seek(<int>) -> Перемещает каретку (указатель) на указанный int(index)

# --------------------------------------------------------------------------

# from PIL import Image
# import pytesseract
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
#         print(list_of_imei)
#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')    

# list_images = ['imei.jpg']
# get_imei_codes(list_images)        

# a = '1'
# print('111' is a*3)



