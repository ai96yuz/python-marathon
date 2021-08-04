# Task 1


class Employee(object):
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, employee_string):
        firstname, lastname, salary = map(str, employee_string.split('-'))
        person = cls(firstname, lastname, salary)
        return person


# Task 2


class Pizza(object):
    order = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order

    @classmethod
    def hawaiian(cls):
        return Pizza(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return Pizza(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return Pizza(['spinach', 'olives', 'mushroom'])


# Task 3


class Employee:
    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split(' ')

        for name, value in kwargs.items():
            setattr(self, name, value)


# Task 4


class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
        self.passmark = int(pass_mark[0: -1])


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'
        self.total_result = {}

    def take_test(self, Testpaper, answers):
        i = 0
        correct_answer = 0
        total_marks = 0
        test_result = ''

        for answer in Testpaper.markscheme:
            if answer == answers[i]:
                correct_answer += 1
            i += 1
        total_marks = round((correct_answer / i) * 100)

        if total_marks >= Testpaper.passmark:
            test_result = 'Passed!'
        else:
            test_result = 'Failed!'

        self.total_result[Testpaper.subject] = test_result + ' (' + str(total_marks) + '%)'
        self.tests_taken = self.total_result


# Task 5


class Gallows():
    def __init__(self, words=[], game_over=False):
        self.words = words
        self.game_over = game_over

    def play(self, word):
        if not self.words:
            self.words.append(word)
            return self.words

        if word not in self.words and self.words[-1][-1] == word[0]:
            self.words.append(word)
            return self.words
        self.game_over = True
        return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'
