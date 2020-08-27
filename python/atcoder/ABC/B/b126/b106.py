n = int(input())
ans = 0
oddl = list(map(int, (i for i in range(1, n, 2))))


def eight(n):
    i = 1
    cnt = 0
    while i <= n:
        if n % i == 0:
            cnt += 1
        i += 1
    if i == 8:
        return 1
    else:
        return 0


for i in oddl:
    ans += eight(i)
print(ans)
