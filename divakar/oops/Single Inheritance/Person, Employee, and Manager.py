
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary,
                 department, team_size):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        self.team_size = team_size

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Team Size:", self.team_size)

m1 = Manager("Suresh", 35, "E101", 80000, "IT", 10)
m1.display_details()
