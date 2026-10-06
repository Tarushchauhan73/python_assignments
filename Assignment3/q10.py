class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.display_details()

print()

car2.display_details()