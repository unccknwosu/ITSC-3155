class BankAccount:
#Bank title
    bank_title = "KC's Software Engineering Bank"

#Instance Attributes
    def __init__(self, customer_name, current_balance, minimum_balance, account_number="000000", routing_number="111111"):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number    
        self.__routing_number = routing_number

#Methods
    def deposit(self, amount):
        self.current_balance += amount
        print(f"\nDeposited {amount} to {self.customer_name}'s account.")
        print(f"New balance: {self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("\nWithdrawal denied: Balance would fall below the minimum allowed.")
        else:
            self.current_balance -= amount
            print(f"\nWithdrew {amount} from {self.customer_name}'s account.")
            print(f"New balance: {self.current_balance}")

    def print_customer_information(self):
        print(f"\nBank Title: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number (protected): {self._account_number}")
        print(f"Routing Number (private): {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")

"""Test Cases
account1 = BankAccount("Alice", 1000, 200)
account1.print_customer_information()
account1.deposit(250)
account1.withdraw(900)
account1.print_customer_information()

account2 = BankAccount("Bob", 500, 50)
account2.print_customer_information()
account2.deposit(250)
account2.withdraw(900)
account2.print_customer_information()"""