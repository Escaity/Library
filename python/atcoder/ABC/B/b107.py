h, w = map(int, input().split())
m = [[] for _ in range(h)]
# 横x、縦yに#があればTrueを格納する
x = [False] * h
y = [False] * w
for i in range(h):
    m[i] = list(input())
    if "#" in m[i]:
        x[i] = True
# 元のマップを転置して縦yに#が存在するか調べる
zm = list(zip(*m))
for i, j in enumerate(zm):
    if "#" in j:
        y[i] = True
M = []
for i, H in enumerate(x):
    for v, W in enumerate(y):
        # 縦横どちらにも#が存在すればそのマップ位置の文字を追加
        if H and W:
            M.append(m[i][v])
    # 空文字列を除く
    if M:
        print("".join(M))
    M = []
