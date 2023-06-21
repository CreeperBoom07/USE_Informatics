from itertools import product
k = 0
for x in product('ГЕПАРД', repeat=5):
    if x.count('Г') == 1 and x[0] != 'А' and x[-1] != 'Е':
        k += 1
print(k)
            
    
