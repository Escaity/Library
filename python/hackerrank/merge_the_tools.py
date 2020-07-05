def merge_the_tools(s, k):
    ks = [""] * (len(s) // k)
    ans = [""] * (len(s) // k)
    for i in range(len(s) // k):
        ks[i] = list(s[0:k])
        s = s[k:]

    for i, v in enumerate(ks):
        for j, w in enumerate(v):
            if str(w) in ans[i]:
                pass
            else:
                ans[i] += str(w)

    """ リストを開業で出力する """
    return print("\n".join(ans))


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
