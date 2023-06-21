from itertools import product
k = 18750

for x in product(set('БЕРСЕРК'), repeat=7):
        k += 1
print(k)

# 96875
