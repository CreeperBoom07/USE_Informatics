with open('9_5284.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]
    
k = 0
for line in data:
    p = 0
    a, b, c, d, e, f = sorted(line)
    if (a+f)**2 > b**2 + c**2  + d**2 + e**2:
        p += 1
    if len([n for n in line if line.count(n) == 3]) == 3 and \
    len([n for n in line if line.count(n) == 1]) == 3:
        p += 1
    if p > 0:
        k += 1
print(k)
        
# 4209
