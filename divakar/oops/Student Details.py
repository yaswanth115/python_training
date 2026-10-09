
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

s1 = Student("Ravi", 21, "Python")
s2 = Student("Priya", 22, "Java")
s3 = Student("Arun", 20, "C++")

s1.display()
print()
s2.display()
print()
s3.display()