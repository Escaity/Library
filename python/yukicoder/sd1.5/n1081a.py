n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    a = [a[i - 1] + a[i] for i in range(1, len(a))]
print(a[0] % 1000000007)
