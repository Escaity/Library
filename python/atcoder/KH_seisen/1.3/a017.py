# https://atcoder.jp/contests/abc017/tasks/abc017_1
s, e = [0] * 3, [0] * 3
ans = 0
for i in range(3):
    s[i], e[i] = map(int, input().split())
    ans += round((s[i] * e[i]) / 10)
print(ans)
