class BankAccount:
    BALANCE_FILE = "balance.txt"

    def __init__(self, account_balance=None):
        if account_balance is not None:
            self.account_balance = account_balance
        else:
            # Load balance from file if it exists, otherwise start with 100
            self.account_balance = self._load_balance()

    def _load_balance(self):
        if os.path.exists(self.BALANCE_FILE):
            with open(self.BALANCE_FILE, "r") as f:
                return float(f.read().strip())
        return 100.0

    def _save_balance(self):
        with open(self.BALANCE_FILE, "w") as f:
            f.write(str(self.account_balance))

    def deposit(self, amount):
        self.account_balance += amount
        self._save_balance()

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            self._save_balance()
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")


bank = BankAccount(100)
# bank.deposit(50)
# bank.withdraw(20)
bank.display_balance()