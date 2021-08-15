# TASK 1


from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):
    field_name = "Fettuccine Alfredo"

    def cook(self):
        print(f'Italian main course prepared: {self.field_name}')


class Tiramisu(Product):
    field_name = "Tiramisu"

    def cook(self):
        print(f'Italian dessert prepared: {self.field_name}')


class DuckALOrange(Product):
    field_name = "Duck À L'Orange"

    def cook(self):
        print(f'French main course prepared: {self.field_name}')


class CremeBrulee(Product):
    field_name = "Crème brûlée"

    def cook(self):
        print(f'French dessert prepared: {self.field_name}')


class Factory(ABC):

    @abstractmethod
    def get_dish(type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()
        if type_of_meal == "dessert":
            return CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory
        if type_of_factory == "french":
            return FrenchDishesFactory


# TASK 2


class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def __repr__(self):
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount


def on_sale_discount(order):
    return order.price * 0.5


def twenty_percent_discount(order):
    return order.price * 0.2


# TASK 3


class MotorCycle:
    """Class for MotorCycle"""

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


class Truck:
    """Class for Truck"""

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    """Class for Car"""

    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"


class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """

    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict"""
        return self.obj.__dict__


# TASK 4


class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


""" main method """
if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()


# TASK 5


class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()
