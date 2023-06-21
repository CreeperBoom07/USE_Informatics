from itertools import product
k = 0
for i in product('ЛЕТО', repeat=4):
    if i.count('Е') > 0:
        k += 1
print(k)