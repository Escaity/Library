""" test case 4/5 """

import collections

arr = [1, 2, 2]

arc = collections.Counter(arr)
arm = arc.most_common()
print(arm[0][0])
