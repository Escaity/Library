N, L = list(map(int, input().split()))
aji = []
for i in range(1, N + 1):
    aji.append(L + i - 1)
if 0 in aji:
    print(sum(aji))
elif min(aji) < 0:
    print(sum(aji) - max(aji))
else:
    print(sum(aji) - min(aji))
