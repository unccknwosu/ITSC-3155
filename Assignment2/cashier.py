class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return 0
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            return False