class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def empoyee_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

class Developer(Employee):
    def __init__(self,name,employee_id,salary,language):
        super().__init__(name,employee_id,salary)
        self.language = language

# class Developer(Employee):
#     def __init__(self,name,employee_id,salary,language):
#         Employee.__init__(self,name,employee_id,salary)
#         self.language = language


    def developer_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Language:", self.language)


m1 = Employee("Divakar", 1, 10000)
m1.empoyee_info()
d1 = Developer("yaswanth", 1, 10000, "Python")
d1.developer_info()
d1.empoyee_info()