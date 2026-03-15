# ДЗ 5.3. hashtag
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.

# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

my_str = input("Enter sentence for hashtag: \n")
my_punctuation_list = string.punctuation + " "
my_str = my_str.title()
for _ in my_str:
    if _ in my_punctuation_list:
        my_str = my_str.replace(_,"")
print("#" + my_str[:139])