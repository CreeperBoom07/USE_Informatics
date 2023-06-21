from itertools import product
k = 0
for x in product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО'):
    k+=1

print(k)

