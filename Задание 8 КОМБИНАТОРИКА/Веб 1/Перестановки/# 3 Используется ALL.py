from itertools import permutations as pm
k = 0
combinations = ('ОY', 'УO',
                'КЛ', 'КН',
                'ЛК', 'ЛН',
                'НК', 'НЛ')
for x in pm('КОЛУН'):
    s = ''.join(x)
    if all([sub not in s for sub in combinations]):
        k += 1
print(k)