# Створіть функцію, яка використовує замикання для підрахунку кількості викликів. 
# Функція повинна приймати іншу функцію як аргумент та повертати нову функцію, 
# яка обгортає передану функцію. Кожен раз, коли обгорнута функція викликається, 
# лічильник має збільшуватися на одиницю.



# def counter(func):
#     counter = 0
#     def inner_counter():
#         nonlocal counter
#         func()
#         counter+=1
#         print(counter)
#     return inner_counter

   



# @counter
# def example_function():
#     print("Inside the function")

# example_function()
# example_function()   
    
# Умова:

# Створіть декоратор, 
# який змінює поведінку функції, додаючи до результату функції число, передане як аргумент декоратору.

# def add_decorator(number):
#     """
#     Реалізує декоратор, який змінює поведінку функції, додаючи до результату функції число.

#     :param number: Число для додавання.
#     :return: Декоратор для додавання числа до результату функції.
#     """
#     def decorator(func):
# 		    # Ваш код
#             def inner(x: int):
#                 result = func(x)+number
#                 return result
#             return inner
#     return decorator



# @add_decorator(5)
# def example_function(x):
#     return x * 2

# # Перевірка
# assert example_function(2) == 9

def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """
    # Ваш код
    def inner_function(func):
        counter = 0
        def count():
            nonlocal counter
            for i in range(repeat_count):
                func()
            counter+=1
            return None
        return count
    return inner_function

@repeat_decorator(1)
def example_function():
    print("hello")

# Перевірка
assert example_function() is None