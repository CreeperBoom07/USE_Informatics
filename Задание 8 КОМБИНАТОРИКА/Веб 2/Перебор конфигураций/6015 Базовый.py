from itertools import product as pd

k = 0
for x in pd('012345678', repeat=7):
    if x[0] != '0' and x.count('8') == 1:
        if int(x[0]) % 2 == 0 and int(x[-1]) % 2 != 0:
            k += 1
print(k)
# 376832
