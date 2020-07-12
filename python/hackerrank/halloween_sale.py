# Test case x11 and x29
p, d, m, s = list(map(int, input().split()))
price = [m] * (s // m + 1)
price[0] = p
for i in range(len(price)):
    if price[i] - d > m:
        price[i + 1] = price[i] - d
    else:
        break
cnt = 0
for j in range(len(price)):
    if price[j] <= s:
        price[j + 1] = price[j] + price[j + 1]
        cnt += 1
    else:
        break

print(cnt)
