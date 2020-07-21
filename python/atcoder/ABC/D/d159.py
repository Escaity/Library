n = int(input())
a = list(map(int, input().split()))
l = (2 * 10 ** 5) + 1
b = [0] * l


def nC2(n):
    return n * (n - 1) // 2


# 要素とリストの番号を対応、要素の数を計算
for i in range(n):
    b[a[i]] += 1

ttl = 0
# ボールの全組み合わせを求める
for j in range(l):
    ttl += b[j] * (b[j] - 1) // 2

for k in range(n):
    # 全組み合わせ-k番目のボールを抜いた組み合わせ+???
    print(ttl - nC2(b[a[k]]) + nC2(b[a[k]] - 1))
