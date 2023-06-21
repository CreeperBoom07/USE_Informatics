from itertools import product as pd

k = 0
for x in pd('МАСЛО', repeat=6):
    if x.count('А') + x.count('О') == 1:
        k += 1
print(k)

# 2916
