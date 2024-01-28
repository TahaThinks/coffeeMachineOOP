from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available_drinks = Menu()
machine_stats = CoffeeMaker()
requested_drink = input(f"What would you like {available_drinks.get_items()}? ").lower()
if requested_drink == 'report':
    machine_stats.report()
else:
    available_drinks.find_drink(requested_drink)