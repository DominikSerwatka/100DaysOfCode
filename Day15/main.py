# Coffe machine program
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


def print_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")
    
    
def check_resources(drink):
    """Take name of drink, return false if there is not enough resources and return True if is enough"""
    for item in MENU[drink]['ingredients']:
        if not MENU[drink]['ingredients'][item] < resources[item]:
            print(f"Lack of {item}")
            print(f"Sorry there is not enough {item}")
            return False
        else:
            resources[item] -= MENU[drink]['ingredients'][item]
    return True


def check_money(quarters, dimes, nickles, pennies, user_input):
    """take number of each coin name of drink, return cost of drink if that is enough money else return None"""
    money = round(float(quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01), 2)
    cost = MENU[user_input]['cost']
    if money >= cost:
        print(f"Here is {money-cost}$ in change.")
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return


def coffee_machine_start():
    run = True
    money = 0

    while run:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print_report(money)
        elif user_input == "off":
            print("end")
            run = False
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            if check_resources(user_input):
                print("Please insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))
                out = check_money(quarters, dimes, nickles, pennies, user_input)
                if out is not None:
                    print(f"Here is your {user_input} ☕ Enjoy!")
                    money += out


coffee_machine_start()


    
    
    