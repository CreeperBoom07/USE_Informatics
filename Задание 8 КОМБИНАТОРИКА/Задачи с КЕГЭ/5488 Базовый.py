from itertools import product as pd

k = 0
for x in pd('ПОЛИНА', repeat=8):
    if x.count('П') + x.count('Л') + x.count('Н') > \
            x.count('О') + x.count('И') + x.count('А'):
        k += 1

print(k)

# 610173
