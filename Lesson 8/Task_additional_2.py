# import math

# def find_gcd(a, b):
#     if a == b:
#         return a
#     if max(a,b)%min(a,b) == 0:
#        return min(a,b)
#     else: 
#         return find_gcd(min(a,b),max(a,b)%(min(a,b)))


 

    
# def find_gcd(a, b):
#     if b == 0:
#         return a
#     return find_gcd(b, a % b)

# print(find_gcd(7,11))   

# Задача. Перевернути Слова у Рядку

# sentence = "    Hello my friend"
# def reverse_words(sentence):
#     """
#     Напишіть функцію reverse_words, 
#     яка приймає рядок та повертає його, де кожне слово перевернуто, а порядок слів збережено.
#     """
#     reversed_sentence = " ".join(map(lambda word: word[::-1],sentence.strip().split(" ")))
#     print(reversed_sentence)
    
     
# #     return (" ".join((sentence[:sentence.find(" ")])[::-1]),sentence.find)

# reverse_words(sentence)


# Additional 3

# ﻿Напишіть функцію sum_of_digits, яка приймає ціле число та повертає суму його цифр.

number = -9876


def sum_of_digits(number):
       result = 0
       number = str(number)
       number_list =list(map(lambda digit: int(digit), list(digit for digit in number if str.isnumeric(digit) )))
       for digit  in number_list:
              result = result + digit 

       return result
print(sum_of_digits(number)) 



