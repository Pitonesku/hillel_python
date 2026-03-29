# ДЗ 9.1. Визначити популярність певних слів у тексті
# На вхід функції popular_words передаються два аргументи. 
# Текст та список слів, популярність яких необхідно визначити.
# При вирішенні цього завдання зверніть увагу на такі моменти
# Слова необхідно шукати у всіх регістрах. Тобто. 
# якщо необхідно знайти слово "one", значить для нього будуть підходити 
# слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
# Вхідні параметри: Текст і масив слів, що шукаються.
# Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями, 
# скільки разів кожнє слово зустрічаються у орігінальному тексті.

text = "When I was One I had just begun When I was Two I was nearly new "
looking_words_list = ['i', 'was', 'three', 'near']

# VERSION 1
# def popular_words(text: str, looking_words_list: list[str] ) -> dict:
#     text = text.strip().lower().split()
#     freq = 0
#     freq_list=[]
#     for looking_word in looking_words_list:
#         freq = len(list((filter(lambda word : word == looking_word in looking_words_list, text))))
#         freq_list.append(freq)
#     return dict(zip(looking_words_list, freq_list))


#VERSION 2
# def popular_words(text: str, looking_words_list: list[str]) -> dict:
#     popular_words = {}
#     text = text.lower().strip().split(" ")
#     for word in looking_words_list:
#         popular_words |= {word:text.count(word)}
#     return popular_words

#VERSION 3

def popular_words(text: str, looking_words_list: list[str]) -> dict:
    return {word: text.strip().lower().split().count(word) for word in looking_words_list}



assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' 


print(popular_words(text, looking_words_list))
