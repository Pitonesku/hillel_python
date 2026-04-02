# ДЗ 10.1. Генераторна функція
# Реалізуйте генераторну функцію (з використанням оператора yield), яка повертатиме по одному члену числової послідовності, 
# закон якої задається за допомогою функції користувача. 
# Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовності (n). 
# Генератор повинен зупинити свою роботу з досягнення n-го члена.
# Підказка: це завдання дуже схоже на нескінченний лічильник з матеріалів лекції! Потрібно лише обмежити кількість видаваних генератором значень!

from inspect import isgenerator

def pow(x):
    return x**2

def my_generator(start: int, qty: int, func):
    
    """
    Generate list of numbers based on desired function
    """
    i = 0 
    while i < qty:
        result = start
        start = func(start)
        i+=1
        yield result


gen = my_generator(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')


