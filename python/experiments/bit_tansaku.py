# https://atcoder.jp/contests/abc128/submissions/14937369

"""
2 2
2 1 2
1 2
0 1
1
"""
N, M = map(int, input().split())
K = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))

a = 0
for bit in range(1 << N):
    flag = True
    for i in range(M):
        c = 0
        for j in K[i][1:]:
            if bit & (1 << (j - 1)):
                c += 1
        if c % 2 != P[i]:
            flag = False
            break
    if flag:
        a += 1

print(a)
