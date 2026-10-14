
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.02

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    def calculate_interest(self):
        return self.balance * 0.05

account1 = BankAccount("Ravi", 10000)
account2 = SavingsAccount("Priya", 10000)

print("Bank Account Interest:", account1.calculate_interest())
print("Savings Account Interest:", account2.calculate_interest())
