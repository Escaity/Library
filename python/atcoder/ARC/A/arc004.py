import time
N = int(input())
a = [list(map(int, input().split())) for i in range(N)]
start = time.time()

dist = []
for i, v in enumerate(a, start=1):
    x1, y1 = v[0], v[1]
    for w in a[i:]:
        x2, y2 = w[0], w[1]
        d = ((abs(x1 - x2)) ** 2 + (abs(y1 - y2)) ** 2) ** 0.5
        dist.append(d)

print(max(dist))
elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
