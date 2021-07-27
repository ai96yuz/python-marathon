# Task 1

def kthTerm(n, k):
    resultList = [1]
    step = 0
    while len(resultList) <= k:
        step += 1
        resultList.append(n ** step)
        length = len(resultList) - 1
        for i in range(0, length, 1):
            resultList.append(n ** step + resultList[i])
    return resultList[k - 1]


# Task 2


def filterBible(scripture, book, chapter):
    scrip = []
    for el in scripture:
        if el[:2] == book and el[2:5] == chapter:
            scrip.append(el)
    return scrip


# Task 3


def isPalindrome(str):
    counts = {}
    for c in str.lower():
        if c.isalpha():
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    odd_counts = [count for count in counts.values() if count % 2 == 1]
    return len(odd_counts) < 2


# Task 4


def findPermutation(n, p, q):
    r = []
    for x in q:
        permutation = (1 + p.index(x))
        r.append(permutation)
    return r


# Task 5


def toPostFixExpression(expression):
    answer = []
    stack = []
    precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1}
    for element in expression:
        if element.isdigit():
            answer.append(element)
            continue
        if element == '(':
            stack.append(element)
            continue
        if element == ')':
            while True:
                temp = stack.pop()
                if temp == '(':
                    break
                else:
                    answer.append(temp)
            continue
        while (
                stack
                and stack[-1] != '('
                and precedence[stack[-1]] >= precedence[element]
        ):
            answer.append(stack.pop())
        stack.append(element)
    answer.extend(stack[::-1])
    return answer


# Task 6


def order(a):
    if a == sorted(a):
        return "ascending"
    elif a == sorted(a, reverse=True):
        return "descending"
    else:
        return "not sorted"


# Task 7


def Cipher_Zeroes(N):
    zero = {digit: 0 for digit in '123457'}
    zero.update({digit: 1 for digit in '069'})
    zero['8'] = 2
    binary = sum(zero[digit] for digit in N)
    if binary == 0:
        return 0
    if binary % 2:
        binary += 1
    else:
        binary -= 1
    return bin(binary)[2:]


# Task 8


def studying_hours(a):
    length = 1
    max_length = 1
    for x, y in zip(a, a[1:]):
        if x <= y:
            length += 1
            max_length = max((length, max_length))
        else:
            length = 1
    return max_length
