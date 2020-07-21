n = int(input())
a = list(map(int, input().split()))
r, cnt = 1, 0
# レンガ砕けるか判定
for i in a:
    # もしレンガの番号と位置が同じなら番号+1
    if r == i:
        r += 1
    # 異なるならレンガを砕く
    else:
        cnt += 1
# 答えが存在しないなら-1を表示
print(cnt) if a.count(1) else print(-1)
