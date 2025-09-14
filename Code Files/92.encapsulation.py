class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public attribute
        self.__balance = initial_balance     # Private attribute (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice Smith", 1000)

print(f"Account holder: {account.account_holder}")
print(f"Initial balance: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500) # Attempt to withdraw more than available

# Attempting to directly access the private attribute (will result in an AttributeError)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Error: {e}")

# Accessing the name-mangled attribute (not recommended for direct use)
print(f"Accessing name-mangled balance: {account._BankAccount__balance}")