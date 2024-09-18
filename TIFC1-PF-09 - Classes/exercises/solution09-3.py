class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate  # Default interest rate is 1%

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account if sufficient balance is available."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Prints the current account balance."""
        print(f"Current balance is ${self.balance:.2f}.")

    def calculate_interest(self):
        """Calculates interest on the current balance based on the interest rate."""
        interest = self.balance * self.interest_rate
        print(f"Interest on the current balance is ${interest:.2f}.")
        return interest

    def apply_interest(self):
        """Applies the calculated interest to the balance."""
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance is ${self.balance:.2f}.")


# Creating instances representing different bank accounts
account1 = BankAccount("123456789", "Alice", 3000, 0.03)  # 3% interest rate
account2 = BankAccount("987654321", "Bob", 10000, 0.10)    # 10% interest rate

# Performing transactions on account1
account1.check_balance()
account1.deposit(200)
account1.withdraw(100)
account1.apply_interest()  # Applying interest to the balance

# Performing transactions on account2
account2.check_balance()
account2.deposit(150)
account2.withdraw(150)  # This should trigger an insufficient balance message
for i in range(0,5):
    account2.apply_interest()  # Applying interest to the balance
