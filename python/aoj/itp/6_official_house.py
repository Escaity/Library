f1 = [[0] * 10 for _ in range(3)]
f2 = [[0] * 10 for _ in range(3)]
f3 = [[0] * 10 for _ in range(3)]
f4 = [[0] * 10 for _ in range(3)]
n = int(input())
b, f, r, v = 0, 0, 0, 0
# b, f, r, v = [] * n, [] * n, [] * n, [] * n
for i in range(n):
    # b[i], f[i], r[i], v[i] = map(int, input().split())
    b, r, f, v = map(int, input().split())
    if b == 1:
        f1[r - 1][f - 1] += v
        if f1[r - 1][f - 1] > 9:
            f1[r - 1][f - 1] == 9
        elif f1[r - 1][f - 1] < 0:
            f1[r - 1][f - 1] == 0

    elif b == 2:
        f2[r - 1][f - 1] += v
        if f2[r - 1][f - 1] > 9:
            f2[r - 1][f - 1] == 9
        elif f2[r - 1][f - 1] < 0:
            f2[r - 1][f - 1] == 0
    elif b == 3:
        f3[r - 1][f - 1] += v
        if f3[r - 1][f - 1] > 9:
            f3[r - 1][f - 1] == 9
        elif f3[r - 1][f - 1] < 0:
            f3[r - 1][f - 1] == 0
    elif b == 4:
        f4[r - 1][f - 1] += v
        if f4[r - 1][f - 1] > 9:
            f4[r - 1][f - 1] == 9
        elif f4[r - 1][f - 1] < 0:
            f4[r - 1][f - 1] == 0
for i in f1:
    print("", *i, sep=" ")
print("#" * 20)
for i in f2:
    print("", *i, sep=" ")
print("#" * 20)
for i in f3:
    print("", *i, sep=" ")
print("#" * 20)
for i in f4:
    print("", *i, sep=" ")
