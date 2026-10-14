
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, model, fuel_type):
        super().__init__(brand, year)
        self.model = model
        self.fuel_type = fuel_type

    def display(self):
        print("Brand:", self.brand)
        print("Year:", self.year)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)

car1 = Car("Toyota", 2024, "Innova", "Diesel")
car1.display()
