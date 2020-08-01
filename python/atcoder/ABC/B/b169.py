n = int(input())
a = list(map(int, input().split()))
mul = 1
# リスト内に0がある場合は0を返すことで計算量を減らす
if 0 in a:
    mul = 0

for i in a:
    mul *= i
    if mul > 10 ** 18:
        mul = -1
        break
print(mul)
