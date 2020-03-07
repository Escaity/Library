# https://atcoder.jp/contests/abc086/tasks/abc086_b
n = input().split()
x = int("".join(n)) ** 0.5
print("Yes") if x.is_integer() else print("No")
