cnt = 0
for i in range(12):
    n = list(set(list(input())))
    cnt += n.count("r")
print(cnt)

"""
print("r" in input())
"""
