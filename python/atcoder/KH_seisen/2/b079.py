# https://atcoder.jp/contests/abc079/tasks/abc079_b
n = int(input())
luc = [0] * (n + 2)
luc[0] = 2
luc[1] = 1
for i in range(2, n + 1):
    luc[i] = luc[i - 1] + luc[i - 2]

print(luc[n])
