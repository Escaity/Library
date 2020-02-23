N = int(input())
Temp, A = list(map(int, input().split()))
H = list(map(float, input().split()))
k = 0
target = float("inf")
n = []
for i, v in enumerate(H, start=1):
    k = Temp - v * float(0.006)
    if target > abs(k - A):
        target = abs(k - A)
        n.append(i)

print(n[-1])
