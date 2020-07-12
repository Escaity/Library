x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

pN = [i for i in range(102) if i not in p]
pNm = [abs(i - x) for i in pN]
pmin = min(pNm)
print(pN[pNm.index(pmin)])

"""
6 5
4 7 10 6 5

10 5
4 7 10 6 5
out:
8
"""
"""
入力を簡略化できる（x, nが1文字ずづ、それ以降は*pに代入される)
x, n, *p = list(map(int, open(0).read().split()))
"""
