class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_details(self):
        print("Car")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Number of Doors:", self.doors)


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_details(self):
        print("Bike")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Engine:", self.engine_cc, "CC")


car = Car("Toyota", "Camry", 4)
bike = Bike("Yamaha", "R15", 155)

vehicles = [car, bike]

for vehicle in vehicles:
    vehicle.display_details()
    print()