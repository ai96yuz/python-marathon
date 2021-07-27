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
    data = {'1.----', '2..---', '3...--', '4....-', '5.....', '6-....', '7--...', '8---..', '9----.', '0-----'}
    for el in words:
        for i in data:
            if el == i[0]:
                if answer == '':
                    answer = i[1:6]
                else:
                    answer = answer + ' ' + i[1:6]
    return answer


# Task 3
import math


def figure_perimetr(data):
    x = []
    a = data.split('#')
    for el in a:
        if el == '':
            continue
        else:
            x.append(el)
    print(x)
    x1, y1, x2, y2 = int(x[0][-1]), int(x[1][-1]), int(x[2][-1]), int(x[3][-1])
    print('x1, y1, x2, y2: ', x1, y1, x2, y2)
    a = (x2 - x1) ** 2
    print('(x2 - x1) ** 2: ', a)
    b = (y2 - y1) ** 2
    print('(y2 - y1) ** 2: ', b)
    print('{} + {}: '.format(a, b), a + b)
    print('math.sqrt({}): '.format(a + b), math.sqrt(a + b))

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))
# test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
# print(figure_perimetr(test2))

# Task 4


import re


def pretty_message(data):
    # e = re.sub(r'(\w)\1{1:}', '', data)

    word = data.split(' ')
    for i in word:
        # x = re.split(r'(\w)(\w)(\w)\1\2\3\w +', i)
        # x = re.sub(r'(\w)\1{1:}', i)
        # print(x)
        for x in i:
            if x == x in i:
                i.replace(x, '')

        # if word.count(i) > 1:
        #     word.remove(i)
    return word
    # x = re.findall('a-z | a-z', txt)
    # print(x)
    # for el in data:
    #     if el == el + el:
    #         data.replace(el, '')
    # return data


# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))


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
