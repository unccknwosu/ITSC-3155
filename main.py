### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,    # slices
            "ham": 4,      # slices
            "cheese": 4,   # ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,    # slices
            "ham": 6,      # slices
            "cheese": 8,   # ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,    # slices
            "ham": 8,      # slices
            "cheese": 12,  # ounces
        },
        "cost": 5.50,
    }
}

resources = {
    "bread": 12,   # slices
    "ham": 18,     # slices
    "cheese": 24,  # ounces
}

### Complete functions ###

class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.profit = 0.0

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: ")) 
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
        except ValueError:
            print("Invalid input. Please enter integer values for coins.")
            return 0

        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total
    
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            self.profit += cost
            return True
        
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} ham sandwich. Enjoy!")
        
### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

machine_on = True

while machine_on:
    print("\nMenu:")
    for size in recipes:
        cost = recipes[size]["cost"]
        print(f"{size.capitalize()} Ham Sandwich - ${cost:.2f}")
        
    choice = input("\nWhat would you like? (small/medium/large/report/off): ").lower()
    
    if choice == "off":
        machine_on = False
        print("Turning off the machine. Goodbye!")
    elif choice == "report":
        print("\nMachine Resources:")
        for item, amount in machine.machine_resources.items():
            unit = "slices" if item in ["bread", "ham"] else "ounces"
            print(f"{item.capitalize()}: {amount} {unit}")
        print(f"Money: ${machine.profit:.2f}")
    elif choice in recipes:
        sandwich = recipes[choice]
        if machine.check_resources(sandwich["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, sandwich["ingredients"])
   
    else:
        print("Invalid input. Please choose 'small', 'medium', 'large', 'report', or 'off'.")