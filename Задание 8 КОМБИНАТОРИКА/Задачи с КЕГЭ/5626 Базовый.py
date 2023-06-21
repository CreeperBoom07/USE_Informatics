from itertools import product as pd

k = 0
for x in pd('01234567', repeat=5):
    if x[0] != '0' and int(x[0]) % 2 == 0 and x[-1] not in ('2', '6') and x.count('7') <= 2:
        k += 1
print(k)

# 9135
