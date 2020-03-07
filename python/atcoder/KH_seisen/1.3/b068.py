# https://atcoder.jp/contests/abc068/tasks/abc068_b
n = int(input())
if n < 2 ** 1:
    print(2**0)
elif n < 2 ** 2:
    print(2 ** 1)
elif n < 2 ** 3:
    print(2 ** 2)
elif n < 2 ** 4:
    print(2 ** 3)
elif n < 2 ** 5:
    print(2 ** 4)
elif n < 2 ** 6:
    print(2 ** 5)
elif n <= 100:
    print(2 ** 6)

"""
n=int(input())
ans=1
for i in range(7):
    if 2**i<=n:ans=2**i
print(ans)
"""