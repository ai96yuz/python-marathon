# Task 1


def outer(name):
    def inner():
        print('Hello, {}!'.format(name))
    return inner


# Task 2


def create(name):
    return lambda x: 'True' if x == name else 'False'


# Task 3
import re


def create_account(user_name: str, password: str, secret_words: list):
    req_pass = re.findall(r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}', password)

    print(req_pass)

    # def check():

    # def check(user_login, user_password, user_secret):
    #     if not user_login, user_password, user_secret:
    #         user_login = user_name
    #         user_password = password
    #         user_secret = secret_words

    #     if user_name == user_login:
    #         yield
    #         name = user_name
    #         yield name


# def create_account(user_name: str, password: str, secret_words: list):
#     name = user_name
#     pin = password
#     word = secret_words
#
#     def check():
#         try:
#             if name == user_name and pin == password and word == secret_words:
#                 return name, pin, word
#         except ValueError:
#             print('ValueError')
#
#     return check


# Task 4


def divisor(num):
    for x in range(1, num + 1):
        if num / x == int(num / x):
            yield x
    while True:
        yield None


# Task 5


def logger(func):
    def concat(*args, **kwargs):
        value = ','.join(func(*args, **kwargs))
        return value

    return concat


# def logger(func):
#     def concat(*args, **kwargs):
#         return_value = func(*args, **kwargs)
#         return return_value
#     return concat

@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


# Task 6
from copy import deepcopy
from random import choice


def randomWord(l):
    if len(l) == 0:
        while True:
            yield None
    l_saved = deepcopy(l)
    while True:
        x = choice(l)
        yield x
        l.remove(x)
        if len(l) == 0:
            l = deepcopy(l_saved)
