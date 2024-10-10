from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
menu=Menu()
coffe_maker=CoffeeMaker()
money_machine=MoneyMachine()
is_on=True;

while is_on:
  chosen=input(f'What do you like ({menu.get_items()}) ?').lower()
  if chosen=='off':
    is_on=False
  elif chosen=='report':
    coffe_maker.report()
    money_machine.report()
  else:
    drink=menu.find_drink(chosen)
    if drink==None:
      continue
    if coffe_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffe_maker.make_coffee(drink)
      
      
    



