from waiter import Waiter
from chef import Chef
from pizza_order import PizzaOrder
from burger_order import BurgerOrder

chef = Chef()
pizzaOrder = PizzaOrder(chef)
burgerOrder = BurgerOrder(chef)

waiter = Waiter()
waiter.take_order(pizzaOrder)
waiter.take_order(burgerOrder)