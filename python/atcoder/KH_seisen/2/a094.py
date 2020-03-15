# https://atcoder.jp/contests/abc094/tasks/abc094_a
cat, cd, t = map(int, input().split())
f = False
if cat <= t and cd > 0 and cat + cd >= t:
    f = True
print("YES") if f else print("NO")
