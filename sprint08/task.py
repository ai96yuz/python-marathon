# Task 1



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


def quadratic_equation(a, b, c):
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
        self.assertTrue(discriminant > 0)

    def test_discriminant_negative(self):
        self.assertFalse(discriminant < 0)

    def test_discriminant_zero(self):
        with self.assertRaises(ZeroDivisionError):
            discriminant // 0

    def test_value_zero(self):
        with self.assertRaises(ZeroDivisionError):
            a == 0


# Task 4



# Task 5



# Task 6