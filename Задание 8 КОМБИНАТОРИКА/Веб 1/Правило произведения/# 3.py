from itertools import product

k = 0
for x in product('АВС', 'АВС', 'АВС', 'АВС', 'АВСХ'):
    k += 1
print(k)