from itertools import permutations as pm

k = 0
for x in set(pm('АМФИБРАХИЙ')):
    s = ''.join(x)
    s = s.replace('И', 'А')
    if 'АА' in s:
        k += 1

print(k)

# 756000
