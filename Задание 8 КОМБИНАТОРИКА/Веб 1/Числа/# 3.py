from itertools import product as pd
k = 0
for x in pd('12345678',  repeat=5):
    s = ''.join(x)
    if all([s[i] != s[i-1] for i in range(1, len(s))]):
        k += 1
print(k)