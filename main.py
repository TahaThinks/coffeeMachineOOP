from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available_drinks = Menu()
requested_drink = input(f"What would you like {available_drinks.get_items()}?")
