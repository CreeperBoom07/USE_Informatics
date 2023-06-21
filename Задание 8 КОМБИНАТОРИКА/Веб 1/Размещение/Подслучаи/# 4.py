from itertools import product
k = 0
for l in range(4, 7):
    for x in product('АНИМЕ', repeat=l):
        k += 1
print(k)
