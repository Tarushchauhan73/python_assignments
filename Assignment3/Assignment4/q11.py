class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_count():
        print("Total Employees:", Employee.employee_count)

    def validate_salary(salary):
        return salary > 0


employee1 = Employee("Tarush", 50000)
employee2 = Employee("Rahul", 60000)
employee3 = Employee("Aman", 45000)

Employee.display_employee_count()
[]
print("Salary 50000 is valid:", Employee.validate_salary(50000))
print("Salary -1000 is valid:", Employee.validate_salary(-1000))