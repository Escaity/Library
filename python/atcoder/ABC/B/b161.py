n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt = 0
ttl = sum(a)
for i in a:
    # 小数点を切り捨てない割り算をしないと答えが合わない（//だと切り捨て)
    if i >= ttl / (4 * m):
        cnt += 1
print("Yes") if cnt >= m else print("No")
