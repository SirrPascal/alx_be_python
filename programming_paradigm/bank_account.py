class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the BankAccount with an optional starting balance."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format with 2 decimals."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
