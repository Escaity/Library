# https://atcoder.jp/contests/abc013/tasks/abc013_2
A = [0] * 10
num = [0] * 2
for i in range(2):
    num[i] = int(input())
num.sort()
for i in range(num[0], num[1]):
    A[i] = 1
print(min(A.count(0), A.count(1)))
"""
x=abs(int(input())-int(input()))
print(min(x,10-x))
"""
