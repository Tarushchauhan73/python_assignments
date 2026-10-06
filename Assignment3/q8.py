class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("After deposit:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("After withdrawal:", self.balance)


account1 = BankAccount("Tarush", 5000)

account1.deposit(2000)
account1.withdraw(1000)