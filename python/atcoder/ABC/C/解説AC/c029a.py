MOD = 10 ** 9 + 7
INF = float("INF")


def main():
    def dfs(s):
        if len(s) == n:
            print(s)
        else:
            for char in ("a", "b", "c"):
                dfs(s + char)

    n = int(input())
    dfs("")


if __name__ == "__main__":
    main()
