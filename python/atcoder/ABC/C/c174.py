"""
エイシングプロコンc問題
"""

n = int(input())
xyz = [0] * ((10 ** 4) + 1)
for x in range(1, (10 ** 2) + 1):
    for y in range(1, (10 ** 2) + 1):
        for z in range(1, (10 ** 2) + 1):
            v = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + x * z - 1
            if v < 10 ** 4 + 1:
                xyz[v] += 1
for i in range(n):
    print(xyz[i])

"""
# 　私がやりたかったことに近かった模範例
n = int(input())
ls = [0] * n
x, y, z = 1, 1, 1
p = 6
m = int(n ** 0.5)
for x in range(1, m + 3):
    for y in range(1, x + 1):
        for z in range(1, y + 1):
            k = 6
            if x == y or y == z:
                k = 3
                if x == z:
                    k = 1
            j = x * x + y * y + z * z + x * y + y * z + x * z
            if j <= n:
                ls[j - 1] += k
            else:
                break
for i in ls:
    print(i)
"""
