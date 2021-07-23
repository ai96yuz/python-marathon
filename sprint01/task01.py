def kthTerm(n, k):
    resultList = [1]
    step = 0
    while len(resultList) <= k:
        step += 1
        resultList.append(n ** step)
        lenght = len(resultList) - 1
        for i in range(0, lenght, 1):
            resultList.append(n ** step + resultList[i])
    return resultList[k-1]


print(kthTerm(3, 4))