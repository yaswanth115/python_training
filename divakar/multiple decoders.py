def calculate_salary(basic, bonus, tax=0):
    return basic + bonus - tax
def validate_input(basic, bonus, tax):
    if not isinstance(basic, (int, float)):
        return False
    if not isinstance(bonus, (int, float)):
        return False
    if not isinstance(tax, (int, float)):
        return False
    return True
def log_execution(basic, bonus, tax):
    print("Function: calculate_salary")
    print("Arguments:", basic, bonus, tax)

    if validate_input(basic, bonus, tax):
        result = calculate_salary(basic, bonus, tax)
        print("Result:", result)
    else:
        print("Invalid input")
log_execution(50000, 10000, 5000)