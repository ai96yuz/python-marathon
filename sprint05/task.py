# Task 1


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


# Task 2


# ....


# Task 3

import re


def valid_email(txt):
    validator = bool(re.search(r'^([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})', txt))

    try:
        if not validator:
            return 'Email is not valid'
        if validator:
            return 'Email is valid'

    except:
        return 'Email is not valid'


# Task 4

def check_odd_even(num):
    try:
        if (num % 2) == 0:
            return 'Entered number is even'
        else:
            return 'Entered number is odd'
    except:
        return 'You entered not a number.'


# Task 5


def divide(numerator, denominator):
    try:
        if denominator == 0:
            return 'Oops, {}/{}, division by zero is error!!!'.format(numerator, denominator)
        sum = numerator / denominator
        if sum:
            return 'Result is {}'.format(sum)
    except:
        return 'Value Error! You did not enter a number!'


# Task 6


