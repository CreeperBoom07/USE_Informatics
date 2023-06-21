from itertools import product as pd
k = 0
for x in pd('0123456789ABC', repeat=8):
    if x[0] != '0' and len(set(x)) == 6 and x.count('A') <= 2:
        k += 1
print(k)

# 298322640
