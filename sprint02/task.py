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


def morse_number(words):
    answer = ''
    data = '1.---- 2..--- 3...-- 4....- 5..... 6-.... 7--... 8---.. 9----. 0-----'
    for el in words:
        for i in data.split():
            if el == i[0]:
                if answer == '':
                    answer = i[1:6]
                else:
                    answer = answer + ' ' + i[1:6]
    return answer


# Task 3
import re
from math import sqrt



def figure_perimetr(data):
    coords = re.findall(r'\d*\d', data)
    coords = [int(el) for el in coords]

    AB = sqrt((coords[2] - coords[0]) ** 2 + (coords[3] - coords[1]) ** 2)
    AC = sqrt((coords[4] - coords[0]) ** 2 + (coords[5] - coords[1]) ** 2)
    CD = sqrt((coords[6] - coords[4]) ** 2 + (coords[7] - coords[5]) ** 2)
    BD = sqrt((coords[6] - coords[2]) ** 2 + (coords[7] - coords[3]) ** 2)

    answer = AB + AC + CD + BD
    return float("{0:.14f}".format(answer))


# Task 4


import re


def pretty_message(data):
    return re.sub(r'([a-z]+?)\1+', r'\1', data)


# Task 5
import re


def max_population(data):
    info = []
    population = []
    result = ()

    for el in data:
        try:
            a = re.search(r'[a-z]{2}(_)[a-z]*(,)\d*', el).group()
        except AttributeError:
            a = re.search(r'[a-z]{2}(_)[a-z]*(,)\d*', el)
        if a is None:
            continue
        else:
            info.append(a)

    for i in info:
        b = re.search(r'\d{5}', i).group()
        population.append(b)

    if max(population) in info[0]:
        result = info[0][0:-6], int(max(population))

    return result
