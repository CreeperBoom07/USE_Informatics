from itertools import product
k = 1
for x in product('АКРУ', repeat=5):
    if x[0] == 'К':
        print(k)
        break
    k += 1
