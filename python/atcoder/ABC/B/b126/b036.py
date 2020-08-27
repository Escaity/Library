n = int(input())
m = [list(input()) for _ in range(n)]
mz = list(zip(*m))
for i in mz:
    i = i[::-1]
    print("".join(i))
