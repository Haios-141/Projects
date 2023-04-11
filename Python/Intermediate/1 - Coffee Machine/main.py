from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu_items = menu.get_items().rstrip(menu.get_items()[-1])  # remove the last '/' from the string

turn_off_machine = False
while not turn_off_machine:
    prompt = f" What would you like? ({menu_items}): "
    choice = input(prompt).lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("\nTurning off, Goodbye 👋")
        turn_off_machine = True
    else:
        drink = menu.find_drink(choice)

        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
