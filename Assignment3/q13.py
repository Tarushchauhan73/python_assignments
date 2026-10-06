class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


product = Product("Laptop", 50000)

print("Product:", product.name)
print("Price:", product.get_price())

product.set_price(55000)

print("Updated Price:", product.get_price())