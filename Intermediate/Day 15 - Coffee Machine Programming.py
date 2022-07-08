MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# from art import logo

# TODO: 2. Print report
def report():
    """ This function will give the report on the resources of the coffee machine. """

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${profit}')


# TODO: 4. Check resources sufficient
def check_resources(order_ingredients):
    """Return True when the ingredients in the machine is sufficient to make the order"""
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


# TODO: 5. Process coins
def process_coins():
    """Return the amount of coins inserted in the machine"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


# TODO: 6. Check transaction successful
# Check if user insert enough coins to purchase their drink
def check_transaction(money_received, drink_cost):
    """Return True if the transaction could be carried out successful"""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received >= drink_cost:
        change = drink_cost - money_received
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
        global profit
        profit += drink_cost
        return True


# TODO: 7. Make coffee
def make_coffee(drink_name, order_ingredients):
    "Deduct the required ingredients from the resoureces"
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name}☕. Enjoy!')


# The program for the Coffee machine
is_on = True

while is_on:
    # TODO: 1. Ask the user to choose a drink
    choice = input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 3. Turn the machine off by typing "off"
    if choice == 'off':
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
