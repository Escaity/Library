n = int(input())
a = list(map(int, input().split()))
cnt = 0

for i, tgt in enumerate(a, 1):
    # 要素の数と番号が対応すればカウント+
    if a[tgt - 1] == i:
        cnt += 1
# ペアの重複計算をはじいて表示
print(cnt // 2)

"""
4
2 1 4 3
"""
