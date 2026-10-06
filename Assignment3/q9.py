class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Tarush", 70000)

employee1.display_details()