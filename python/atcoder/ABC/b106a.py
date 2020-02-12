n = int(input())
nl = map(int, (i for i in range(1, n + 1, 2)))
ans = 0


def eight(num):
    i = 1
    cnt = 0
    while i <= num:
        if num % i == 0:
            cnt += 1
        i += 1
    if cnt == 8:
        return 1
    else:
        return 0


for i in nl:
    ans += eight(i)

print(ans)
