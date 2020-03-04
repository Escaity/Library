# https://atcoder.jp/contests/abc112/tasks/abc112_b

N, T = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
ans, sav = 1001, 0
for i in A:
    if i[1] <= T:
        sav = i[0]
        if ans > sav:
            ans = sav
if ans > 1000:
    ans = "TLE"
print(ans)
