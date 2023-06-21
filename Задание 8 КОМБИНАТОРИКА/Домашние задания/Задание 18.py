from itertools import product as pd

k = 1
a = []
for x in pd(sorted('АЛГОРИТМ'), repeat=4):
    s = ''.join(x)
    if s[-2:] == 'ИМ':
        a.append(k)
    k += 1
print(a)



# lst = list(pd(sorted('АЛГОРИТМ'), repeat=4))
# print(lst[4052])
# print(lst[4053])
# print(lst[4054])
