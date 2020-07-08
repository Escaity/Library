import math


def minimumDistances(a):
    n = len(a)
    # 求める距離を無限で初期化
    dst = math.inf
    # 文字列の組み合わせを調べる
    for i in range(n):
        for j in range(i + 1, n):
            # 数字のペアが見つかったら絶対距離をdstに格納（最小距離を更新していく)
            if a[i] == a[j]:
                dst = min(dst, abs(j - i))
    # 数字ペアが見つからなかったときは dstに-1を代入
    if dst == math.inf:
        dst = -1
    return dst
