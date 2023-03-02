from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_on = True

while is_on:
    coffee = input(f" What would you like? ({menu.get_items()}): ")
    drink = menu.find_drink(coffee)
    if coffee.lower() == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif coffee.lower() == "off":
        is_on = False
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
