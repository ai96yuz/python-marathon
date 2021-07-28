# Task 1


def outer(name):
    def inner():
        print('Hello, {}!'.format(name))
    return inner


# Task 2


def create(name):
    return lambda x: 'True' if x == name else 'False'


# Task 3


# def create_account(user_name: str, password: str, secret_words: list):
#     def check():
#         answer = lambda x, y, z: 'True' if x == user_name and y == password and z == secret_words else 'False'
#         return answer
#     return check
#
#     # return lambda x, y, z: 'True' if x == user_name and y == password and z == secret_words else 'False'
#
#
#
# val1 = create_account("123", "qQ1!45", initial_arr)
# print(val1("qQ1!45", checked_arr_1_true))


# Task 4





# Task 5