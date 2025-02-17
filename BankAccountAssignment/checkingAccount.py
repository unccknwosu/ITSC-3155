from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, account_number="000000", routing_number="111111"):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit 

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"\nTransfer denied: Amount ${amount} exceeds transfer limit of ${self.transfer_limit}.")
        elif self.current_balance - amount < self.minimum_balance:
            print("\nTransfer denied: Insufficient funds to maintain minimum balance after transfer.")
        else:
            self.current_balance -= amount
            target_account.current_balance += amount
            print(f"\nTransferred ${amount} from {self.customer_name}'s account to {target_account.customer_name}'s account.")
            print(f"{self.customer_name}'s new balance: ${self.current_balance}")
            print(f"{target_account.customer_name}'s new balance: ${target_account.current_balance}")
