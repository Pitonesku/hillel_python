# ДЗ 10.2. Знайти перше слово
# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
# При розв'язанні задачі зверніть увагу на наступні моменти:
#     У рядку можуть зустрічаються крапки та/або коми
#     Рядок може починатися з літери або, наприклад, з пробілу або точки
#     У слові може бути апостроф і він є частиною слова
#     Весь текст може бути представлений лише одним словом та все

# Вхідні параметри: Рядок.
# Вихідні параметри: Рядок.

#VERSION 1
import re

def first_word(text: str) -> str:
    patern = r"\w+'*\w*"
    words = (re.findall(patern, text))
    return words[0]
   


# import string

# def first_word(text: str) -> str:
#     """
#     Find first word in the text
#     """
#     text = (text.strip().split((" ")))
#     print(text)

#     for word in text:
#         if any(char.isalpha() for char in word):
#             first_word = word
#             break
#     first_word = "".join(filter(lambda char: char.isalpha() or char == "'" or char not in string.punctuation, first_word))
#     return first_word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
