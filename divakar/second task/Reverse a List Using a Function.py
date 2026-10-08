def reverse_list(numbers):
    reverse = []

    for i in numbers:
        reverse = [i] + reverse

    return reverse


print(reverse_list([10, 20, 30, 40, 50]))