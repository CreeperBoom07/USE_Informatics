from itertools import permutations

k = 0
for x in permutations('КАРПЫ'):
    s = ''.join(x)
    if 'АЫ' not in s and 'ЫА' not in s and s[0] != 'Р' and s[-1] != 'Р':
        k += 1

print(k)

# 48
