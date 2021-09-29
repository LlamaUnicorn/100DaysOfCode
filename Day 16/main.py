# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Print report
my_money_machine = MoneyMachine()
my_coffemaker = CoffeeMaker()


# TODO: Check resources sufficient
is_on = True

my_menu = Menu()
#my_menu_item = MenuItem() 

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


# TODO: Process coins
# TODO: Check transaction successful
# TODO: Make Coffee

# test_menu = MenuItem('Latte')
# test_menu.name('Latte')
# print(test_menu.ingredients)


