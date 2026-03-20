# ДЗ 6.3. Добуток чисел
# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.

import string

# #Version 1 WORKING
# number = input('Enter the number or type "exit" to exit:\n')
# result = 1

# while len(str(number)) > 1:
#         for num in str(number):
#             num = int(num)
#             result = num*result
#         print(f"{number} -> {result}")
#         number = result
#         result = 1




#Version # 2
result = 1
while True:
      number = input('Enter the number or type "exit" to exit:\n')
      if number == "exit":
            break
      elif not number.isdigit:
            continue
      else:
           while len(str(number)) > 1:
            for num in str(number):
                num = int(num)
                result = num*result
            print(f"{number} -> {result}")
            number = result
            result = 1
            
      break


# NOT WORKING
# number = "232"
# result = 1
# while len(str(number)) > 1:
#     divider = len(str(number))-1
#     num = int(number) // 10**divider
#     number = int(number) - num*10**divider

#     result = num * result
    
# print(result)