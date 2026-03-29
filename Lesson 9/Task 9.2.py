# ДЗ 9.2. Різниця між числами

# Є набір чисел (float або int). Вам потрібно знайти різницю між найбільшим (максимум) 
# і найменшим (мінімум) елементом. Ваша функція difference має вміти працювати 
# з невизначеною кількістю аргументів. Якщо аргументів немає, то функція повертає 0 (нуль).
# Якщо з 3-м тестом будуть проблеми, використовуйте функцію округлення round(x, 2), 
# де х це число, яке потрібно округлити.
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).



import random
numbers= [number*int(random.random()*10)*random.choice([-1,1]) for number in range(1,10)]
print(numbers)

#VERSION 1

# def difference(*args: int) -> float:
#     if len(args) < 1:
#         return 0
#     else:
#         minimum = args[0]
#         maximum = args[0]
#         for num in args:
#             if num < minimum:
#                 minimum = num

#         for num in args:
#             if num > maximum:
#                 maximum = num

#     return round((maximum - minimum),2)

# VERSION 2
def difference(*args: int | float) -> int | float:
    if len(args) > 0:
        return round(sorted(args)[-1] - sorted(args)[0],2)
    else: return 0

 
assert difference(1, 2, 3) == 2, 'Test1' 
assert difference(5, -5) == 10, 'Test2' 
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3' 
assert difference() == 0, 'Test4' 
print('OK')    
print(difference(*numbers))
