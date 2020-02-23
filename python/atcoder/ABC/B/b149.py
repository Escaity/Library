a, b, k = map(int, input().split())
taka = a - k
if taka < 0:
    b = b + taka
    taka = 0
    if b < 0:
        b = 0
print(taka, b)
