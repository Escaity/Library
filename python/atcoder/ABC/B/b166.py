n, k = list(map(int, input().split()))
kl = [[] for _ in range(k)]
for i in range(k):
    _ = int(input())
    d = list(map(int, input().split()))
    kl[i].append(d)
# 3次元配列klをsum関数で1次元に変換してsetでお菓子を持ってる人を特定
f1 = set(sum(sum(kl, []), []))
# 全員の集合
r = set(i for i in range(1, n + 1))
# rとf1の差集合を求めてお菓子を持ってない人の数を表示
print(len(r - f1))
