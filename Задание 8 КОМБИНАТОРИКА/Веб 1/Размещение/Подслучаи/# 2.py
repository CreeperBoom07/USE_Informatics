from itertools import product
k = 0
for x in product('КАТЕР', repeat=3):
    if x.count('Р') > 1:
        k += 1
print(k)