from itertools import product as pd

k = 0
for x in pd('012345678', repeat=5):
    if x[0] != '0' and x.count('3') == 1:
        s = ''.join(x)
        if all('3'+i not in s and i+'3' not in s for i in '5678'):
            k += 1
print(k)
# 6400      
