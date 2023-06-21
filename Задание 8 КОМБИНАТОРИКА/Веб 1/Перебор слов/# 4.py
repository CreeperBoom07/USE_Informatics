# ВНИМАНИЕ: слова могут быть расположены наоборот
from itertools import product
k = 0
c1 = 0
c2 = 0
for x in product('АОУ', repeat=5):
    s = ''.join(x)
    k += 1
    if s == 'УАУАУ':
        c2 = k
    if s == 'ОУОУА':
        c1 = k

print(c2-c1+1)


