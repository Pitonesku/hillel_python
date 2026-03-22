# ДЗ 7.1. Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.

import string
def say_hi(name: str, age) -> str:
    return ("Chao") if (name == "exit" or age == "exit") else (f"Hi. My name is {name} and I'm {age} {"years" if int(age) > 1 else "year"} old")


def is_digit (msg : str):
    while True:
        value = input(msg)
        if value.isdigit():
           return value
        elif value == "exit":
            return "exit"
        else: print('Please enter the corect number, or type "exit" to exit')
        


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'

print('ОК')