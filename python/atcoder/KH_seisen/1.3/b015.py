# https://atcoder.jp/contests/abc015/tasks/abc015_2
n = int(input())
A = list(map(int, input().split()))
print(-(-sum(A) // (n - A.count(0))))
