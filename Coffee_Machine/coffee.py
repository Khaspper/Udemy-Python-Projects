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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# resources["water"] -= MENU["latte"]["ingredients"]["water"]
# print(MENU["cappuccino"]["cost"])


def enough_ingredients(coffee):
    if coffee == "espresso":
        if MENU[coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        return True

    else:
        if MENU[coffee]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            return False

        elif MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False

        elif MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
    take_from_resource(coffee)
    return True


def take_from_resource(coffee):
    if coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


def take_payment(coffee):
    global money
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * .25
    dimes = int(input("how many dimes?: ")) * .10
    nickles = int(input("how many nickles?: ")) * .05
    pennies = int(input("how many pennies?: ")) * .01

    total = quarters + dimes + nickles + pennies
    if total >= MENU[coffee]["cost"]:
        money += MENU[coffee]["cost"]

        if total > MENU[coffee]["cost"]:
            change = total - MENU[coffee]["cost"]
            print(f"Here is ${change} in change")
        else:
            print("No change :)")
        return True

    return False


def machine():
    coffee = input(" What would you like? (espresso/latte/cappuccino): ")

    if coffee.lower() == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
        machine()

    elif coffee.lower() == "espresso":
        if enough_ingredients(coffee):
            if not take_payment(coffee):
                print("Sorry that's not enough money. Money refunded.")
                machine()
            else:
                take_from_resource(coffee)
                print(f"Here is your {coffee} ☕️. Enjoy!")
                machine()
        machine()

    elif coffee.lower() == "latte":
        if enough_ingredients(coffee):
            if not take_payment(coffee):
                print("Sorry that's not enough money. Money refunded.")
                machine()
            else:
                take_from_resource(coffee)
                print(f"Here is your {coffee} ☕️. Enjoy!")
                machine()
        machine()

    elif coffee.lower() == "cappuccino":
        if enough_ingredients(coffee):
            if not take_payment(coffee):
                print("Sorry that's not enough money. Money refunded.")
                machine()
            else:
                take_from_resource(coffee)
                print(f"Here is your {coffee} ☕️. Enjoy!")
                machine()
        machine()

    elif coffee.lower() == "off":
        print("Have a good day!")


machine()
