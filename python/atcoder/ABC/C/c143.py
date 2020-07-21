"""
10
aabbbbaaca
"""
n = int(input())
a = list(input())
cnt = 1
for i in range(n - 1):
    if a[i] != a[i + 1]:
        cnt += 1
print(cnt)
