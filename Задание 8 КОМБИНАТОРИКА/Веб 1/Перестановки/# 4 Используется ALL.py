from itertools import permutations
k = 0
for x in permutations('ПЕСКАРЬ'):
    s = ''.join(x)
    if s[0] != 'Ь' and all([sub not in s for sub in ('ЬЕ', 'ЬА', 'ЬР')]):
        k += 1
print(k)
