from itertools import permutations as pm

a = set()
k = 0
for x in pm('МИМИКРИЯ'):
    a.add(''.join(x))
    k += 1
print(len(a))
