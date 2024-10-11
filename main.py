from menu import Menu, MenuItem, logo
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from replit import clear

clear()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

is_on = True
print(logo)
while is_on:
    object = menu.get_items()
    choice = input(f"What would you like? ({object}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)