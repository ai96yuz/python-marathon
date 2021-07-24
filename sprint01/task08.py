def studying_hours(a):
    counter = 0
    for x, y in zip(a, a[1:]):
        if x <= y:
            counter += 1
        elif x > y:
            continue
    return counter

    # for index, value in enumerate(a):
    #     print(index)
    #     print(value)
    #     if value <= value in index+1:
    #         counter += 1
    #         # if a[i] > a[i+1]:
    #         #     counter = 0
    #     elif value > value + 1:
    #         continue
    #     else:
    #         break
    # return counter