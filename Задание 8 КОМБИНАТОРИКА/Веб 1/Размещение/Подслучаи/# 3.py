from itertools import product
k = 0
for i in product('ЖИРАФ', repeat=5):
    if i.count('Ж') == 1 and i[0] != 'Ф' and i[-1] != 'Р':
        k += 1
print(k)