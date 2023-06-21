from itertools import product, p
k = 0
for i in product('ЗЕРКАЛО', repeat=6):
    if i.count('К') == 1 and i.count('А') == 3:
        k += 1
print(k)
