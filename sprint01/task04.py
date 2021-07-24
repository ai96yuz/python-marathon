def findPermutation(n, p, q):
    r = []
    i = 0
    for p, q in range(0, n):
        r.append(p.index(q[i]))
        i +=1