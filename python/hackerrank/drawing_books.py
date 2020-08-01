def pageCount(n, p):
    book = [[] for _ in range((n // 2 + 1))]
    t = [False] * (n // 2 + 1)

    for i in range(0, n + 1, 2):
        if i + 1 < n and i != 0:
            if i == p or i + 1 == p:
                t[i // 2] = True
        elif i == 0:
            if i + 1 == p:
                t[i // 2] = True
        else:
            if i == p:
                t[i // 2] = True

    return min(int(t.index(True)) - 0, len(t) - 1 - int(t.index(True)))
