# ДЗ 5.2. Модифікувати калькулятор
# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче. 
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного 
# обчислення - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
# import string
 
# symbol_list = str.replace(string.punctuation, "+","").replace("-","").replace(".","")
# operator_list = "+-*/"

# exit = False
# error_msg = ("You innput wrong number, please try again ot type 'exit' to exit")
# print("Please enter the first number:")
# while True:
#     num1 = input("num1 = ")
#     if num1 == "exit":
#         exit = True
#         break
#     if any(_ in num1 for _ in string.ascii_letters) or any(_ in num1 for _ in symbol_list):
#         print(error_msg)
#         continue
#     elif str.count(num1, "+") > 1 or str.count(num1, "-") > 1 or str.count(num1, ".") > 1:
#         print(error_msg)
#         continue
#     elif "+" in num1 and str.index(num1,"+") > 0 or "-" in num1 and str.index(num1,"-") > 0:
#         print(error_msg)
#         continue
#     num1 = float(num1)
#     print(num1)
#     print("Please enter second number or type 'exit' to exit")
#     break


# while True:
#     if exit == True:
#         break
#     else: num2 = input("num2 = ")

#     if num2 == "exit":
#         exit = True
#         break
#     elif any(_ in num2 for  _ in string.ascii_letters) or any(_ in num2 for _ in symbol_list):
#         print(error_msg)
#         continue
#     elif str.count(num2,".") > 1:
#         print(error_msg)
#         continue
#     elif "+" in num2 and (str.count(num2, "+") > 1 or str.index(num2,"+") > 0):
#         print(error_msg)
#         continue
#     elif "-" in num2 and (str.count(num2,"-") > 1 or str.index(num2,"-") > 0):
#         print(error_msg)
#         continue
#     num2 = float(num2)
#     print("Enter operator: +, -, *, /, or type 'exit' to exit")
#     break


# while True:
#     if exit == True:
#         break
#     else: operator = input("operator: ")
#     if operator == "exit":
#         break
#     elif operator in operator_list: 
#         match operator:
#             case "-": result = num1 - num2
#             case "+": result = num1 + num2
#             case "*": result = num1 * num2
#             case "/": 
#                 if num2 == 0:
#                     print("ERROR. Cannot dived by ZERO")
#                     break
#                 result = num1 / num2
#         print(f"Result: {num1} {operator} {num2} = {result:.445f}")
#         break
#     else: print("Enter valid operator, or type 'exit' to exit")
# if exit == True:
#     print("Thanks")

