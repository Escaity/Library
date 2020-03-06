# https://atcoder.jp/contests/abc073/tasks/abc073_b
n = int(input())
sum = 0
l, r = [0] * n, [0] * n
for i in range(n):
    l[i], r[i] = list(map(int, input().split()))
for i in range(n):
    sum += r[i] - l[i] + 1

print(sum)
