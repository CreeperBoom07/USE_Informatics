from itertools import product as pd
k = 0
for x in pd('0123456789', repeat=3):
    if x[0] != '0':
        int_x = [int(n) for n in x]
        if int_x == sorted(int_x):
            k += 1
print(k)
# 165
