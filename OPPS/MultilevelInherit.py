class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(
        self, name, age, employee_id, salary, department
    ):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_employee()
        print(f"Department: {self.department}")


manager1 = Manager("Ravi", 35, "E101", 80000, "IT")
manager1.display_manager()