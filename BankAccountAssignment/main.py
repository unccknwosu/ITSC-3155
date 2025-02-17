from savingsAccount import SavingsAccount
from checkingAccount import CheckingAccount

def main():
    # ----- Savings Account Scenarios -----
    print("=== Savings Account Scenario ===")
    
    # Create two instances of SavingsAccount
    savings1 = SavingsAccount("Charlie", 2000, 100, interest_rate=0.05, account_number="SAV001", routing_number="RT001")
    savings2 = SavingsAccount("Dana", 1500, 100, interest_rate=0.03, account_number="SAV002", routing_number="RT002")

    # Scenario for savings1
    savings1.print_customer_information()
    savings1.deposit(300)
    savings1.apply_interest()
    savings1.withdraw(500)
    savings1.print_customer_information()

    # Scenario for savings2
    savings2.print_customer_information()
    savings2.deposit(200)
    savings2.apply_interest()
    savings2.withdraw(100)
    savings2.print_customer_information()

    # ----- Checking Account Scenarios -----
    print("\n=== Checking Account Scenario ===")
    
    # Create two instances of CheckingAccount
    checking1 = CheckingAccount("Eve", 1000, 50, transfer_limit=500, account_number="CHK001", routing_number="RT003")
    checking2 = CheckingAccount("Frank", 800, 50, transfer_limit=300, account_number="CHK002", routing_number="RT004")

    # Scenario: A user opens a checking account and performs transactions
    checking1.print_customer_information()
    checking1.deposit(100)
    checking1.withdraw(150)
    checking1.print_customer_information()

    # Specific scenario: Eve attempts to withdraw $900 (which might be denied if it violates the minimum balance)
    print("\nScenario: Eve attempts to withdraw $900 from her checking account.")
    checking1.withdraw(900)

    # Demonstrate transfer with limitations:
    print("\nTesting transfer from checking1 to checking2:")
    # Attempt a transfer that exceeds the transfer limit
    checking1.transfer(600, checking2)
    # Attempt a valid transfer
    checking1.transfer(400, checking2)

    # Final account information after transfers
    checking1.print_customer_information()
    checking2.print_customer_information()

if __name__ == "__main__":
    main()
