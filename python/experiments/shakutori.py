n = 6
x = 12
a = [5, 3, 8, 6, 1, 4]

r = 0
res = 0
tot = 0

for l in range(n):
    while r < n and tot + a[r] <= x:
        tot += a[r]
        r += 1

    res += r - l

    if r == l:
        r += 1
    else:
        tot -= a[l]

print(res)
