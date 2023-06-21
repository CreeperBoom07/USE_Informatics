from itertools import product as pd
k = 0
for x in pd('01234567', repeat=7):
    if x[0] != '0' and len(x) == len(set(x)):
        s = ''.join(x)
        for i in '01234567':
            if int(i) % 2 == 0:
                s = s.replace(i, '0')
            else:
                s = s.replace(i, '1')
        if '11' not in s and '00' not in s:
            k += 1

print(k)
