def bonAppetit(bill, k, b):
    n = len(bill)
    cost = 0
    for i in range(n):
        if i != k:
            cost += bill[i]
    cost //= 2
    if cost == b:
        print("Bon Appetit")
    else:
        print(b - cost)
