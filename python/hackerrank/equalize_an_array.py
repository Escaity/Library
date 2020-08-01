from collections import Counter

n = int(input())
a = list(map(int, input().split()))
ac = Counter(a)
print(n - ac.most_common()[0][1])
