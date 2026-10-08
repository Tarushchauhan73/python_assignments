class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class Developer(Employee):
    def calculate_salary(self):
        allowance = 5000
        return self.basic_salary + allowance


class Manager(Employee):
    def calculate_salary(self):
        allowance = 10000
        return self.basic_salary + allowance


developer = Developer("Rahul", 40000)
manager = Manager("Tarush", 70000)

print("Developer:", developer.name)
print("Salary:", developer.calculate_salary())

print()

print("Manager:", manager.name)
print("Salary:", manager.calculate_salary())