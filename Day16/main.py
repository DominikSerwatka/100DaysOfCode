from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_run = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while is_run:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        is_run = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




