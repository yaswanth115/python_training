def smallest_number(numbers):
    small = numbers[0]

    for num in numbers:
        if num < small:
            small = num

    return small


numbers = [25, 10, 45, 7, 32, 18]
print("Smallest number:", smallest_number(numbers))