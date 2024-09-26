from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_on = True

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}):")

    if choice == "off":
        is_on = False
        break
    elif choice == "report":
        my_coffe_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)

        if not drink:
            continue
        if my_coffe_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffe_maker.make_coffee(drink)