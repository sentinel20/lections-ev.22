
# types = (str, int, float, list, tuple)


# for value in types:
#     print(value, True if '_iter_' in dir(value) else False)
    # print(value)
    

# name_lists = ['Ermek', 'Aidana', 'Tima', 'Bermet', 'Zhanylai']    

# for name in name_lists:
#     if name.lower() == 'aidana':
#         continue
#     print(f'Hi {name}!')

# name_lists.append('Ramazan')
# for name in name_lists:
#     if name == 'Ramazan':
#         break
# print(f'Hi {name}!')

# sred = len(name_lists) // 2
# name_lists.insert(sred,'Ramazan')
# for name in name_lists:
#     if name == 'Ramazan':
#         break
    # print(f'Hi {name}!')

# a = bool(23)
# while a:
#     if input('enter message: ') in 'war drugs black'.split():
#         print('Your BLOCK!!')
#         break

# 1) input(Email)  2) Show Email
# test@test.com  test@mail.ru  Testgmail.ru

# CRUD - Create Read Update Delete

# DB_EMAILS = []

# while True:
#     print(' 1) Input Email  2) Show db_emails 3) Delete email in DB 4) stop While, 5) rename email')
#     choices = int(input('enter choice'))
#     if choices == 1:
#         email = input('enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAILS:
#                 print('email уже существует!!')
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         print('invalid email, only GMAIL.COM!!!')    
#     elif choices == 2:
#         print(DB_EMAILS)
#     elif choices == 3:
#         email = input('enter email: ')
#         if email in DB_EMAILS:
#             # index = DB_EMAILS.index(email)
#             # DB_EMAILS.pop(index) 
#             DB_EMAILS.remove(email)
#         else:
#             print (f' {email} не существует!!!')
#     elif choices == 4:
#         break 
#     elif choices == 5:
#         old_email = input('Enter email: ')
#         if old_email in DB_EMAILS:
#             new_email = input('enter new email: ')
#             if email.endswith('@gmail.com'):
#                 DB_EMAILS.remove(old_email)
#                 DB_EMAILS.append(new_email)
                     
#     else:
#         print('Error !!!')      
  
# ПРОВЕРКА ОПЕРАТОРОВ continue И break в ЦИКЛАХ WHILE и FOR
# for i in range (5):
#     if i == 3:
#         continue
#     print(i)

