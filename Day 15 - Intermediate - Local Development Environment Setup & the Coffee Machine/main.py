# https://repl.it/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

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


# TODO: 4. Check resources sufficient?
def resource_check(order):
    """Checks available resources for the order"""
    for key in resources:
        if key in MENU[order]["ingredients"]:
            if resources[key] < MENU[order]['ingredients'][key]:
                # print(MENU[order]['ingredients'][key])
                print(f"Sorry there is not enough {key}")
                not_enough_resources = True
                return not_enough_resources
                break
    # for key, value in resources.items():
    #     print("available", key, value)
    # for key, value in MENU[order]['ingredients'].items():
    #     print("Your order requires: ", key, value)


def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_sum = (quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100
    total_sum = format(total_sum, ".2f")
    total_sum = float(total_sum)
    return total_sum



money = 0.0
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
app_running = True
while app_running:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. Your code should end execution when this
    # happens
    if drink == "off":
        break
    # TODO: 3. Print report
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        continue
    else:
        resource_shortage = resource_check(drink)
        if resource_shortage == True:
            continue
    
    # TODO: 5. Process coins.
    total_sum = process_coins()

    print(total_sum)
    print(MENU[drink]["cost"])
# TODO: 6. Check transaction successful?
    if total_sum < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif total_sum >= MENU[drink]["cost"]:
        change_left = total_sum - MENU[drink]["cost"]
        change_left = format(change_left, ".2f")
        change_left = float(change_left)
        if total_sum > MENU[drink]["cost"]:
            print(f"Here is ${change_left} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        money += MENU[drink]['cost']

# TODO: 7. Make Coffee.
    for key in resources:
        if key in MENU[drink]["ingredients"]:
            resources[key] -= MENU[drink]['ingredients'][key]
