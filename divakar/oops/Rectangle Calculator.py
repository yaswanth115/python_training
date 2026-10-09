
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(10, 5)
r2 = Rectangle(8, 4)

print("Rectangle 1")
print("Length:", r1.length)
print("Width:", r1.width)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print()

print("Rectangle 2")
print("Length:", r2.length)
print("Width:", r2.width)
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())