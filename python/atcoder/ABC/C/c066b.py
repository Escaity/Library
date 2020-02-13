n = int(input())
*a, = map(int, input().split())

right = a[1::2]
right.reverse()
left =  a[0::2]

b = []
b.extend(right)
b.extend(left)

if n%2 == 1:
    b.reverse()

print(*b)
