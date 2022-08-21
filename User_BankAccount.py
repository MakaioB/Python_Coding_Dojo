class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
    def withdraw(self, amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            print(self.balance)
            return(self.balance)
        else:
            amount = amount + 5.00
            self.balance = self.balance - amount
            print("Insufficient funds: Charging a $5 fee")
            print(self.balance)
            return(self.balance)
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance * self.int_rate + self.balance
            print(self.balance)
            return(self.balance)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

account_1 = BankAccount(0.03, 25)
account_2 = BankAccount(0.02, 50)

b = BankAccount
u = User
u.deposit(account_1, 25)
u.deposit(account_2, 10)
u.withdraw(account_1, 30)
u.withdraw(account_2, 70)
u.display_account_info(account_1)
u.display_account_info(account_2)
u.yield_interest(account_1)
u.yield_interest(account_2)