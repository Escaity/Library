from decimal import Decimal

# decimal型は文字列で渡す
a, b = [Decimal(i) for i in input().split()]
# decimal型→int型に変換
print(int(a * b))

