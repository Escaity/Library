n, m, c = list(map(int, input().split()))
B = list(map(int, input().split()))
A = (list(map(int, input().split())) for _ in range(n))
ans = 0
cnt = 0
for i, u in enumerate(A):
    for j, v in enumerate(u):
        ans += v * B[j]

    ans += c
    if ans > 0:
        cnt += 1
    ans = 0
print(cnt)
