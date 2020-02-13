import itertools

n = list(range(1, int(input()) + 1))
s1 = tuple(map(int, input().split()))
s2 = tuple(map(int, input().split()))
perm = list(itertools.permutations(n))
a = perm.index(s1)
b = perm.index(s2)

print(abs(a - b))
