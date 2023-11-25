from string import ascii_uppercase as up
from itertools import product as pd

abc = '0123456789' + up
abc = abc[:17]
print(abc[3::2])
k = 0
for x in pd(abc, repeat=5):
    if x[0] != '0':
        s = ''.join(x)
        if s.count('1') <= 2:
            for n in abc[3::2]:
                s = s.replace(n, 'Н')
            if 'Н1' not in s and '1Н' not in s and '11' not in s:
                k += 1
print(k)
# 1117608
