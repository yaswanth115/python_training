def create_multiplier(n):
    def multiply(x):
        return x * n
    return multiply
def main():
    double = create_multiplier(2)
    triple = create_multiplier(3)

    print(double(10))
    print(triple(10))
main()