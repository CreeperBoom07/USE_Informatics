from itertools import product as pd
k = 0
for x in pd('012345678', repeat=6):
    if x[0] != '0':
        n = ''.join(x)
        if int(n, 9) % 2 == 0 and len([i for i in n if int(i) % 2 == 0]) <= 2:
            k += 1
print(k)
# 93696
