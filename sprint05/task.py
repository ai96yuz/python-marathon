# Task 1


def divide(numerator, denominator):
    try:
        if denominator == 0:
            return 'Oops, {}/{}, division by zero is error!!!'.format(numerator, denominator)
        sum = numerator / denominator
        return 'Result is {}'.format(sum)
    except:
        return 'Value Error! You did not enter a number!'


# Task 2

import cmath


def solve_quadric_equation(a, b, c):
    try:
        if a == 0:
            return 'Zero Division Error'
        a, b, c = float(a), float(b), float(c)
        discriminant = (b**2 - 4*a*c)
        x1 = complex(-b - discriminant ** 0.5) / (2 * a)
        x2 = complex(-b + discriminant ** 0.5) / (2 * a)
        return 'The solution are x1={} and x2={}'.format(str(x1), str(x2))
    except:
        return 'Could not convert string to float'


# Task 3


class ToSmallNumberGroupError(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return repr(self.num)


def check_number_group(number):
    try:
        if isinstance(number, str):
            number = int(number)
        if number > 10:
            return 'Number of your group {} is valid'.format(number)
        if -10 < number <= 10:
            raise ToSmallNumberGroupError('Number of your group can\'t be less than 10')
    except ToSmallNumberGroupError as e:
        return 'We obtain error:' + e.num
    except:
        return 'You entered incorrect data. Please try again.'


# Task 4


class MyError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return repr(self.number)


def check_positive(number):
    try:
        if isinstance(number, str):
            number = int(number)
        if number >= 0:
            return 'You input positive number: {}'.format(float(number))
        if number < 0:
            raise MyError('{}. Try again.'.format(float(number)))
    except MyError as e:
        return 'You input negative number: ' + e.number
    except:
        return 'Error type: ValueError!'


# Task 5


def check_odd_even(num):
    try:
        return 'Entered number is even' if (num % 2) == 0 else 'Entered number is odd'
    except:
        return 'You entered not a number.'


# Task 6

import re


def valid_email(txt):
    validator = bool(re.search(r'^([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})', txt))
    try:
        return 'Email is valid' if validator else 'Email is not valid'
    except:
        return 'Email is not valid'


# Task 7


def day_of_week(day):
    week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    try:
        for key, value in week.items():
            if int(day) == key:
                return value
        if day not in range(1, 7):
            return 'There is no such day of the week! Please try again.'
    except:
        return 'You did not enter a number! Please try again.'
