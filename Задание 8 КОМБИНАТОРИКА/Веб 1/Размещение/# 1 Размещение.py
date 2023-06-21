from itertools import product
k = 0
for x in product('КРОТ', repeat=6):
    if x.count('О') == 1:
        k += 1
print(k)