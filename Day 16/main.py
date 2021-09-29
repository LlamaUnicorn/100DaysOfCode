# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffemaker = CoffeeMaker()


is_on = True

my_menu = Menu()

while is_on:
    options = my_menu.get_items
    choice = input(f"What would you like ({options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money_machine.report()
        my_coffemaker.report()
    else:
        drink = my_menu.find_drink(choice)
        is_enough_ingredients = my_coffemaker.is_resource_sufficient(drink)
        is_payment_successful = my_money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            my_coffemaker.make_coffee(drink)

# TODO: Print report
# TODO: Check resources sufficient
# TODO: Process coins
# TODO: Check transaction successful
# TODO: Make Coffee

