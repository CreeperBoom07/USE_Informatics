from itertools import product as pd
k = 0
for x in pd('ABCD', repeat=4):
    if list(x) == sorted(x):
        k += 1
print(k)
# 35
