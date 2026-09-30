def calculator(operation, *args):
    if operation == "add":
        return sum(args)

    elif operation == "subtract":
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result

    elif operation == "divide":
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    else:
        return "Invalid operation"


print(calculator("add", 10, 20, 30, 40))
print(calculator("multiply", 2, 3, 4))
print(calculator("subtract", 100, 20, 10))
print(calculator("divide", 100, 2, 5))