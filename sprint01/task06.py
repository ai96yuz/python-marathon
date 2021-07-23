def order(a):
    if (a == sorted(a)):
        return "ascending"
    elif (a == sorted(a, reverse=True)):
        return "descending"
    else:
        return "not sorted"


print(order([10, 5, 4]))