n = int(input())
s = input().split()
a = []
for i in range(n):
    a += s[i]
    a = a[::-1]
print(" ".join(a))