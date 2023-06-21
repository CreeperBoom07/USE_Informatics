from itertools import product as pd

k = 0
for x in pd('0123456', repeat=5):
    if x[0] != '0' and int(x[0]) % 2 == 0 and int(x[-1]) >= 3 and x.count('4') <= 1:
        k += 1

print(k)

# 3024
