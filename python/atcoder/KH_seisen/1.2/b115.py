# https://atcoder.jp/contests/abc115/tasks/abc115_b
X = [int(input()) for _ in range(int(input()))]
maxX = max(X)
X.remove(maxX)
print(sum(X) + round(maxX / 2))
"""
l=[int(input()) for _ in range(int(input()))]
print(sum(l)-int(max(l)/2))
"""
