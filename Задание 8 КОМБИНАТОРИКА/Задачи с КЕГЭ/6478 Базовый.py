from itertools import product as pd

k = 0
for x in pd('МОЛЬ', repeat=5):
    s = ''.join(x)
    if 'ОЬ' not in s and 'ЬЬ' not in s and not s.startswith('Ь'):
        k += 1
print(k)

# 495
