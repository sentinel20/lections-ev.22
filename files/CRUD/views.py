
# import json
# import random

# FILE_PATH = 'data.json'

# def get_data():
#     with open(FILE_PATH) as file:
#         return json.load(file)

# def list_of_products():
#     data = get_data()
#     return data

# def retrieve_product():
#     data = get_data()
#     # print(data)
#     id = int(input('Vvedite id producta: '))
#     product = list(filter(lambda x: x['id'] == id, data))
#     return product[0]
# # print(retrieve_product())
# def get_id():
#     with open('id.txt', 'r') as file:
#         id = int(file.read())
#         # print(id)
#         # print(type(id))
#         id += 1
#     with open('id.txt', 'w') as file:
#         file.write(str(id))
#     return id    

# def create_product():
#     data = get_data()
#     product = {
#         'id': get_id(),
#         'title': input('Vvedite nazvanie producta: '),
#         'price': float(input('Vvedite price producta: ')),
#         'description': input('Vvedite opisaniye: ')
#     }
#     data.append(product)
#     with open(FILE_PATH, 'w') as file:
#         json.dump(data, file)
#     result = {'msg': 'Created', 'product': product}
#     return result
           
# # print(create_product())

# def update_product():
#     data = get_data()
#     flag = False
#     id = int(input('Vvedite ID producta: '))
#     product = list(filter(lambda x: x['id'] == id, data))
#     if not product:
#         return {'msg': 'Invalid ID! Product does not exist!'}
    
#     index = data.index(product[0])
#     choice = input('Chto izmenit\'?(title-1, price-2, description-3): ')
#     if choice == '1':
#         data[index]['title'] = input('Vvedite novoe nazvanie: ')
#         flag = True
#     elif choice == '2':
#         data[index]['price'] = float(input('Vvedite noviy price: '))
#         flag = True    
#     elif choice == '3':
#         data[index]['description'] = input('Vvedite novoe opisanie: ')
#         flag = True
#     else:
#         print('Invalid choice for update!')
    
#     with open(FILE_PATH, 'w') as file:
#         json.dump(data, file)
            
#     if flag:
#         return {'msg': 'Updated', 'product': data[index]}
#     else:
#         return {'msg': 'Not updated!'}

# def delete_product():
#     data = get_data()
#     id = int(input('Vvedite id producta: '))
#     product = list(filter(lambda x: x['id'] == id, data)) 

#     if not product:
#         return {'msg': 'Invalid ID! Product does not exist!'}

#     index = data.index(product[0])
#     deleted = data.pop(index)
#     json.dump(data, open(FILE_PATH, 'w'))

#     return {'msg': 'Deleted', 'product': deleted}

