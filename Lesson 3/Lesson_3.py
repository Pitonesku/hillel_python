#   ДЗ 3.1. Найпростіший калькулятор
#  Програма має виконувати прості математичні дії (+, -, *, /).
#  Користувачеві пропонується почерзі ввести числа та дію над цими числами,
#  а програма, виходячи з дії, обчислює та друкує результат.
# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

print("Simple calculator program")
x = float(input("Enter the first number, x =  "))
y = float(input("Enter the second number, y =  "))
operator = input("Enter the required , +, -, *, /:  ")
match operator:
    case("+"): print(x, "+", y, "=", (x + y)) 
    case("-"): print(x, "-", y, "=", (x - y))
    case("*"): print(x, "*", y, "=", (x * y))
    case("/"): print(x, "/", y, "=",(x / y)) if y != 0 else print("Cannot dived by zero")
    case _: print("You entered unvalid operator")

#add space between the tasks
print("***********************")
print()
    
# ДЗ 3.2. Перемістити елемент у списку
#     Ваша програма має перенести останній елемент списку з кінця на початок, тобто, останній елемент списку має стати першим. Послідовність інших елементів не має змінюватися.
#     Порожній список або список з одним елементом повинен залишитися незмінним.
#     Кількість елементів у списку може бути будь-яким – нуль та більше!

print("Move last element in the list to the first psn")

list = []

# list.append(list.pop(list[7])) что получается при таком коде
print("Original list:", list)
if len(list) > 1:
    list.append(list.pop(0))
    list.insert(0, list.pop(-2))
print("Updated list", list)

#add space between the tasks
print("***********************")
print()
# Var#2

print("Var#2")
print("Original list", list)
if bool(list) != False:
    list.append(list.pop(0))
    list.insert(0,(list.pop(len(list)-2)))
print("Updated list:", list)

#add space between the tasks
print("***********************")
print()

# ДЗ 3.3. Розділити один список на два списки
# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список. 
# Тобто, в результаті повинен вийти список із 2-х списків.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.
# Важливо! Потрібно створити рішення, яке обробляє 3 випадки - список порожній,
# у списку парна кількість елементів і в списку непарна кількість елементів.

print("Original list:", list)
if bool(list) != False:
    half_list_length, is_odd_length = divmod(len(list), 2)
    if is_odd_length == True:
        list = [list[:half_list_length + 1]] + [list[half_list_length + 1:]]
    else: list = [list[0:(half_list_length)], [list[-half_list_length:]]]  
else: list = [list]*2
print("Updated list:", list)


