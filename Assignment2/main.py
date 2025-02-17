import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    print("Welcome to the Ham Sandwich Maker Machine!")
    sandwich_size = input("What size sandwich would you like? (small/medium/large): ").lower()
    
    if sandwich_size not in recipes:
        print("Sorry, we don't offer that size.")
        return

    recipe = recipes[sandwich_size]
    order_ingredients = recipe["ingredients"]
    cost = recipe["cost"]

    if not sandwich_maker_instance.check_resources(order_ingredients):
        return

    print(f"The cost of a {sandwich_size} sandwich is ${cost:.2f}. Please insert coins.")
    total_coins = cashier_instance.process_coins()

    if cashier_instance.transaction_result(total_coins, cost):
        sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")

if __name__=="__main__":
    main()