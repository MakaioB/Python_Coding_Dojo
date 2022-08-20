class BankAccount:
    def __init__(self, balance = 0, int_rate = 0.05): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
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
            self.balance = self.balance * self.int_rate
            print(self.balance)
            return(self.balance)

account_1 = BankAccount(52.79)
account_2 = BankAccount()
b = BankAccount
b.deposit(account_1, 5000.00)
b.deposit(account_2, 6969.69) #My friends game me the values to use.
b.withdraw(account_1, 5100.00)
b.withdraw(account_2, 25.00)
b.display_account_info(account_1)
b.display_account_info(account_2)
b.yield_interest(account_1)
b.yield_interest(account_2)
