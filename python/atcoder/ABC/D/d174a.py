"""
4
WWRR
2
左からWの累積和と右からRの累積和の最大値を比較して、その中の最小値を探す
"""
import itertools

n = int(input())
s = list(input())
left_w = [0]
right_r = [0]
for l in s:
    if l == "W":
        left_w.append(1)
    else:
        left_w.append(0)
lacc = list(itertools.accumulate(left_w))

for r in s[::-1]:
    if r == "R":
        right_r.append(1)
    else:
        right_r.append(0)
racc = list(itertools.accumulate(right_r))
racc = racc[::-1]

print(min(map(max, zip(lacc, racc))))
