# This app defines a BankAccount class with __init__, deposit, withdraw, and check_balance methods. The __init__ method is called when an object of the BankAccount class is created and it initializes the name and balance attributes of the object. The deposit and withdraw methods allow the user to deposit and withdraw money from the account, respectively. The check_balance method allows the user to check their account balance.

class BankAccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        print(f"Account {self.name} with balance {self.balance} created!!! ")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to the account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance to withdraw {amount}.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account.")

    def check_balance(self):
        print(f"Balance: {self.balance}")

# To use this app, you can create a BankAccount object by calling the BankAccount class and passing in the name of the account holder and the initial balance (if any). You can then use the deposit, withdraw, and check_balance methods to manage the account.

# Create a bank account
account = BankAccount("John Smith")

# Deposit 1000
account.deposit(1000)

# Check balance
account.check_balance()

# Withdraw 500
account.withdraw(500)
account.withdraw(501)

# Check balance again
account.check_balance()
