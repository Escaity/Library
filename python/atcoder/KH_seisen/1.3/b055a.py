n = int(input())
p = 1
for i in range(1, n + 1):
    p = p * i % 1000000007

print(p)
