
def validate_numbers(func):
    def wrapper(*args, **kwargs):

        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("All arguments must be numeric")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("All arguments must be numeric")

        return func(*args, **kwargs)

    return wrapper
@validate_numbers
def calculate_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
def main():
    print(calculate_sum(10, 20, 30))
    print(calculate_sum(5, 10, 15))

    try:
        print(calculate_sum(10, "20", 30))
    except TypeError as e:
        print(e)
main()