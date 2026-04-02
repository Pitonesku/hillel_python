# ДЗ 10.3. Перевірити чи є парним чи ні
# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.

def is_even(num: int) -> bool:
    """
    Checking the number is even or not
    """
    return True if num % 2 == 0 else False


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')