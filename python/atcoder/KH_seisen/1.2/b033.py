# https://atcoder.jp/contests/abc033/tasks/abc033_b
N = int(input())
shi, p = [None] * N, [None] * N
for i in range(N):
    shi[i], p[i] = list(map(str, input().split()))
pm = list(map(int, p))
ph = max(pm)
phi = p.index(str(ph))
pop = sum(pm) - ph
if pop < ph:
    print(shi[phi])
else:
    print("atcoder")
