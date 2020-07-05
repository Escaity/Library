import collections

n = int(input())
words = list(input() for _ in range(n))
print(len(set(words)))

wc = collections.Counter(words)
print(*wc.values())
