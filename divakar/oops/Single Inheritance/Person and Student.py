
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)
        print("Course:", self.course)

s1 = Student("Ravi", 21, 101, "Python")
s2 = Student("Priya", 22, 102, "Data Science")

s1.display()
print()
s2.display()
