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


import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):
    pass

class TriangleNotExistException(Exception):
    pass

class dopException(TriangleNotExistException):
    pass

class dopException2(TriangleNotValidArgumentException):
    pass

class Triangle:
    def __init__(self,triangle):
        ###validation of arguments
        self.flag=True
        try:
            if type(triangle)!=tuple:
                raise dopException2
            else:
                if len(triangle)!=3:
                    raise dopException2
                else:
                    self.a, self.b, self.c = triangle[0], triangle[1], triangle[2]
                    if type(self.a)!=int or type(self.b)!=int or type(self.c)!=int:
                        raise dopException2
        except TriangleNotValidArgumentException as e:
            self.flag=False
            print("Not valid arguments")

         ####validation of existing triangle
        if self.flag==True:
            try:
                if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
                    pass
                else:
                    raise dopException
            except TriangleNotExistException as e:
                print("Can`t create triangle with this arguments")

    #get_area
    def get_area(self):
        if self.flag==True:
            p=(self.a+self.b+self.c)/2
            s=sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
            return s

class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.not_valid_triangle = [
            (1, 2, 3)]
    def test_class(self):
        self.assertEqual(type(Triangle),type)
    def test_res(self):
        self.assertNotEqual(TriangleNotValidArgumentException,TriangleNotExistException)
    def test_smth(self):
        self.assertLess(len(self.not_valid_triangle),2)


# Task 5


import unittest


class Worker:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary < 0:
            raise ValueError
        elif self.salary <= 1000:
            return 0.0
        elif self.salary <= 3000:
            return (self.salary - 1000) * 0.1
        elif self.salary <= 5000:
            return (3000 - 1000) * 0.1 + (self.salary - 3000) * 0.15
        elif self.salary <= 10000:
            return (3000 - 1000) * 0.1 + (5000 - 3000) * 0.15 + (self.salary - 5000) * 0.21
        elif self.salary <= 20000:
            return (3000 - 1000) * 0.1 + (5000 - 3000) * 0.15 + (10000 - 5000) * 0.21 + (self.salary - 10000) * 0.3
        elif self.salary <= 50000:
            return (3000 - 1000) * 0.1 + (5000 - 3000) * 0.15 + (10000 - 5000) * 0.21 + (20000 - 10000) * 0.3 + (
                        self.salary - 20000) * 0.4
        return (3000 - 1000) * 0.1 + (5000 - 3000) * 0.15 + (10000 - 5000) * 0.21 + (20000 - 10000) * 0.3 + (
                    50000 - 20000) * 0.4 + (self.salary - 50000) * 0.47


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Vika", 100000)
        self.non_salary = Worker("Vasia")

    def testResult(self):
        self.assertEqual(self.worker.get_tax_value(), 40050.0)

    @unittest.expectedFailure
    def testNoneSalary(self):
        self.assertEqual(self.non_salary.get_tax_value(), 0.1)


# Task 6


import unittest
import re


def file_parser(*args):
    calculator = 0
    if len(args) > 2:
        file_path = args[0]
        find_str = args[1]
        replaced_str = args[2]
        # for line in file_read:
        #     result = re.findall(find_str, line)
        #     calculator += len(result)
        # return f'Replased {calculator} strings'
    else:
        file_path = args[0]
        find_str = args[1]
        file_read = open(file_path)
        for line in file_read:
            result = re.findall(find_str, line)
            calculator += len(result)
        return f'Found {calculator} strings'


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.file_parser = file_parser('parser.txt', 'better')

    def testResult(self):
        self.assertEqual(self.file_parser, 'Found 8 strings')

    @unittest.expectedFailure
    def testFailure(self):
        self.assertEqual(self.file_parser, 'Replased 8 strings')