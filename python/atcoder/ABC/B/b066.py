s = list(input())
while s:
    # リスト末尾の一文字を消す
    s = s[:-1]
    sl = len(s)
    # 偶文字列になるのはリストの長さが偶数の時
    if sl % 2 == 0:
        s1 = s[0 : sl // 2]
        s2 = s[sl // 2 :]
        # 前半分、後半分の要素が等しくなったら答えを表示
        if s1 == s2:
            print(sl)
            break


"""
akasakaakasakasakaakas
"""
