def enum_div(n):
    ldv, udv = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ldv.append(i)
            if i != n // i:
                udv.append(n // i)
    i += 1
    return ldv + udv[::-1]


print(enum_div(12))
