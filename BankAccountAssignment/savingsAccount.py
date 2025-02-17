from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, account_number="000000", routing_number="111111"):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate  
        
    def apply_interest(self):
        interest_amount = self.current_balance * self.interest_rate
        self.current_balance += interest_amount
        print(f"\nApplied interest of ${interest_amount:.2f} to {self.customer_name}'s account.")
        print(f"New balance after interest: ${self.current_balance:.2f}")
