if __name__ == "__main__":
    name, score = [], []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    grade = dict(zip(name, score))
    scmin = min(score)
    mincnt = score.count(scmin)
    grdst = sorted(grade.items(), key=lambda x: x[1])
    for i in range(mincnt):
        grdst.pop(0)

    #grdstリスト[name, score]内の最小値(score)であるnameをminnameに格納
    minname = [
        name for name, value in grdst if value == min(grdst, key=lambda x: x[1])[1]
    ]
    minname.sort()
    for name in minname:
        print(name)
