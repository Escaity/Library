n = int(input())
A = list(map(int, input().split()))

res = 0
r = 1
for l in range(n):
    while r < n and (r <= l or A[r - 1] < A[r]):
        r += 1
    res += r - l
    if l == r:
        r += 1

print(res)
