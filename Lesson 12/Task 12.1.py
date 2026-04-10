# ДЗ 12.1. Генератор простих 
# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа. 
# Верхня межа цього діапазону визначається параметром цієї функції.
# Наприклад, виклик функції
# list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7].
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд

def prime_generator(n:int):
    """
    Return all prime digits in range from 2 to n
    """
    # for i in range(n):
    #     filter(lambda i:( i % 2 !=0, i % 3 != 0, i % 5 !=0, i % 7 != 0, i % 2 !=0), range(n))
    i = 2    
    while i <= n:
        if i in (2,3,5,7) or any ([i % 2 !=0, i % 3 != 0, i % 5 !=0, i % 7 != 0]):
            yield i
            i+=1
        else:
            i+=1



                
    
    
    print(list(prime_generator(11)))
