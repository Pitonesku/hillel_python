# ДЗ 12.1. Генератор простих 
# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа. 
# Верхня межа цього діапазону визначається параметром цієї функції.
# Наприклад, виклик функції
# list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7].
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд

# VERSION 1
# def prime_generator(n:int):
#     """
#     Return all prime digits in range from 2 to n
#     """
#     # i = 2    
#     # while i <= n:
#     #     if i in (2,3,5,7):
#     #         yield i
#     #         i+=1
#     #     elif all ([i % 2 !=0, i % 3 != 0, i % 5 !=0, i % 7 != 0, (i**0.5 % 1) !=0]):
#     #         yield i
#     #         i+=1
#     #     else: i+=1


# VERSION 2

# def prime_generator(n:int):
#     """
#     Return all prime digits in range from 2 to n
#     """
#     yield from filter(lambda i: i in (2,3,5,7) or all([i % 2 !=0, i % 3 != 0, i % 5 !=0, i % 7 != 0, (i**0.5) % 1 !=0]), range(n+1))
    


# Version 3

def prime_generator(n:int):
    
     
     yield from filter(lambda x: x in (2,3,5,7) or all([x % d !=0 for d in range(2,(int(x**0.5) +1))]), range(2,n+1))

    
print(list(prime_generator(29)))        
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
        
print(list(prime_generator(170)))
