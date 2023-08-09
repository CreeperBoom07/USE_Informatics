from itertools import product as pd
'''Если в слове есть повторяющиеся буквы то их надо удалить!!!'''
for ind, val in enumerate(pd(sorted(set('МАРИНА')), repeat=8), start=1):
    if ''.join(val) == 'МАРИАННА':
        print(ind)
        break
