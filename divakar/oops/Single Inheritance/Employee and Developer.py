
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Programming Language:", self.programming_language)

d1 = Developer("Arjun", 50000, "Python")
d2 = Developer("Priya", 60000, "Java")
d3 = Developer("Rahul", 55000, "JavaScript")

d1.display_details()
print()
d2.display_details()
print()
d3.display_details()
