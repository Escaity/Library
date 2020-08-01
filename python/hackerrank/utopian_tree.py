def utopianTree(n):
    tree = [0] * (n + 1)
    tree[0] = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            tree[i] = tree[i - 1] + 1
        else:
            tree[i] = tree[i - 1] * 2

    return tree[n]
