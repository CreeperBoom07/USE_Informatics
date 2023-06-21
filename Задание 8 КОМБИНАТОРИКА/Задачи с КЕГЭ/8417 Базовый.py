from itertools import permutations as pm
k = 0
for x in pm('ЯРОСЛАВ', r=5):
    s = ''.join(x)
    for i in 'ЯОА':
        s = s.replace(i, 'Г')

    for i in 'РСЛВ':
        s = s.replace(i, 'С')
    if s.count('С') > s.count('Г') and 'ГГ' not in s:
        k += 1
print(k)

# 1224
