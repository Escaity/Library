import sys

n, m = list(map(int, input().split()))
sc = [None] * n
ans = 0
for i in range(m):
    s, c = list(map(int, input().split()))
    if sc[s - 1] is None or sc[s - 1] == c:
        sc[s - 1] = c
    else:
        print(-1)
        sys.exit()
r = [[1], [1, 10], [1, 10, 100]]
if ans == 0 and sc[0] != 0:
    for i in range(n):
        if sc[i] is None:
            sc[i] = 0
    for j, v in enumerate(r[n - 1]):
        ans += sc[n - j - 1] * v
    if len(str(ans)) != n:
        ans = -1
elif n == 1:
    ans = 0
else:
    ans = -1
print(ans)
