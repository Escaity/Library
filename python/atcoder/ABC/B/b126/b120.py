# 2数の共通する約数を列挙する関数
def com_div(x, y):
    dv = []
    # range(min, 0, -1)とすることでminから1まで-1ずつループ
    # これで作成したリストをreverseする必要がなくなる
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            dv.append(i)
    return dv


a, b, k = list(map(int, input().split()))
print(com_div(a, b)[k - 1])
