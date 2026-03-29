def calculator(num1, num2, operation):
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція у вигляді рядка:
        - 'add' для додавання (+)
        - 'subtract' для віднімання (-)
        - 'multiply' для множення (*)
        - 'divide' для ділення (/)
    :return: Результат операції.
    """
#     if operation not in ["add", "subtract", "multiply", "divide"]:
#         result = 0
#     else:
#         match operation:
#             case "add": result = num1 + num2
#             case "subtract": result = num1 - num2
#             case "multiply": result = num1 - num2
#             case "divide": result = "error" if num2 ==0 else num1 / num2

#     return result

# print(calculator(2,7,"substract"))
#     # Ваш код тут

numbers = [1, 2, 3, 4, 5]
# def multiply_even_numbers(numbers):
#     """
#     Помножує всі парні числа у списку на 2.

#     :param numbers: Список чисел.
#     :return: Новий список з парними числами, помноженими на 2.
#     """
#     result = list(map(lambda num: num *2, filter(lambda num: num % 2 == 0, numbers)))
    
#     return result


# #Перевірка
# assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]

# print(multiply_even_numbers(numbers))

#def square_numbers(numbers):
#     """
#     Замінює кожне число у списку його квадратом.

#     :param numbers: Список чисел.
#     :return: Новий список з квадратами чисел.
#     """
#     result = []
#     result = list(map(lambda num: num*num, numbers))
#     return result

# print(square_numbers)

# # Перевірка
# assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
# assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
# assert square_numbers([]) == []

def factorial(num):
    """
    Обчислює факторіал числа num.

    :param n: Ціле число.
    :return: Факторіал числа num.
    """
    result = 1
    if num == 1 or num == 0:
        return result
    else:
        result = result * num
        num -=1
    return result * factorial(num)
    

  
    

print(factorial(0))
# Перевірка
#assert factorial(5) == 120