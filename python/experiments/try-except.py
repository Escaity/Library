a = [1, 3, 4, 5, 9]
flag = True
try:
    print(a.index(2))
# 例外が発生したとき
except ValueError:
    flag = False
# 例外が発生しなかったとき
else:
    pass
print(flag)
