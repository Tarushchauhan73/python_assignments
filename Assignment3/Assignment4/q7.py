class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def update_stock(self, new_quantity):
        self.quantity = new_quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_cart_price(self):
        total_cart_price = sum(
            product.calculate_total_price()
            for product in self.products
        )
        return total_cart_price


product1 = Product("Laptop", 50000, 2)
product2 = Product("Smartphone", 20000, 3)

cart = ShoppingCart()

cart.add_product(product1)
cart.add_product(product2)

print("Shopping Cart:")
print("Total Cart Price:", cart.calculate_total_cart_price())