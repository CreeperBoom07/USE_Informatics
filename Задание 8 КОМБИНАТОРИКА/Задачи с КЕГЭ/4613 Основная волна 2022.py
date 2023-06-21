from itertools import product as pd

k = 0
for x in pd('012345678', repeat=5):
    if x[0] != '0' and int(x[0]) % 2 == 0 and x[-1] not in ('1', '8') and x.count('3') <= 1:
        k += 1

print(k)

# 18944
