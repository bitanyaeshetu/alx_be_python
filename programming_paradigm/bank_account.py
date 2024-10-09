class BankAccount:
    def __init__(self, account_holder = 0, ):
        self.account_holder = account_holder
        

    def deposit(self, amount):
        if amount > 0:
            self.account_holder += amount

    def withdraw(self, amount):
        if 0 < amount <= self.account_holder:
            self.account_holder -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_holder:.2f}")  # Ensure two decimal places and no extra spaces
