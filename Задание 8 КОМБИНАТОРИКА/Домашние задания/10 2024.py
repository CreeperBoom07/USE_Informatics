from itertools import product as pd


k = 0
for x in pd('01234567', repeat=5):
    if x[0] != '0' and '1' not in x and len(x) == len(set(x)):
        s = ''.join(x)
        for n in s:
            if int(n) % 2 == 0:
                s = s.replace(n, '0')
            else:
                s = s.replace(n, '1')
        if '11' not in s and '00' not in s:
            k += 1
print(k)

# 180
        
