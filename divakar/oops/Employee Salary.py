
class Employee:
    def __init__(self, employee_id, name, monthly_salary):
        self.employee_id = employee_id
        self.name = name
        self.monthly_salary = monthly_salary

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.annual_salary())

    def annual_salary(self):
        return self.monthly_salary * 12

e1 = Employee(101, "Ravi", 30000)
e2 = Employee(102, "Priya", 35000)
e3 = Employee(103, "Arun", 25000)

e1.display()
print()
e2.display()
print()
e3.display()