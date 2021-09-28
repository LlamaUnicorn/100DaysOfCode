# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Print report
# TODO: Check resources sufficient
# TODO: Process coins
# TODO: Check transaction successful
# TODO: Make Coffee

# test_menu = MenuItem('Latte')
# test_menu.name('Latte')
# print(test_menu.ingredients)

my_coffemaker = CoffeeMaker()
my_coffemaker.report()
my_coffemaker.is_resource_sufficient()