import random

N = int(input())

for i in range(N):
    print("%d %d" % (random.randint(0, 100), random.randint(0, 100)))

