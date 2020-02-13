N, submit = list(map(int, input().split()))
res = list(list(map(str, input().split())) for _ in range(submit))
ac_list = []
ac, wa = 0, 0
res_list = []
for i in res:
    res_list.append(i[1][:1])
    if i in ac_list:
        pass
    elif i[1] == "AC":
        ac_list.append(i)
        ac += 1

for i in range("".join(res_list).rfind("A")):
    if res[i][1] == "WA":
        wa += 1
print(ac, wa)
