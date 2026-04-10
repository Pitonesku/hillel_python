# ДЗ 12.3. Перевірка на парність.
# Завдання ускладнюється.
# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне, 
# або False якщо число непарне, але при цьому 
# НЕ МОЖНА використовувати ділення у функції, та дії пов'язані з ним. 
# Тобто. заборонено використовувати /, //, % та divmod
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа :)
# Вхідні дані: Ціле число.
# Вихідні дані: True або False

    #VERSION 1
# def is_even(num:int) -> bool:
#     last_digit = int(str(num)[-1])
#     if any([last_digit == 0, last_digit == 2, last_digit == 4, last_digit == 6, last_digit == 6 ]):
#         return True
#     else: 
#         return False

    #VERSION 2
def is_even(num:int) -> bool:
    flag = False
    last_digit = int(str(num)[-1])
    flag = True if last_digit in (0,2,4,6,8) else False
    return flag

    # if last_digit in range(0,10,2):
    #     return True
    # else: 
    #     return False
    
    

print(is_even(2321))