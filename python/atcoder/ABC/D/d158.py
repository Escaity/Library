"""
先頭と末尾でリストを操作するためdequeを使う
ループの度に文字列を反転するとTLEするので
rev（bool)で文字列が反転したかしてないかを判定する
ことで高速化を図る。
"""
from collections import deque

s = deque(list(input()))
n = int(input())
q = [list(input().split()) for _ in range(n)]
rev = False

for tfc in q:
    # t==1の時はrevフラグを反転させる
    if tfc[0] == "1" and rev is False:
        rev = True
    elif tfc[0] == "1" and rev is True:
        rev = False

    # t==2の時は文字列操作を行う
    # rev == Falseならデフォルト（そのまま操作する）
    # rev == Trueならその逆に操作する
    elif rev is False:
        if tfc[1] == "1":
            s.appendleft(tfc[2])
        else:
            s.append(tfc[2])
    elif rev is True:
        if tfc[1] == "1":
            s.append(tfc[2])
        else:
            s.appendleft(tfc[2])
# 反転状態であれば、文字列を反転する
if rev:
    s.reverse()
print("".join(s))

"""
a
6
2 2 a
2 1 b
1
2 2 c
1
1
"""
