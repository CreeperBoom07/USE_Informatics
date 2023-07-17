from string import ascii_uppercase
from itertools import product
abc = '0123456789' + ascii_uppercase
abc = abc[:16]

k = 0
for x in product(abc, repeat=3):
    if x[0] != '0' and len(x) == len(set(x)):
        s = ''.join(x)
        for i in '2468ACE':
            s = s.replace(i, '0')
        for i in '3579BDF':
            s = s.replace(i, '1')
        if '11' not in s and '00' not in s:
            k += 1
print(k)

