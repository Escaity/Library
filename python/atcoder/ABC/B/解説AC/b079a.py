#リュカ数
n = int(input())
a1, a2 = 2, 1
for _ in range(n):
    a1, a2 = a2, a1+a2
print(a1)