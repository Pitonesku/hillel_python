# ДЗ 8.2. Паліандром
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
import string
text = "ass.A"

def is_palindrome(text: str) -> bool:
    """
    Проверяет является ли строка палиндромом.
    Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
   
    """
    my_punctuation = string.punctuation + " "
    text = text.lower()
    for _ in text:
        if _ in my_punctuation:
            text = text.replace(_, "")
    text_reversed = text[::-1]
    return text == text_reversed

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4'

print(is_palindrome(text))
    

