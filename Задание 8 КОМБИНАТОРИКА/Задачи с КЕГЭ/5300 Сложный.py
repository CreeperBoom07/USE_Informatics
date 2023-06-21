from itertools import permutations as pm

k = 0
for x in set(pm('ХОЧУ В ВУЗ')):
    if x[0] != ' ' and x[-1] != ' ':
        s = ''.join(x)
        if '  ' not in s:
            w1, w2, w3 = s.split(' ')
            if all(False if i[0] == 'У' else True for i in (w1, w2, w3)):
                k += 1

print(k-1)

# 75599
'''Пояснение: в задаче сказано посчитать НОВЫЕ предложения, т.е. предложение "ХОЧУ В ВУЗ" считать не надо\
   т.к. Леся его уже составила'''
