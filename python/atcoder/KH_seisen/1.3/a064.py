# https://atcoder.jp/contests/abc064/tasks/abc064_a

r, g, b = map(int, input().split())
digit = r * 100 + g * 10 + b
print("YES") if digit % 4 == 0 else print("NO")


