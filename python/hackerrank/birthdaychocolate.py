def birthday(s, d, m):
    n = len(s)
    cnt = 0
    for i in range(n - m + 1):
        bar = 0
        for j in range(i, i + m):
            bar += s[j]
        if bar == d:
            cnt += 1

    return cnt
