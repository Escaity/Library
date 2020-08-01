n = int(input())
s = list(input())
ans = 0
for i in range(n - 1):
    sl = set(s[: i + 1])
    sr = set(s[i + 1 :])
    # 左側slと右側srの論理積をとることで共通要素がだせる
    common = len(sl & sr)
    # 最大値が見つかるごとに更新していく
    ans = max(common, ans)
print(ans)
