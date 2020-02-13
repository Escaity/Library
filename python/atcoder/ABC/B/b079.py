n = int(input())
def luc(a, b, n):
    if n > 0:
        return luc(b,a+b,n-1)
    else:
        return a
print(luc(2,1,n))
