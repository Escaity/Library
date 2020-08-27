"""
ポイント
1 100のとき10000だと２回100で割れるので☓　10100となる
"""
D, N = map(int, input().split())
if N < 100:
    print(N * 100 ** D)
else:
    print(101 * 100 ** D)

