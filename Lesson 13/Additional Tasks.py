# Створіть клас Square, який успадковує клас Rectangle і має лише один атрибут side (сторона). 
# Додайте метод calculate_area() так, щоб правильно обчислював площу квадрата.

# class Rectangle:
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b

#     def __str__(self):
#         return f"side a:{self.side_a} side b:{self.side_b}"
#     def calculate_area(self):
#         return self.side_a*self.side_b

# class Square(Rectangle):
#     def __init__(self, side_a):
#         self.side_a = side_a
#         self.side_b = side_a
    
# my_sqr = Square(4)

# print(my_sqr.calculate_area())


# Additional Task #3
# Умова:
# Створіть клас MathOperations, який має статичний метод multiply, який приймає два аргументи
# і повертає їхню добуток.


# class MathOperations():
#     staticmethod
#     def multiply(a, b):
#         return a*b
    
# print(MathOperations.multiply(3,4))

# Створіть класи A, B, C і D, як описано в питанні про "ромб". 
# Додайте метод show у кожен з класів, який виводить своє ім'я (A, B, C або D). '
# 'Зверніть увагу на правильний виклик методу show для об'єкта класу D.

# Ці тести перевіряють правильність роботи ромбовидного успадкування для класів A, B, C і D. 
# Тест 1 визначає вивід для класу A, який відомий і не має успадкування. 
# Тест 2 перевіряє вивід для класу B, який успадковує від класу A. 
# Тест 3 перевіряє вивід для класу D, який успадковує від класів B та C. 
# В кожному тесті використовується функція capture_stdout, 
# захоплює вивід методу show та дозволяє перевірити його з допомогою assert.

class A:
    def show(self):
        print("A", end="")

class B(A):
    def show(self):
        A.show()
        print("B", end="")

class C(A):
    def show(self):
        A.show()
        print("C", end="")

class D(B, C):
    def show(self):
        B.show()
        C.show()


obj_A = A()
output_A = capture_stdout(obj_A.show)
assert output_A == "A"