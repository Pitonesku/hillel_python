# ДЗ 8.1. Додати 1 до числа
# Ваше завдання — написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом. До нього необхідно додати 1.
# Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму, знову розбити на список із цифр.
# В результаті функція повертає список із цифр, що становлять значення суми.
# Так зі списку з цифрами [1, 2, 3, 4], має вийти число 1234. До нього додаємо 1, і отримуємо 1235. 
# Після цього потрібно розбити отримане число на складові цифри. У результаті має бути список [1, 2, 3, 5], який повертає функція.


#Version 1
nums = [9, "t", 9]
nums1 = [1, 2, "h", 0, 2]

def add_one(nums : list[int] ):
  if all(isinstance(num, int) for num in nums):
    number = str()
    for _ in nums:
      number = number + str(_)
    number = str(int(number) +1)
    number_lst = list()
    for _ in number:
      number_lst.append(int(_))
    return number_lst
  else: 
    raise Exception ("Only INT accepted") #????


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 

try:
    print(add_one(nums))
except Exception:
   print("error")


#Version 2
#      
def add_one(nums : list[int]):
    try:
        nums =str(int("".join(map(str,nums)))+1)
        nums = list(nums)
        nums = list(map(int, nums))
        return nums
    except Exception:
       print("wrong input")


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1' 
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2' 
assert add_one([0]) == [1], 'Test3' 
assert add_one([9]) == [1, 0], 'Test4' 

print(add_one(nums1))