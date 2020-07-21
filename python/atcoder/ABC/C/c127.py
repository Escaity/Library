k, g = map(int, input().split())
id = [map(int, input().split()) for i in range(g)]
# リストidを左と右で分割してl,rに格納
l, r = list(zip(*id))
# ゲートの区間に重複があれば計算した値を、そうでなければ0を表示
print(min(r) - max(l) + 1) if min(r) - max(l) >= 0 else print(0)
