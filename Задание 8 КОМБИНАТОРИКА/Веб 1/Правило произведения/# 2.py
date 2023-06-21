from itertools import product
k = 0
for x in product('КУМА', repeat=5):
    if x[0] in 'КМ' and x[-1] in 'УА':
        k += 1
print(k)
# Или так
k = 0
for x in product('КМ', 'КУМА', 'КУМА', 'КУМА', 'УА'):
    k += 1
print(k)