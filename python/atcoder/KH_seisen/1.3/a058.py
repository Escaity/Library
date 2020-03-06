# https://atcoder.jp/contests/abc058/tasks/abc058_a
a, b, c = list(map(int, input().split()))
print("YES") if b - a == c - b else print("NO")
