def appendAndDelete(s, t, k):
    idx, d = 0, 0
    sd, ta = 0, 0
    flag = False
    if s == t:
        flag = True
    r = min(len(s), len(t))
    for i in range(r):
        if s[i] != t[i]:
            idx = i
            sd = len(s) - idx
            ta = len(t) - idx
            break
        sd = len(s) - r
        ta = len(t) - r
    if sd + ta <= k or flag:
        return "Yes"
    else:
        return "No"


print(appendAndDelete("ashley", "ash", 2))

