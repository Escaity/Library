# https://atcoder.jp/contests/abc121/tasks/abc121_b
N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = (list(map(int, input().split())) for _ in range(N))
ans, cnt = 0, 0
for v in A:
    for i, w in enumerate(v):
        ans += w * B[i]
    if ans + C > 0:
        cnt += 1
    ans = 0
print(cnt)
