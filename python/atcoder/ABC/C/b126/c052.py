n = int(input())
cnt = [0] * 1005
for i in range(2, n + 1):
    now = i
    for j in range(2, now + 1):
        while now > 0 and now % j == 0:
            cnt[j] += 1
            now //= j
ans = 1
for i in range(n + 1):
    if cnt[i] != 0:
        ans *= cnt[i] + 1
        ans %= 10 ** 9 + 7

print(ans)
