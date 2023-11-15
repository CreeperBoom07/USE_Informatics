from itertools import product as pd
from string import ascii_uppercase as up
s = open('files/24_8654.txt').readline().strip()
lst = []
for a, b, c in pd(up, repeat=3):
    temp = a + 'B' + b + c + 'D'
    lst += [temp]
m = c = 4
for i in range(len(s)-4):
    if s[i:i+5] not in lst:
        c += 1
        m = max(m, c)
    else:
        c = 4
print(m)
# 4187
