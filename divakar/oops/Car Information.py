
class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.price}"

c1 = Car("Toyota", "Camry", 2024, 2500000)
c2 = Car("Honda", "City", 2025, 1500000)
c3 = Car("Hyundai", "Creta", 2024, 1800000)

print(c1)
print(c2)
print(c3)