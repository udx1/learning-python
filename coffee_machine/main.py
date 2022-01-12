from menu import MENU
from menu import resources

# local variables
DRINKS = []
INGREDIENTS = "ingredients"
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
COST = "cost"


def load_drinks():
    """Function to load drinks served."""
    for drinks in MENU:
        DRINKS.append(drinks)


def print_report(m):
    """Function to print the resources reports.\n
       Takes the money in hand as an input parameter."""
    for resource_key in resources:
        unit = "g" if resource_key == COFFEE else "ml"
        print(f"{resource_key} : {resources[resource_key]}{unit}")
    print(f"Money : ${round(m,2)}")


def check_resources(drink):
    """Checks whether sufficient resources are available to make the requested drink."""
    if MENU[drink][INGREDIENTS][WATER] > resources[WATER]:
        return WATER
    elif MENU[drink][INGREDIENTS][COFFEE] > resources[COFFEE]:
        return COFFEE
    elif drink != "espresso" and MENU[drink][INGREDIENTS][MILK] > resources[MILK]:
        return MILK

    return 1

def process_coins():
    """Function to accept money and validate"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))*.25
    dimes = int(input("How many dimes?:"))*.10
    nickles = int(input("How many nickles?:"))*.05
    pennies = int(input("How many pennies?:"))*.01

    return quarters + dimes + nickles + pennies


def check_transaction(drink, money_inserted):
    """Function to check the whether money tendered is sufficient to buy a coffee"""
    coffee_cost = MENU[drink]["cost"]
    change = 0
    print(f"Money inserted = {round(money_inserted,2)}, {drink} costs {coffee_cost}")
    if money_inserted < coffee_cost:
        return -1
    elif money_inserted > coffee_cost:
        change = round(money_inserted - coffee_cost, 2)
        print(f"Here is ${change} in change.")
    return (money_inserted - change)


def make_coffee(drink):
    """ Make coffee, ie update the resources use."""
    resources[WATER] -= MENU[drink][INGREDIENTS][WATER]
    resources[COFFEE] -= MENU[drink][INGREDIENTS][COFFEE]
    if drink != "espresso":
        resources[MILK] -= MENU[drink][INGREDIENTS][MILK]

    print(f"Here is your {drink} ☕. Enjoy!")


selection = "start"
money = 0.00
load_drinks()

while selection != "off":
    selection = input("What would you like? (espresso/latte/cappuccino):").lower()

    if selection == "report":
        print_report(money)
    elif selection in DRINKS:
        enough_resources = check_resources(selection)
        if enough_resources == 1:
            money_tendered = check_transaction(selection, process_coins())
            if money_tendered == -1:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += money_tendered
                make_coffee(selection)
        else:
            print(f"Sorry, there is not enough {enough_resources}")
    elif selection != "off":
        print("Invalid selection, please select a valid item from menu!")
