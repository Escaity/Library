import itertools

N, X = list(map(int, input().split()))
B = list(map(int, input().split()))
Ba = list(itertools.accumulate(B))
cnt = 1
for i in Ba:
    if i <= X:
        cnt += 1
print(cnt)
