n = int(input())
x = list(map(int, input().split()))
xs = sorted(x)
for i in x:
    # Xiが中央値より小さいなら
    if i < xs[n // 2]:
        # 中央値を表示
        print(xs[n // 2])
    else:
        # 中央値の1つ前(小さい方)を表示
        print(xs[n // 2 - 1])

"""
4
2 4 4 3
"""
