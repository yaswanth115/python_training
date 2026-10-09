
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

a1 = BankAccount("Ravi", 1001)
a2 = BankAccount("Priya", 1002)

print("Account 1")
print("Initial balance:", a1.balance)
a1.deposit(5000)
a1.withdraw(1500)
a1.check_balance()

print()

print("Account 2")
a2.deposit(2000)
a2.withdraw(500)
a2.check_balance()