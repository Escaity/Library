import math
from collections import Counter

n = int(input())
s = [Counter(list(input())) for _ in range(n)]
# a-zの最小出現回数を格納するリスト
a = [math.inf] * 26
# a-zの要素がn回出現したかを判定するリスト
flag = [0] * 26
ans = ""
for i in s:
    ke = list(i.keys())
    val = list(i.values())
    for j, k in enumerate(ke):
        # カウンタの要素keyでa-zの出現回数（＆全ての要素にa-zが含まれているか）を計算
        a[ord(k) - 97] = min(a[ord(k) - 97], val[j])
        flag[ord(k) - 97] += 1
for v in range(len(a)):
    if a[v] != math.inf and flag[v] >= n:
        ans += a[v] * chr(97 + v)

print(ans)

"""
# 別解：論理積を用いる方法

from collections import Counter
N = int(input())
C = Counter(input())

# 最初のカウンターと次のカウンターの要素の論理積をとり、最小の共通要素を求める
for n in range(N - 1):
    C &= Counter(input())
# element関数でvalueの数だけkeyの値を繰り返し出力するリストを作成
# ソートした後、*で要素のみ抽出、sep=""で文字列化する
print(*sorted(C.elements()), sep="")
"""
