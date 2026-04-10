# ДЗ 12.2. Заповнення списку кубами чисел
# Напишіть функцію-генератор generate_cube_numbers, яка формує набір кубів чисел, 
# починаючи з числа 2 до вказаної Вами величини. Тобто. генератор повинен працювати доти, 
# поки генерується значення менше зазначеної величини.
# Нагадую, що вийти із генератора можна за допомогою return без параметрів.

# NON GENERATOR
# def generate_cube_numbers(n:int) -> list[int]:
#     """
#     Generate list with number^3, till number^3 < n
#     """
#     cube_list =[]
#     for num in range (n):
#         if num**3 < n:
#             cube_num = num**3
#             cube_list.append(cube_num)
#         else:
#             break
#     return cube_list

# GENERATOR VERSION 1
# def generate_cube_numbers(n:int):
#     """
#     Generate list with number^3, till number^3 < n
#     """
#     for num in range (2,n):
#         if num**3 <= n:
#             cube_num = num**3
#             yield cube_num
#         else:
#             break

# VERSION 2   
# def generate_cube_numbers(n:int):
#     yield from map(lambda x: x**3, (filter(lambda x: (x**3 <= n ), range(2,n))))

# VERSION 3   
def generate_cube_numbers(n:int):
    i = 2
    while i**3 <= n:
        yield i**3
        i+=1
  
  


from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'



#print(generate_cube_numbers(30))

# print(list(filter(lambda x: (x**3 < 100 ), range(100))))