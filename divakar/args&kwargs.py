def process_data(*args, **kwargs):
    minimum = kwargs.get("minimum", 0)
    operation = kwargs.get("operation", "sum")

    # Apply minimum filter
    numbers = [num for num in args if num >= minimum]

    if operation == "sum":
        return sum(numbers)

    elif operation == "max":
        return max(numbers) if numbers else None

    elif operation == "min":
        return min(numbers) if numbers else None

    elif operation == "average":
        return sum(numbers) / len(numbers) if numbers else None

    else:
        return "Invalid operation"


print(process_data(10, 20, 30, 40, operation="sum", minimum=20))
print(process_data(10, 20, 30, 40, operation="max", minimum=20))
print(process_data(10, 20, 30, 40, operation="min", minimum=20))
print(process_data(10, 20, 30, 40, operation="average", minimum=20))