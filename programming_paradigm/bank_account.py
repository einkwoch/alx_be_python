import os

class BankAccount:
    BALANCE_FILE = "balance.txt"

    def __init__(self, account_balance=None):
        # Load existing balance if no initial balance is given
        if account_balance is None:
            self.account_balance = self._load_balance()
        else:
            self.account_balance = account_balance
            self._save_balance()  # Save initial balance

    def _load_balance(self):
        """Read the saved balance from the file, or start with 100."""
        if os.path.exists(self.BALANCE_FILE):
            with open(self.BALANCE_FILE, "r") as f:
                try:
                    return float(f.read().strip())
                except ValueError:
                    return 100.0
        return 100.0

    def _save_balance(self):
        """Save the current balance to a file."""
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
        print(f"Current Balance: ${self.account_balance:.2f}")
