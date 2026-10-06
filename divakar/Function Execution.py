def call_count(func):
    count = 0
    def wrapper(name):
        nonlocal count
        count += 1
        print(f"{func.__name__} called {count} times")
        func(name)
    return wrapper
@call_count
def greet(name):
    print("Hello", name)
def main():
    greet("John")
    greet("David")
    greet("Alice")


main()