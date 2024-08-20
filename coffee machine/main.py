from menu import MENU
from menu import resources


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received,cost_of_coffee ):
    if money_received > cost_of_coffee:
        print("Transaction successful, Please wait while we are processing your order. ")
        print(f"Please collect your change {money_received - cost_of_coffee}")
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name , order_ingredient):
    for item in resources:
        resources[item]-=order_ingredient[item]
    print(f"Here is your {drink_name}, ENJOY!")

is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(MENU[choice]["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





