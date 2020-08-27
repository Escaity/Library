# 素因数分解を列挙
def primeFact(n):
    i = 2
    pl = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            pl.append(i)
        i += 1
    if n > 1:
        pl.append(int(n))
    return pl


a, b = map(int, input().split())
# a, bの共通する素因数の数+1が答え
print(len(set(primeFact(a)) & set(primeFact(b))) + 1)
