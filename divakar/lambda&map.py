def process_numbers(numbers):
    result = list(map(lambda x: x * x,filter(lambda x: x > 15 and x % 2 == 0, numbers)))
    return result
numbers = [12, 5, 18, 21, 30, 7, 44, 15, 60]

print(process_numbers(numbers))