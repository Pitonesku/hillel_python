# ДЗ 6.1. Діапазон букв
# Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

import string
is_exit = False
to_repeat = False
while True:
        my_range= input('Please enter letters range in the format: letter-letter, e.g. a-g, B-c, B-A" or type "exit" for exit \n')
        if (len(my_range) == 3) and (my_range[0] in string.ascii_letters) and (my_range[1] == "-") and (my_range[2] in string.ascii_letters):
            index_1 = string.ascii_letters.index(my_range[0])
            index_2 = string.ascii_letters.index(my_range[2])
            if index_1 < index_2:
                    print(string.ascii_letters[index_1:index_2+1])
            elif string.ascii_letters.index(my_range[2]) == 0:
                    print(string.ascii_letters[index_1::-1])
            else:  print(string.ascii_letters[index_1:index_2-1:-1])
            break
        elif my_range == "exit":
               print("Chao")
               break
        else: print("Wrong input. Try again") 
   
