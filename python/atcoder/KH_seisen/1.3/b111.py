# https://atcoder.jp/contests/abc111/tasks/abc111_b
n = int(input())
while n % 111 != 0:
    if n % 111 and (n // 100) * 111 >= n:
        break
    else:
        n = (n // 100) * 111 + 111
print(n)

"""
N=int(input())
print((((N-1)//111)+1)*111)
"""
