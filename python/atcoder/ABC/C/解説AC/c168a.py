import math

a, b, h, m = list(map(int, input().split()))

ca = (h * 60 + m) / 720 * (2 * math.pi)
cb = m / 60 * (2 * math.pi)
t = ca - cb
ans = math.sqrt(a * a + b * b - 2.0 * a * b * math.cos(t))
print(ans)
