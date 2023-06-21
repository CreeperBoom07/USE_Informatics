from itertools import product as pd

k = 0
for x in pd('0123456789', repeat=3):
    if list(x) == sorted(x) and x[0] != '0':
        k += 1
print(k)


















