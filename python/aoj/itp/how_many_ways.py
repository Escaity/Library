import itertools

while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break

    N = [i for i in range(1, n + 1)]
    perm = list(itertools.combinations(N, 3))
    # print(perm)
    cnt = 0
    for i in perm:
        if sum(list(i)) == x:
            cnt += 1
    print(cnt)
