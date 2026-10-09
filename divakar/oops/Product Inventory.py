
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def sell(self, quantity):
        if quantity <= 0:
            print("Sale quantity must be positive.")
        elif quantity > self.quantity:
            print("Not enough stock available.")
        else:
            self.quantity -= quantity
            print("Sold:", quantity)

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Remaining Stock:", self.quantity)
        print("Inventory Value:", self.total_value())

p1 = Product(101, "Laptop", 50000, 10)
p2 = Product(102, "Mouse", 500, 20)
p3 = Product(103, "Keyboard", 1000, 15)

p1.sell(3)
p2.sell(5)
p3.sell(2)

print()

p1.display()
print()
p2.display()
print()
p3.display()