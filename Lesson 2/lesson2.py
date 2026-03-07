#Нужно ли отделять знаки арифм операций от переменных и чисел пробелами?

print("Square of the number")
number = float(input("Enter number: "))
print (number,"^2=",number**2, sep='')
print()

print("Average of three numbers")
num1 = float(input("Enter number #1: "))
num2 = float(input("Enter number #2: "))
num3 = float(input("Enter number #3: "))
average = (num1+num2+num3)/3
print("Average is:", average)
print()

print("Convert minutes to hours and minutes")
minutes_by_user = int(input("Enter minutes: "))
#hours = minutes_by_user//60
#minutes = minutes_by_user%60
hours, minutes = divmod(minutes_by_user, 60)
print("In",minutes_by_user, "minutes -", hours, "hours", minutes, "minutes")
print()

print("Discount calculation")
price = float(input("Enter the price: "))
discount = int(input("Enter the discount: "))
price_with_disc = price - price/100*discount
print("Price with discount:", price_with_disc)
print()

print("Last digit in the number")
number = int(input("Enter the number: "))
last_digit = number % 10
print("Last digit is:", last_digit)
print()

print("Perimeter calculation")
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
perimeter = (side_a + side_b) * 2
print("Perimeter: ", perimeter)
print()

print("Four digits in row")
number = int(input("Enter 4 digits number: "))
digit1 = number // 1000
digit2 = (number - digit1*1000) // 100
digit3, digit4 = divmod((number - digit1*1000-digit2*100), 10)
print(digit1, digit2, digit3, digit4, sep="\n")