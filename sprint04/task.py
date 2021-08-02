# Task 1


class Employee(object):
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, employee_string):
        firstname, lastname, salary = map(str, employee_string.split('-'))
        person = cls(firstname, lastname, salary)
        return person


# Task 2


class Pizza(object):
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def hawaiian(cls):
        return Pizza(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return Pizza(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return Pizza(['spinach', 'olives', 'mushroom'])


# Task 3


