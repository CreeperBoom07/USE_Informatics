with open('9_7811.csv') as file:
    lst = []
    for line in file:
        temp = [int(x) for x in line.split(',')]
        lst.append(temp)

k = 0
for line in lst:
    a, b, c, d, e = sorted(line)
    if len(line) == len(set(line)) and (a+e)/(3*(b+c+d)) < 0.25:
        k += 1
print(k)

# 11420    
