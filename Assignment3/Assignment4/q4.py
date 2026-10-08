class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, recipient_account):
        if amount <= self.__balance:
            self.__balance -= amount
            recipient_account.__balance += amount
            print(f"Transferred {amount} to {recipient_account.account_holder}.")
        else:
            print("Insufficient funds for transfer.")


account1 = BankAccount(101, "Tarush", 5000)
account2 = BankAccount(102, "Rahul", 3000)

account1.deposit(1000)
account1.withdraw(500)

account1.transfer(2000, account2)

print("Account 1 Balance:", account1.get_balance())
print("Account 2 Balance:", account2.get_balance())