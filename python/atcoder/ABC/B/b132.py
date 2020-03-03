"""
5
1 3 5 4 2

1 2 3
3 2 1
"""
N = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(2, N):
    if max(a[i - 2], a[i - 1]) == min(a[i - 1], a[i]) or min(a[i - 2], a[i - 1]) == max(a[i - 1], a[i]):
        if a[i-2] != a[i-1] or a[i-1] != a[i]:
            cnt += 1

print(cnt)