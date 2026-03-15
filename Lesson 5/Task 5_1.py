# ДЗ 5.1. Ім'я змінної
# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
# Змінна не може:
# - починатися з цифри
# - містити великі літери,
# - пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# - бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# Список зареєстрованих слів можна взяти із keyword.kwlist.
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

import string
import keyword

#   Version 1

# punctuation_list = str.replace(string.punctuation, "_"," ") 
# while True:
#     variable = input("variable name = ")

#     if str.isdigit(variable[0]):
#         print(False)
#         break
#     elif any (_ in variable for _ in string.ascii_uppercase):
#         print(False)
#         break
#     elif any ( _ in variable for _ in punctuation_list):
#         print(False)
#         break
#     elif keyword.iskeyword(variable):
#         print(False)
#         break
#     elif len(variable) > 1 and (str.count(variable, "_") == len(variable)):
#         print(False)
#         break
#     print(True)
#     break


#       Version 2

punctuation_list = str.replace(string.punctuation, "_"," ")
variable = input("variable name = ")

is_valid = not((variable[0] in string.digits) 
            or any(_ in variable for _ in string.ascii_uppercase) 
            or any(_ in variable for _ in punctuation_list) 
            or keyword.iskeyword(variable)
            or (len(variable) > 1 and (variable.count("_") == len(variable))))

print(is_valid)

