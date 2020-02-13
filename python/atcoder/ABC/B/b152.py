a, b = list(map(int, input().split()))

if b < a:
    a, b = b, a

for i in range(b):
    print(str(a), end="")
print()
