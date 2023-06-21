from itertools import product
k = 1
for x in product('АОУ', repeat=5):
    if ''.join(x) == 'УАУАУ':
        print(k)
        break
    else:
        k += 1