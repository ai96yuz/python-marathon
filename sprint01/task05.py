def toPostFixExpression(e):
    stack = []
    symb = []
    operators = set(['-', '*', '+', '/', '%'])
    miss = set([')', '('])
    # e = e[::-1]
    for i in e:
        if i in operators:
            stack.append(i)
        elif i in miss:
            continue
        else:
            symb.append(i)

    return symb + stack
