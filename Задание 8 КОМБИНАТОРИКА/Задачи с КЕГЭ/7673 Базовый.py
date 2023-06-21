from itertools import product as pd
a = 0
comb = [''.join(i) for i in pd('ГЕЭ023', repeat=7)]
ind1 = comb.index('2023ЕГЭ')+1
ind2 = comb.index('ЕГЭ2023')+1
print(ind1-ind2-1)
# 166004
