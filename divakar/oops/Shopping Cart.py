class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(product.name, "added to cart.")

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            print(product.name, "removed from cart.")
        else:
            print(product.name, "not found in cart.")

    def calculate_total(self):
        total = 0
        for product in self.items:
            total += product.price
        return total

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
            return

        for product in self.items:
            print(f"{product.name}: {product.price}")

        print("Total:", self.calculate_total())

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 800)
p3 = Product("Keyboard", 1500)

cart = ShoppingCart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

print("\nShopping Cart:")
cart.display_cart()

cart.remove_product(p2)

cart.remove_product(p2)

print("\nUpdated Shopping Cart:")
cart.display_cart()