# https://atcoder.jp/contests/abc054/tasks/abc054_a
a, b = map(int, input().split())
if a == 1:
    a = 14
if b == 1:
    b = 14
if a == b:
    print("Draw")
else:
    print("Alice") if a > b else print("Bob")
