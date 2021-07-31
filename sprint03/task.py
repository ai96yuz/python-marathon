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


def create_account(user_name, password, secret_words):
    password_regular = re.compile(r'(?=.*[0-9])(?=.*[!@#$%^&_*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&_*]{6,}')
    password_checker = bool(re.search(password_regular, password))

    if not password_checker:
        raise ValueError

    def check(password_check, secret_words_check):
        if password != password_check:
            return False
        secret_checker = []
        secret_copy = secret_words.copy()
        for word in secret_words_check:
            for item in secret_copy:
                if word == item:
                    secret_checker.append(word)
                    secret_copy[secret_copy.index(item)] = ""
                    break
        if len(secret_words) != len(secret_words_check):
            return False
        elif len(secret_checker) >= len(secret_words) - 1:
            return True
        elif len(secret_checker) < len(secret_words) - 1:
            return False
    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])


# Task 4


def divisor(num):
    for x in range(1, num + 1):
        if num / x == int(num / x):
            yield x
    while True:
        yield None


# Task 5


def logger(func):
    def info(*args, **kwargs):
        func_result = func(*args, **kwargs)
        result = [f"Executing of function {func.__name__} with arguments"]
        if args and kwargs:
            args = [str(item) for item in args]
            kwargs = [str(item) for item in kwargs.values()]
            args.extend(kwargs)
            result.append(f"{', '.join(args)}")
        elif args:
            result.append(f"{', '.join({str(item) for item in args})}")
        elif kwargs:
            result.append(f"{', '.join({str(item) for item in kwargs.values()})}")
        print(f"{' '.join(result)}...")
        return func_result
    return info


@logger
def print_arg(arg):
    print(arg)


@logger
def sum(a, b):
    return a+b


@logger
def concat(*a, **kwa):
    a = list([str(item) for item in a])
    a.extend([str(item) for item in kwa.values()])
    return "".join(a)


# Task 6
from copy import deepcopy
from random import choice


def randomWord(data):
    copy = set(data.copy())
    if len(data) == 0:
        while True:
            yield None
    while True:
        element = choice(data)
        print(element)
        yield element
        if len(data) == 0:
            data = copy