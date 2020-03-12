s = int(input())
m = s // 60
h = m // 60
print(h, m - h * 60, s - m * 60, sep=":")
