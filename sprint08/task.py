# Task 1


import unittest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self, *args):
        self.data = args

    def get_total_price(self):
        total_price = 0
        for item in self.data[0]:
            discount = 0
            if item.count > 20:
                discount = item.price * 0.5
            elif item.count == 20:
                discount = item.price * 0.3
            elif item.count >= 10:
                discount = item.price * 0.2
            elif item.count >= 7:
                discount = item.price * 0.1
            elif item.count >= 5:
                discount = item.price * 0.05
            total_price += item.count * (item.price - discount)
        return total_price


class CartTest(unittest.TestCase):

    def setUp(self):
        self.products = (Product('p1', 10, 4),
                         Product('p2', 100, 5),
                         Product('p3', 200, 6),
                         Product('p4', 300, 7),
                         Product('p5', 400, 9),
                         Product('p6', 500, 10),
                         Product('p7', 1000, 20))
        self.cart = Cart(self.products)

    def testResult(self):
        self.assertEqual(self.cart.get_total_price(), 24785.0)


# Task 2


import unittest


class DivideTest(unittest.TestCase):
    def test_integer_solution(self):
        self.assertTrue(4 // 2 == 2)

    def test_non_integer_solution(self):
        self.assertEqual(5 // 2, 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            1 // 0


# Task 3


import unittest
import math

discriminant = int()


def quadratic_equation(a, b, c):
    global discriminant
    discriminant = b ** 2 - 4 * a * c

    if a == 0:
        raise ValueError
    else:
        if discriminant == 0:
            x1 = -b / (2 * a)
            return x1
        elif discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return (x1, x2)


class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_positive(self):
        self.assertTrue(discriminant >= 0)

    def test_discriminant_negative(self):
        self.assertFalse(discriminant < 0)

    def test_discriminant_zero(self):
        with self.assertRaises(ZeroDivisionError):
            discriminant // 0

    def test_discriminant_regex(self):
        with self.assertRaisesRegex(ValueError, 'literal'):
            int('XYZ')


# Task 4



# Task 5



# Task 6