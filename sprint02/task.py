# Task 1


def double_string(data):
    counter = 0
    answer = []
    for str in data:
        for el in data:
            answer.append(str + el)
        if str in set(answer):
            counter += 1
    return counter


# Task 2


def morse_number(data):
    answer = ''
    code = '-----'
    for el in data:
        el = int(el)
        if 1 <= el <= 5:
            code = code.replace('-' * el, '.' * el, 1)
        elif 6 <= el <= 9:
            code = '.....'
            code = code.replace('.' * (el - 5), '-' * (el - 5), 1)
        answer += ' ' + code
    return answer.strip()

    # Other example of current task
    #
    # answer = ''
    # data = '1.---- 2..--- 3...-- 4....- 5..... 6-.... 7--... 8---.. 9----. 0-----'
    # for el in words:
    #     for i in data.split():
    #         if el == i[0]:
    #             answer = answer + ' ' + i[1:6]
    # return answer[1:]


print(morse_number("295"))
# Task 3


import re
from math import sqrt


def figure_perimetr(data):
    data = re.findall(r'\d*\d', data)
    data = [int(el) for el in data]
    answer = sqrt((data[2] - data[0]) ** 2 + (data[3] - data[1]) ** 2) + \
             sqrt((data[4] - data[0]) ** 2 + (data[5] - data[1]) ** 2) + \
             sqrt((data[6] - data[4]) ** 2 + (data[7] - data[5]) ** 2) + \
             sqrt((data[6] - data[2]) ** 2 + (data[7] - data[3]) ** 2)

    return float("{0:.14f}".format(answer))


# Task 4


import re


def pretty_message(data):
    return re.sub(r'([a-z]+?)\1+', r'\1', data)


# Task 5


import re


def max_population(data):
    items = re.findall(r'([a-z]{2}_[a-z]+),(\d+)', ' '.join(data))
    capital = [el[1] for el in items]
    for item in items:
        if max(capital) in item[1]:
            return item[0], int(max(capital))
