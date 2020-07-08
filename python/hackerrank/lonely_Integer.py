from collections import Counter

# カウント数最小のキーを返す
def lonelyinteger(a):
    c = Counter(a)
    d = c.most_common()
    return d[-1][0]
