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


def logger(funcDecorator):
    def wrapper(*args, **kwargs):
        data = ''
        print('Executing of function ' + funcDecorator.__name__ + ' with arguments ', end='')
        for arg in args:
            data += str(arg) + ", "
        for kwarg in kwargs.values():
            data += str(kwarg) + ", "
        print(data[:-2] + "...")
        return funcDecorator(*args, **kwargs)

    return wrapper


@logger
def concat(*args, **kwargs):
    data = ''
    for arg in args:
        data = data + str(arg)
    for kwarg in kwargs.values():
        data += str(kwarg)
    return data


@logger
def sum(a, b):
    return a + b


def print_arg(arg):
    print(arg)

    @logger
    def print_arg(arg):  # имя не совпадало )))
        pass

    print_arg(arg)


# Task 6
from random import choice


def randomWord(data):
    if len(data) == 0:
        while True:
            yield None
    data_saved = data.copy()
    while True:
        el = choice(data_saved)
        yield el
        data_saved.remove(el)
        if len(data_saved) == 0:
            data_saved = data.copy()
