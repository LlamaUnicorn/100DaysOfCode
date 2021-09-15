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
            "milk": 1500,
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
def resource_check(drink):
    for key in resources:
        if key in MENU[drink]["ingredients"]:
            if resources[key] < MENU[drink]['ingredients'][key]:
                # print(MENU[drink]['ingredients'][key])
                print(f"Sorry there is not enough {key}")
                break
        # print(MENU[drink]['ingredients'][key])
    # for key, value in resources.items():
    #     print("available", key, value)
    # for key, value in MENU[drink]['ingredients'].items():
    #     print("Your order requires: ", key, value)


money = 0
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
app_running = True
while app_running:
    drink = input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. Your code should end execution when this
    # happens
    if drink == "off":
        # app_running = False
        break
    # TODO: 3. Print report
    elif drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        resource_check(drink)

# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.