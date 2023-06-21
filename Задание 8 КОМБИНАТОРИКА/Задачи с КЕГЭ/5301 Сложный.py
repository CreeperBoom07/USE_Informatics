from itertools import product as pd

k = 0
for x in pd('леся ', repeat=5):
    if x.count(' ') == 1 and x[0] != ' ' and x[-1] != ' ':
        s = ''.join(x)
        w1, w2 = s.split(' ')
        w1 = w1.replace('я', 'е').replace('с', 'л')
        w2 = w2.replace('с', 'л').replace('я', 'е')
        if 'лл' not in w1 and 'ее' not in w1 \
                and 'лл' not in w2 and 'ее' not in w2:
            k += 1

print(k)

# 192
