n = int(input())
ans = float("inf")
for i in range(1, int(n ** 0.5) + 1):
    d = n // i
    ans = min(abs(d - i) + (n - d * i), ans)

print(ans)
