def enum_div(n):
    dv = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dv.append(i)
            if i != n // i:
                dv.append(n // i)
    # dv.sort()
    return dv


a, b, c = list(map(int, input().split()))
ab = set([i for i in range(a, b + 1)])
cd = set(enum_div(c))
print(len(ab & cd))
