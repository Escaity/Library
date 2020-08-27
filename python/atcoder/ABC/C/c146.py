"""
二分探索を用いる
"""
a, b, x = list(map(int, input().split()))


def is_ok(arg):
    return a * arg + b * len(str(arg)) <= x  # 条件を満たすならTrueを返す


def m_bisect(ng, ok):
    while abs(ok - ng) > 1:
        c = (ok + ng) // 2
        if is_ok(c):
            ok = c
        else:
            ng = c
    return ok


# 最大値+1をどんどん小さくしていって求めたい最大値を探すイメージ
print(m_bisect(10 ** 9 + 1, 0))

