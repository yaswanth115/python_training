employees = [
    {"name": "John", "salary": 65000},
    {"name": "David", "salary": 85000},
    {"name": "Alex", "salary": 55000},
    {"name": "Sam", "salary": 95000}
]

salary_sorted = sorted(
    employees,
    key=lambda x: x["salary"],
    reverse=True
)

print("Sorted by Salary:")
for employee in salary_sorted:
    print(employee)