# ДЗ 14.1. Група студентів
# Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# На його основі створіть клас Студент (перевизначте метод виведення інформації).
# Створіть клас Група, екземпляр якого складається з об'єктів класу Студент. 
# Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, 
# інакше - None.
# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати 
# ці два методи;)
# Визначте для групи метод str() для повернення списку студентів у вигляді рядка.

class Person():
    def __init__(self, gender, age, name, surname):
        self.gender = gender
        self.name = name
        self.surname = surname
        self.age = age

    def __str__ (self):
        age_info = f"age: {self.age}" if self.age !=None else ""
        return (f"gender: {self.gender} {age_info} name: {self.name} surname: {self.surname}")


class Student(Person):
    def __init__(self, gender, age, name, surname, record_book):
        super().__init__(gender, age, name, surname)
        self.record_book = record_book

    def __str__(self):
        FIO_age_gend = super().__str__()
        return f"{FIO_age_gend} {self.record_book} "

class Group():
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, surname):
        student = self.find_student(surname)
        self.group.discard(student)

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student
                

    # def __str__(self):
    #     surname_list = list()
    #     for student in self.group:
    #         surname_list.append(student.surname)
    #     return f"group:{self.number} students: {surname_list}"

    def __str__(self):
        surname_list = ", ".join(sorted([student.surname for student in self.group ]))
        return surname_list



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!