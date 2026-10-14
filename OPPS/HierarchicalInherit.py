class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display_details(self):
        self.display_employee()
        print(f"Language: {self.language}")


class Tester(Employee):
    def __init__(self, name, salary, testing_tool):
        super().__init__(name, salary)
        self.testing_tool = testing_tool

    def display_details(self):
        self.display_employee()
        print(f"Testing Tool: {self.testing_tool}")


dev = Developer("Ravi", 60000, "Python")
tester = Tester("Priya", 50000, "Selenium")

print("Developer Details")
dev.display_details()

print("\nTester Details")
tester.display_details()