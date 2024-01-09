class BankAccount:
    all_accounts = []
    bank_balance = 0
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.02, balance=0): 
        # your code here! (remember, instance attributes go here)
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self
    # @classmethod
    # def printAll(cls):
    #     for instance in cls.all_accounts:
    #         cls.bank_balance += self.balance

user1 = BankAccount(.02, 200)
user2 = BankAccount(.02, balance=0)
user3 = BankAccount(.05, 400)
user1.deposit(50).deposit(30).deposit(10).withdraw(30).yield_interest().display_account_info()
user2.deposit(25).deposit(50).withdraw(10).withdraw(20).withdraw(50).withdraw(25).yield_interest().display_account_info()
user3.deposit(75).withdraw(30).yield_interest().display_account_info()