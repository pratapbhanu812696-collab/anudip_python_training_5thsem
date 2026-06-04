8. ATM Simulation System
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")
# Example usage
atm = ATM()
atm.check_balance()
atm.deposit(1000)
atm.check_balance()
atm.withdraw(200)
atm.check_balance()
atm.withdraw(900)
atm.check_balance()
atm.deposit(500)
atm.check_balance()
atm.withdraw(300)
atm.check_balance()

