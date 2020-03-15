# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_a

*s, t = map(int, input().split())
s.sort()
f = False
for i in range(s[0], s[1] + 1):
    if i == t:
        f = True
print("Yes") if f else print("No")
