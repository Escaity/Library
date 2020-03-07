# https://atcoder.jp/contests/abc078/tasks/abc078_b
"""
12 3 1
"""
x, y, z = list(map(int, input().split()))
x -= z
cnt = 0
while x >= y + z:
    x = x - y - z
    cnt += 1
print(cnt)
"""
x,y,z=map(int,input().split())
print((x-z)//(y+z))
"""
