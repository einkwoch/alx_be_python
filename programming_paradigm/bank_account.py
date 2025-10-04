class BankAccount:
    def __init__ (self,account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance+=amount

    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance-=amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(self.account_balance)


bank = BankAccount(100)
# bank.deposit(50)
# bank.withdraw(20)
bank.display_balance()